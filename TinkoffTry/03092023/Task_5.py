def main():
    states = {}
    max_roads = []
    count_town, count_road = map(int, input().split())
    town_1, town_2, road = map(int, input().split())
    towns = {road: (town_1, town_2)}
    for i in range(count_road - 1):
        town_1, town_2, road = map(int, input().split())
        not_in = True
        for add_towns in towns.values():
            if town_1 in add_towns or town_2 in add_towns:
                towns[road] = town_1, town_2
                not_in = False
                break
        if not_in:
            set_towns = set()
            for t1, t2 in towns.values():
                set_towns.add(t1)
                set_towns.add(t2)
            states[len(set_towns)] = dict(sorted(towns.items()))
            towns = {road: (town_1, town_2)}
    if towns:
        set_towns = set()
        for t1, t2 in towns.values():
            set_towns.add(t1)
            set_towns.add(t2)
        states[len(set_towns)] = dict(sorted(towns.items()))
    #
    for key, value in states.items():
        # print(key, value, sep=': ')
        for road, towns in value.items():
            max_road = road
            # del value[road]
            # print(road, value, sep=' del -> ')
            set_towns = set()
            for k1, t2 in value.items():
                if k1 > max_road:
                    set_towns.add(t2[0])
                    set_towns.add(t2[1])
            if len(set_towns) < key:
                max_roads.append(max_road)
                break
    print(min(max_roads) - 1)


if __name__ == '__main__':
    main()
