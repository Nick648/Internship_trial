def main():
    v = 42
    print(f"Begin {v=}")
    for i in range(1, 22):
        l = v / (i + 1)
        v -= l
        print(f"{i=}; {v=}")
        # v = v/(i+1) * i
    print(f"End {v=}")


def main_2():
    s = 0
    k = 1
    while s <= 7:
        print(f"Cycle {s=}; {k=}")
        k += 1
        s += k
        print(f"Cycle2 {s=}; {k=}")
    print(f"End {s=}; {k=}")


def main_3():
    a = 10
    b = 5
    if (a > 1) or (a < b):
        a -= 5
    if (a > 1) and (a == b):
        a -= 5
    print(f"{a=}")


def main_4():
    arr = [8, 6, 3, 1, 5, 3, 10]
    print(f"Begin {arr=}")
    for i in range(6):
        for j in range(7 - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            # print(f"New iter: {arr=}")
    print(f"Sorted array: {arr=}")


if __name__ == '__main__':
    # main()
    # main_2()
    # main_3()
    main_4()
