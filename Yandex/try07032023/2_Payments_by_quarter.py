from datetime import datetime, timedelta, date


def last_day_of_month(any_date: date) -> date:
    # The day 28 exists in every month. 4 days later, it's always next month
    next_month = any_date.replace(day=28) + timedelta(days=4)
    # subtracting the number of the current day brings us back one month
    return next_month - timedelta(days=next_month.day)


def get_count_days(date_1: date, date_2: date) -> int:
    begin_date = date_1
    count_days = 0
    while begin_date.month < date_2.month:
        last_day = last_day_of_month(begin_date).day
        count_days += last_day - begin_date.day + 1
        begin_date = begin_date.replace(day=last_day) + timedelta(days=1)
    count_days += date_2.day - begin_date.day + 1
    return count_days


def get_sum_quarters(dates: list, k: int) -> str:  # 1-3, 4-6, 7-9, 10-12
    sum_quarter = 0
    if k == 1:
        date_qua_1 = datetime.strptime('01-01-2022', '%d-%m-%Y').date()
        date_qua_2 = datetime.strptime('31-03-2022', '%d-%m-%Y').date()
    elif k == 2:
        date_qua_1 = datetime.strptime('01-04-2022', '%d-%m-%Y').date()
        date_qua_2 = datetime.strptime('30-06-2022', '%d-%m-%Y').date()
    elif k == 3:
        date_qua_1 = datetime.strptime('01-07-2022', '%d-%m-%Y').date()
        date_qua_2 = datetime.strptime('30-09-2022', '%d-%m-%Y').date()
    elif k == 4:
        date_qua_1 = datetime.strptime('01-10-2022', '%d-%m-%Y').date()
        date_qua_2 = datetime.strptime('31-12-2022', '%d-%m-%Y').date()
    for item in dates:
        date_1, date_2, amount = item[0], item[1], item[2]
        if date_qua_1 <= date_1 <= date_qua_2:
            days_quarter = get_count_days(date_1, date_qua_2)
            days_interval = get_count_days(date_1, date_2)
            if days_interval > days_quarter:
                sum_quarter += amount * days_quarter
            else:
                sum_quarter += amount * days_interval
        elif date_qua_1 <= date_2 <= date_qua_2:
            days_quarter = get_count_days(date_qua_1, date_2)
            sum_quarter += amount * days_quarter
        elif date_1 <= date_qua_1 and date_2 >= date_qua_2:
            days_quarter = get_count_days(date_qua_1, date_qua_2)
            sum_quarter += amount * days_quarter
    sum_quarter = str(round(sum_quarter, 2))
    if sum_quarter != '0':
        if len(sum_quarter[sum_quarter.find('.')+1:]) != 2:
            return sum_quarter + '0'
        return sum_quarter
    return '0.00'


def main():
    n = int(input())
    dates = []
    for _ in range(n):
        amount, date_from, date_finish = input().split()
        date_obj_1 = datetime.strptime(date_from + '-2022', '%d.%m-%Y').date()
        date_obj_2 = datetime.strptime(date_finish + '-2022', '%d.%m-%Y').date()
        am_day = str(int(amount) / get_count_days(date_obj_1, date_obj_2))
        am_day = float(am_day[:am_day.find('.')+3])
        dates.append((date_obj_1, date_obj_2, am_day))
    for q in range(1, 5):
        print(get_sum_quarters(dates, q))


if __name__ == '__main__':
    main()

'''
4
10 10.02 11.05
10 11.12 23.12
100 24.05 30.06
4342 10.07 12.09

'''
