if __name__ == '__main__':
    count_guns, cash = map(int, input().split())
    guns = list(map(int, input().split()))
    cost = 0
    for cost_gun in guns:
        if cost < cost_gun <= cash:
            cost = cost_gun
    print(cost)
