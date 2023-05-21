if __name__ == '__main__':
    cost = 0
    k, n = map(int, input().split())
    colors = list(map(int, input().split()))
    k_colored = n // k
    will_colored = n % k
    cost += sum(colors) * k_colored
    while will_colored:
        min_cost = min(colors)
        cost += min_cost
        will_colored -= 1
        colors.pop(colors.index(min_cost))
    print(cost)
