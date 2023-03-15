def main():
    n = int(input())
    train = []
    items = {}
    for _ in range(n):
        query = input().split()
        if query[0] == 'add':
            wagons = int(query[1])
            cargo = query[2]
            train.append((wagons, cargo))
            if cargo in items:
                items[cargo] += wagons
            else:
                items[cargo] = wagons
        elif query[0] == 'get':
            cargo = query[1]
            if cargo in items:
                print(items[cargo])
            else:
                print(0)
        elif query[0] == 'delete':
            wagons = int(query[1])
            while wagons:
                last_wagons, last_cargo = train.pop()
                if last_wagons > wagons:
                    train.append((last_wagons - wagons, last_cargo))
                    items[last_cargo] -= wagons
                    wagons = 0
                elif last_wagons == wagons:
                    items[last_cargo] -= wagons
                    wagons = 0
                else:
                    items[last_cargo] -= last_wagons
                    wagons -= last_wagons


if __name__ == '__main__':
    main()
