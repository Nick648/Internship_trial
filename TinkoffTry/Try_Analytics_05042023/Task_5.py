def main():
    numbers = [i for i in range(1, 16)]
    heroes = []
    item = 0
    for i in range(15):
        hero = []
        for h in range(5):
            if item == len(numbers):
                item = 0
            hero.append(numbers[item])
            item += 1
        item -= 1
        heroes.append(hero)

    for line in heroes:
        print(line)


if __name__ == '__main__':
    main()

# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
