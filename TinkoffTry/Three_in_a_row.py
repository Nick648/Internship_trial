def check_limit(sum_crystals: int, crystals: list[int], index: int, n_day: int, x_crystals: int, count_day: int):
    # print(f"New -> {sum_crystals=}; {index=}; {count_day=}")
    while True:
        if index >= n_day:
            count_crystal = crystals[-1]
        else:
            count_crystal = crystals[index]
        sum_crystals += count_crystal
        count_day += 1
        index += 1
        # print(f"{sum_crystals=}; {index=}; {count_crystal=}; {count_day=}")
        if sum_crystals == x_crystals:
            return count_day
        if sum_crystals > x_crystals and index != 1:
            return check_limit(sum_crystals - count_crystal, crystals, 0, n_day, x_crystals, count_day)
        elif sum_crystals > x_crystals and index == 1:
            return -1


def main() -> None:
    n_day, x_crystal = map(int, input().split())
    crystals = list(map(int, input().split()))
    ans = check_limit(0, crystals, 0, n_day, x_crystal, 0)
    print(ans)


if __name__ == '__main__':
    main()

"""
    Ex 1:
INPUT:
4 19
2 3 4 5

OUTPUT: 5

    Ex 2:
INPUT:
5 10
1 2 4 8 16

OUTPUT: 6

    Ex 3:
INPUT:
3 10
4 5 3

OUTPUT: -1
"""
