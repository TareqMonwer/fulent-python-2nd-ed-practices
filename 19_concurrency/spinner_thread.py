import itertools
import time
from threading import Event, Thread


def spin(message: str, done: Event) -> None:
    for char in itertools.cycle('\|/-'):
        status = f'\r{char} {message}'
        print(status, end='', flush=True)

        if done.wait(.1):
            break
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='')

def slow():
    time.sleep(3)
    return 42

def supervisor():
    done = Event()
    spinner = Thread(target=spin, args=('Thinking!', done))
    print('Spinner', spinner)
    spinner.start()
    result = slow()
    done.set()
    spinner.join()
    return result

def main():
    result = supervisor()
    print("Answer: ", result)


if __name__ == "__main__":
    main()
