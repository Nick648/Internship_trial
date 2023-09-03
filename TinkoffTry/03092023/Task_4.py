from itertools import combinations


def find_sum():
    for n in range(n_cash * 2):
        for comb in combinations(cash, n + 1):
            if sum(comb) == need_sum:
                final_comb = comb
                return final_comb
    return ()


if __name__ == '__main__':
    need_sum, n_cash = map(int, input().split())
    cash = list(map(int, input().split()))
    for i in range(0, n_cash + 1, 2):
        cash.insert(i, cash[i])
    ans = find_sum()
    if ans:
        print(len(ans))
        for item in ans:
            print(item, end=' ')
    else:
        print(-1)
