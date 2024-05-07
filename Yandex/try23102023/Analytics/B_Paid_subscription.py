import csv
from datetime import datetime, timedelta, date
import time


def test_data() -> list:
    data = [
        ['0000000000000001', '2023-04-30', 'True'],
        ['0000000000000002', '2023-05-31', 'False'],
        ['0000000000000002', '2023-08-28', 'True'],
        ['0000000000000003', '2023-05-31', 'False'],
        ['0000000000000003', '2023-08-29', 'True'],
        ['0000000000000004', '2023-07-01', 'True'],
        ['0000000000000005', '2023-07-01', 'False'],
    ]
    return data


def csv_read() -> list:
    data = []
    with open("startup_users_visits.csv", encoding='utf-8') as r_file:
        # Создаем объект reader, указываем символ-разделитель ","
        file_reader = csv.reader(r_file, delimiter=",")
        # Счетчик для подсчета количества строк и вывода заголовков столбцов
        count = 0
        # Считывание данных из CSV файла
        for row in file_reader:
            if count == 0:
                # Вывод строки, содержащей заголовки для столбцов
                print(f'Файл содержит столбцы: {", ".join(row)}')
            else:
                # Вывод строк
                data.append([row[0], row[1], row[2]])
            count += 1
        print(f'Всего в файле {count} строк.')
    print(f'\tФайл прочитан!')
    return data


def format_data(data) -> None:
    for row in data:
        # row[1] = datetime.strptime(row[1], '%d.%m.%Y').date()
        row[1] = datetime.strptime(row[1], '%Y-%m-%d').date()
        if row[2] == 'True':
            row[2] = True
        elif row[2] == 'False':
            row[2] = False
    data.sort(key=lambda e: e[1])
    print(f'\tДанные отформатированы и отсортированы!')


def get_dict(data) -> dict:
    first_visit = {}
    for row in data:
        if row[0] not in first_visit:
            first_visit[row[0]] = row[1]
    print(f'Кол-во users {len(first_visit)}')
    print(f'Словарь первых визитов создан!')
    # print(first_visit)
    return first_visit


def get_current_date() -> date:
    sec = time.time()
    return date.fromtimestamp(sec)


def get_count_month(data, key, val) -> int:
    begin_count = 0
    for row in data:
        user_id, date_id, pay = row[0], row[1], row[2]
        if key == user_id and pay is True and date_id >= val and (date_id - val).days + 1 <= 90:
            # print(f'{user_id=}; {pay=}; {date_id=}; {(date_id - val).days=}')
            begin_count += 1
        elif date_id >= val and (date_id - val).days + 1 > 90:
            break
    # print(f'FUNC {key=}; {val=}; {begin_count=}')
    return begin_count


def clear_data(data: list, begin_month, begin_year) -> list:
    clear_date = datetime.strptime(f'{begin_year}-{begin_month}-01', '%Y-%m-%d').date()
    del_data = -1
    for i in range(len(data)):
        if data[i][1] < clear_date:
            del_data = i
        elif data[i][1] >= clear_date:
            break
    if del_data > 10:
        print(f'{del_data=}')
    for i in range(del_data, -1, -1):
        # print(f'{i=}')
        del data[i]
    return data


def run_algorithm(data, begin_date, current_date, first_visit) -> dict:
    count_month = {}
    begin_month, begin_year, begin_count = begin_date.month, begin_date.year, 0
    all_count, current_count = len(first_visit), 0
    for key, val in first_visit.items():
        current_count += 1
        if current_count == round(all_count * 0.1):
            print('\tDone 10%')
        if current_count == round(all_count * 0.25):
            print('\tDone 25%')
        if current_count == round(all_count * 0.5):
            print('\tDone 50%')
        if current_count == round(all_count * 0.75):
            print('\tDone 75%')
        if current_count % 30 == 0:
            data = clear_data(data, begin_month, begin_year)
        if (current_date - val).days < 90:
            if begin_count:
                count_month[f'{begin_year}-{begin_month:0>2}-01'] = begin_count
            break
        if val.month == begin_month and val.year == begin_year:
            begin_count += get_count_month(data, key, val)
        else:
            if begin_count:
                count_month[f'{begin_year}-{begin_month:0>2}-01'] = begin_count
                begin_count = 0
            while True:
                if begin_month == 12:
                    begin_month = 1
                    begin_year += 1
                else:
                    begin_month += 1
                if val.month == begin_month and val.year == begin_year:
                    begin_count += get_count_month(data, key, val)
                    break
    return count_month


def output_ans(count_month: dict) -> None:
    print(count_month)
    print('\tOUTPUT:\n')
    for key_date, val_count in count_month.items():
        print(f'{key_date},{val_count}')


def main():
    data = csv_read()
    # data = test_data()
    format_data(data)
    first_visit = get_dict(data)
    begin_date = data[0][1]
    current_date = get_current_date()
    # print(begin_date, current_date, (current_date - begin_date).days, current_date > begin_date, sep='; ')
    count_month = run_algorithm(data, begin_date, current_date, first_visit)
    output_ans(count_month)


if __name__ == '__main__':
    main()

'''
INPUT:
user_id,date,pay
0000000000000001,2023-04-30,True
0000000000000002,2023-05-31,False
0000000000000002,2023-08-28,True
0000000000000003,2023-05-31,False
0000000000000003,2023-08-29,True
0000000000000004,2023-07-01,True
0000000000000005,2023-07-01,False

OUTPUT:
2023-04-01,1
2023-05-01,1



{'2022-11-01': 133, '2022-12-01': 552, '2023-01-01': 437, '2023-02-01': 949, '2023-03-01': 950, '2023-04-01': 678, '2023-05-01': 954, '2023-06-01': 848, '2023-07-01': 582}
	OUTPUT:

2022-11-01,133
2022-12-01,552
2023-01-01,437
2023-02-01,949
2023-03-01,950
2023-04-01,678
2023-05-01,954
2023-06-01,848
2023-07-01,582
'''
