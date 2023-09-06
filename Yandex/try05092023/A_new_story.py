def attempt_2():
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    year_1, month_1, day_1, hour_1, min_1, sec_1 = map(int, input().split())
    year_2, month_2, day_2, hour_2, min_2, sec_2 = map(int, input().split())
    full_sec_1, full_sec_2 = 0, 0
    full_sec_1 += year_1 * 365 * 24 * 60 * 60
    full_sec_2 += year_2 * 365 * 24 * 60 * 60
    for i in range(month_1 - 1):
        full_sec_1 += days_in_month[i] * 24 * 60 * 60
    for i in range(month_2 - 1):
        full_sec_2 += days_in_month[i] * 24 * 60 * 60
    full_sec_1 += day_1 * 24 * 60 * 60
    full_sec_2 += day_2 * 24 * 60 * 60
    full_sec_1 += hour_1 * 60 * 60
    full_sec_2 += hour_2 * 60 * 60
    full_sec_1 += min_1 * 60
    full_sec_2 += min_2 * 60
    full_sec_1 += sec_1
    full_sec_2 += sec_2
    full_sec_delta = full_sec_2 - full_sec_1
    day_delta, sec_delta = full_sec_delta // (60 * 60 * 24), full_sec_delta % (60 * 60 * 24)
    print(day_delta, sec_delta)


if __name__ == '__main__':
    attempt_2()
