import time
import functools


def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        args_list = [f'{arg!r}' for arg in args]
        args_list.extend(f'{k}={v!r}' for k, v in kwargs.items())
        args_str = ', '.join(args_list)
        print(f'[{elapsed}] {name}({args_str}) -> {result!r}')
        return result
    return clocked


