import time


def generator(x: int):
    i = 0
    # print(f"Begin generator: {x=}; {i=}")
    while i < x:
        # print(f"In generator 1: {x=}; {i=}")
        yield i
        i += 1
        # print(f"In generator 3: {x=}; {i=}")
    # print(f"End generator: {x=}; {i=}")


def try_gen(count: int) -> None:
    a = []
    # print(f"Begin try_gen: {count=}")
    for pos in generator(count):
        a.append(pos)
        # print(f"In try_gen: {pos=}")
    # print(f"End try_gen: {count=}")


def try_for(count: int) -> None:
    a = []
    for pos in range(count):
        a.append(pos)
        # print(f"In try_for: {pos=}")


def try_while(count: int) -> None:
    a = []
    while count:
        a.append(count)
        # print(f"In try_while: {pos=}")
        count -= 1


if __name__ == '__main__':
    total_count = 10000000
    start = time.time()
    try_gen(total_count)
    print('Total time try_gen:', round(time.time() - start, 3))
    start = time.time()
    try_for(total_count)
    print('Total time try_for:', round(time.time() - start, 3))
    start = time.time()
    try_while(total_count)
    print('Total time try_while:', round(time.time() - start, 3))
