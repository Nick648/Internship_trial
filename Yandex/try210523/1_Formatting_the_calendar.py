weekdays = {
    "Monday": 1,
    "Tuesday": 2,
    "Wednesday": 3,
    "Thursday": 4,
    "Friday": 5,
    "Saturday": 6,
    "Sunday": 7,
}


def main():
    n_days, weekday = map(str, input().split())
    n_days = int(n_days)
    line = 0
    for _ in range(weekdays[weekday] - 1):
        print('..', end=' ')
        line += 1
    for day in range(1, n_days + 1):
        line += 1
        if line == 8:
            print()
            line = 1
        if day < 10:
            print(f'.{day}', end=' ')
        else:
            print(day, end=' ')


if __name__ == '__main__':
    main()
