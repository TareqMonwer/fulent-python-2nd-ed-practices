import asyncio
import itertools
import time


async def spin(message: str) -> None:
    for char in itertools.cycle(r'\|/-'):
        status = f'\r{char} {message}'
        print(status, end='', flush=True)

        try:
            await asyncio.sleep(.3)
        except asyncio.CancelledError:
            break
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='')

async def slow():
    await asyncio.sleep(3)
    return 42

async def supervisor():
    spinner = asyncio.create_task(spin('Thinking!'))
    print('Spinner', spinner)

    result = await slow()
    spinner.cancel()
    return result

def main():
    result = asyncio.run(supervisor())
    print("Answer: ", result)


if __name__ == "__main__":
    main()
