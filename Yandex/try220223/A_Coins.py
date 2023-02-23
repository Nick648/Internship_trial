import itertools


def get_count_second(n: int, count_p: int):
    pass


def get_count_first(n: int, count_o: int):
    coins = ['O' for _ in range(count_o)]
    combs = []
    for _ in range(n - count_o):
        coins.append('P')
    print(f"\t{coins=}")
    comb_set = itertools.permutations(coins)
    for item in comb_set:
        if item not in combs:
            print(item)
            combs.append(item)
            for i in range(n - count_o + 1, n):
                get_count_second(n, n - count_o)
    # print(f"{comb_set=}")


def main():
    n = int(input())
    # count_done = 1
    # for i in range(1, n + 1):
    #     get_count_first(n, i)
    print(0.5)


if __name__ == '__main__':
    main()
