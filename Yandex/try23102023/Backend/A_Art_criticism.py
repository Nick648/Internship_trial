def main():
    n, m = map(int, input().split())
    criteria = list(map(int, input().split()))
    sum_criteria = 0
    for i in range(m):
        # print(f'{criteria[i]=};')
        if criteria[i]:
            sum_criteria += (criteria[i] ** 2 + sum(criteria[i + 1::]))
    print(sum_criteria)


if __name__ == '__main__':
    main()
