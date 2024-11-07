import itertools
import time
from multiprocessing import Process, Event
from multiprocessing import synchronize


def spin(message: str, done: synchronize.Event) -> None:
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
    spinner = Process(target=spin, args=('Thinking!', done))
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
