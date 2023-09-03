import itertools


def read_file() -> tuple[int, int]:
    with open(file='input.txt') as file:
        s = file.readline()
    n, k = map(int, s.split())
    return n, k


if __name__ == '__main__':
    n, k = read_file()
    count_1 = 0
    count_2 = 0
    for comb in itertools.combinations_with_replacement([i + 1 for i in range(k)], n):
        print(f'\tComb = {comb}')
        no_repetitions = []
        for real_comb in itertools.permutations(comb):
            if real_comb in no_repetitions:
                continue
            no_repetitions.append(real_comb)
            print(real_comb)
        composition = 1
        for item in comb:
            composition *= item
        count_divider = 1
        for i in range(2, composition // 2 + 1):
            if composition % i == 0:
                count_divider += 1
        if count_divider % 2 == 0:
            count_2 += len(no_repetitions)
        else:
            count_1 += len(no_repetitions)
        print('-' * 30)
    print(count_1 % 1_000_000_007)
