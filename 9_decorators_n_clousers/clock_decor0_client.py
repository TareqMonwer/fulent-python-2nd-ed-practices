import time

# from clock_deco0 import clock
from clock_deco1 import clock


@clock
def snoze(seconds, text="Snozed"):
    time.sleep(seconds)


@clock
def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)


if __name__ == "__main__":
    print("*" * 20, "Calling snoze(0.5)")
    print(snoze(0.5, text="Snoozed"))
    print("*" * 20, "Calling factorial(20)")
    # factorial(20)
    print("20! = ", factorial(20))
