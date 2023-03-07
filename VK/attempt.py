from itertools import combinations


def t1():
    stone = []
    max_w = 72
    while True:
        w, m = map(int, input().strip().split())
        if not w and not m:
            break
        stone.append((w, m))
    max_money = 0
    print(f'{stone=}')
    for i in range(1, len(stone) + 1):
        print(f'\t{i=}')
        for comb in combinations(stone, i):
            print(f'{comb=}')
            w = [item[0] for item in comb]
            ws = sum([item[0] for item in comb])
            m = [item[1] for item in comb]
            ms = sum([item[1] for item in comb])
            print(f'{ws=}; {ms=}')
            if ms >= max_money and ws <= max_w:
                max_money = ms
                print(f'\tNew m -> {max_money=}; {w=}; {m=}; {comb=}')
    print(max_money)


def t2():
    a = 2
    b = 3
    for i in range(0, 10):
        c = a + b
        a = b
        b = c
        print(b)


def t3():
    fd = {}
    try:
        name = fd['name']
    except KeyError:
        print('error')
        raise
    finally:
        print('finally')


def t4():
    d = {i: i for i in range(10) if (i == pow(i, 2)) and i % 1}
    print(d)
    # d = dict(map(lambda x: pow(x, 2), range(1, 10, 2)))
    # print(d)
    d = dict.fromkeys(range(1, 10, 2), lambda x: x ** 2)
    print(d)
    d = {}
    for i in range(10):
        ({}, d)[i % 2][i] = i ** 2
    print(d)


def t5():
    n = 10
    k = 0
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 1:
                print(1, end=' ')
                k += 1
            else:
                print(0, end=' ')
        print()
    print(f'{k=}')


def t6():
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()

    ax.plot([0, 20], [100, 250], 'r', label='obj1')
    ax.plot([15, 200], [30, 35], 'g', label='obj2')
    ax.plot([0, 200], [10, 20], 'y', label='obj3')
    ax.plot([0, 2], [1, 5], 'p', label='obj4')
    ax.plot([5, 30], [120, 130], 'b', label='obj')
    ax.set(title='Line & Markers - 2 points')
    ax.legend()

    plt.xlabel('Width')
    plt.ylabel('Height')
    ax = fig.gca()
    fig.tight_layout()
    plt.grid()
    plt.show()


if __name__ == '__main__':
    # t1()
    # t2()
    # t3()
    # t4()
    # t5()
    # t6()
    pass

'''
23 13
29 7
19 11
27 25
15 31
14 30
15 35
3 2
27 16
7 36
3 37
0 0

'''
