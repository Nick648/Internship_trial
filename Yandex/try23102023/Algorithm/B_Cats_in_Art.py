def main():
    n, m = map(int, input().split())
    cost = list(map(int, input().split()))
    # min_cost = min(cost)
    # need_while = cost.count(min_cost) < m
    # min_costs = [min_cost]
    # need_buy = m - cost.count(min_cost)
    if m == 1:
        print(1)
    else:
        min_cost = sum(cost)
        min_distance = n
        for i in range(n - 1):
            for j in range(i + m, n):
                mb_min_cost = sum(cost[i:j + 1])
                # print(f'{i=}; {j=}; {cost[i]=}; {cost[j]=}; {cost[i:j+1]=};')
                if mb_min_cost <= min_cost and (j - i + 1) <= min_distance:
                    min_cost = mb_min_cost
                    min_distance = j - i + 1
        print(min_distance)


if __name__ == '__main__':
    main()
