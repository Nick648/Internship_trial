from datetime import datetime, timedelta, date


def write_txt_file(output_data: str) -> None:
    with open("output.txt", "w", encoding="utf-8") as write_file:
        write_file.write(output_data)


def get_weeks(date_1: date, date_2: date) -> tuple[int, list[tuple[date, date]]]:
    week_day = date_1.isoweekday()
    begin_date = date_1
    count_week = 1
    weeks = []
    while begin_date + timedelta(days=(7 - week_day)) < date_2:
        weeks.append((begin_date, begin_date + timedelta(days=(7 - week_day))))
        begin_date += timedelta(days=(7 - week_day) + 1)
        week_day = 1
        count_week += 1
    weeks.append((begin_date, date_2))
    return count_week, weeks


def last_day_of_month(any_date: date) -> date:
    # The day 28 exists in every month. 4 days later, it's always next month
    next_month = any_date.replace(day=28) + timedelta(days=4)
    # subtracting the number of the current day brings us back one month
    return next_month - timedelta(days=next_month.day)


def get_months(date_1: date, date_2: date) -> tuple[int, list[tuple[date, date]]]:
    begin_date = date_1
    months = []
    count_months = 1
    dif = last_day_of_month(begin_date) - begin_date
    while begin_date + dif < date_2:
        months.append((begin_date, begin_date + dif))
        begin_date += dif + timedelta(days=1)
        dif = last_day_of_month(begin_date) - begin_date
        count_months += 1
    months.append((begin_date, date_2))
    return count_months, months


def get_years(date_1: date, date_2: date) -> tuple[int, list[tuple[date, date]]]:
    begin_date = date_1
    years = []
    count_years = 1
    dif = date(year=begin_date.year, month=12, day=31) - begin_date
    while begin_date + dif < date_2:
        years.append((begin_date, begin_date + dif))
        begin_date += dif + timedelta(days=1)
        dif = date(year=begin_date.year, month=12, day=31) - begin_date
        count_years += 1
    years.append((begin_date, date_2))
    return count_years, years


def get_quarters(date_1: date, date_2: date) -> tuple[int, list[tuple[date, date]]]:  # 1-3, 4-6, 7-9, 10-12
    begin_date = date_1
    cur_month = begin_date.month
    if 0 < cur_month < 4:
        next_month = 3
    elif 3 < cur_month < 7:
        next_month = 6
    elif 6 < cur_month < 10:
        next_month = 9
    else:
        next_month = 12
    quarters = []
    count_quarters = 1
    last_day_month = last_day_of_month(date(year=begin_date.year, month=next_month, day=28)).day
    dif = date(year=begin_date.year, month=next_month, day=last_day_month) - begin_date
    while begin_date + dif < date_2:
        quarters.append((begin_date, begin_date + dif))
        begin_date += dif + timedelta(days=1)
        next_month = begin_date.month + 2
        last_day_month = last_day_of_month(date(year=begin_date.year, month=next_month, day=28)).day
        dif = date(year=begin_date.year, month=next_month, day=last_day_month) - begin_date
        count_quarters += 1
    quarters.append((begin_date, date_2))
    return count_quarters, quarters


def get_month_year_for_reviews(cur_month: int, cur_year: int) -> tuple[int, int]:  # 4-9, 10-3
    if 3 < cur_month < 10:
        next_month = 9
        next_year = cur_year
    elif 9 < cur_month < 13:
        next_month = 3
        next_year = cur_year + 1
    else:
        next_month = 3
        next_year = cur_year
    return next_month, next_year


def get_reviews(date_1: date, date_2: date) -> tuple[int, list[tuple[date, date]]]:  # 4-9, 10-3
    begin_date = date_1
    next_month, next_year = get_month_year_for_reviews(begin_date.month, begin_date.year)
    reviews = []
    count_reviews = 1
    last_day_month = last_day_of_month(date(year=next_year, month=next_month, day=28)).day
    dif = date(year=next_year, month=next_month, day=last_day_month) - begin_date
    while begin_date + dif < date_2:
        reviews.append((begin_date, begin_date + dif))
        begin_date += dif + timedelta(days=1)
        next_month, next_year = get_month_year_for_reviews(begin_date.month, begin_date.year)
        last_day_month = last_day_of_month(date(year=next_year, month=next_month, day=28)).day
        dif = date(year=next_year, month=next_month, day=last_day_month) - begin_date
        count_reviews += 1
    reviews.append((begin_date, date_2))
    return count_reviews, reviews


def display_results(result: tuple[int, list[tuple[date, date]]]) -> None:
    count_data = result[0]
    data = result[1]
    # str_info = f"{count_data}\n"
    print(count_data)
    for interval in data:
        date_1 = interval[0]
        date_2 = interval[1]
        # str_info += f"{date_1.strftime('%Y-%m-%d')} {date_2.strftime('%Y-%m-%d')}\n"
        print(f"{date_1.strftime('%Y-%m-%d')} {date_2.strftime('%Y-%m-%d')}")
    # return str_info


# def test_for_development() -> None:
#     today_date = date.today()
#     next_date = today_date + timedelta(days=450)
#     print(f"{today_date=}; {next_date=}")
#     print(get_reviews(today_date, next_date))
#     display_results(get_reviews(today_date, next_date))


def main():
    result = ()
    type_split = input()
    dates_string = input().split()
    month_1, day_1, year_1 = dates_string[0][5:7], dates_string[0][-2:], dates_string[0][:4]
    month_2, day_2, year_2 = dates_string[1][5:7], dates_string[1][-2:], dates_string[1][:4]
    date_str_1 = f"{month_1}-{day_1}-{year_1}"
    date_str_2 = f"{month_2}-{day_2}-{year_2}"
    date_obj_1 = datetime.strptime(date_str_1, '%m-%d-%Y').date()
    date_obj_2 = datetime.strptime(date_str_2, '%m-%d-%Y').date()
    # print(date_obj_1, type(date_obj_1), date_obj_2, type(date_obj_2))
    if type_split == 'WEEK':
        result = get_weeks(date_obj_1, date_obj_2)
    elif type_split == 'MONTH':
        result = get_months(date_obj_1, date_obj_2)
    elif type_split == 'QUARTER':
        result = get_quarters(date_obj_1, date_obj_2)
    elif type_split == 'YEAR':
        result = get_years(date_obj_1, date_obj_2)
    elif type_split == 'REVIEW':
        result = get_reviews(date_obj_1, date_obj_2)
    display_results(result)
    # str_info = display_results(result)
    # write_txt_file(str_info)
    return 0


if __name__ == '__main__':
    ''' !!!У меня данный код работает и выдает правильный ответ на всех тестах!!! '''
    main()
