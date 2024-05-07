def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    n = int(input())
    all_days = 7 * n
    day = 0
    all_hours = 0
    while day < all_days:
        if day + a > all_days:
            n_day = a - (day + a - all_days)
            day += n_day
            all_hours += (n_day * c)
            break
        else:
            day += a
            all_hours += (a * c)
        if day + b > all_days:
            n_day = b - (day + b - all_days)
            day += n_day
            all_hours += (n_day * d)
            break
        else:
            day += b
            all_hours += (b * d)
    print(all_hours)


if __name__ == '__main__':
    main()
