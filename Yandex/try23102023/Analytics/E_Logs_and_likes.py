import csv
import sys


def resize_maxsize() -> None:
    max_int = sys.maxsize
    while True:
        # decrease the maxInt value by factor 10
        # as long as the OverflowError occurs.
        try:
            csv.field_size_limit(max_int)
            break
        except OverflowError:
            max_int = int(max_int / 10)


def tsv_read() -> list:
    data = []
    with open("logs.tsv", encoding='utf-8') as r_file:
        # Создаем объект reader, указываем символ-разделитель "\t"
        file_reader = csv.reader(r_file, delimiter="\t")
        # Счетчик для подсчета количества строк и вывода заголовков столбцов
        count = 0
        # Считывание данных из CSV файла
        for row in file_reader:
            if count == 0:
                # Вывод строки, содержащей заголовки для столбцов
                print(f'Файл содержит столбцы: {", ".join(row)}')
            else:
                # Вывод строк
                data.append(row)
            count += 1
        print(f'Всего в файле {count} строк.')
    print(f'\tФайл прочитан!')
    return data


def format_data(data) -> None:
    d = []
    for row in data:
        if row[2] not in d:
            d.append(row[2])
    print(d)


def main():
    resize_maxsize()
    data = tsv_read()
    format_data(data)
    # print(data)


if __name__ == '__main__':
    main()
