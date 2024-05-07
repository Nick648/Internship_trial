import csv
import matplotlib.pyplot as plt
from math import sqrt


def csv_read() -> list:
    data = []
    with open("path.csv", encoding='utf-8') as r_file:
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
                data.append(row)
            count += 1
        print(f'Всего в файле {count} строк.')
    print(f'\tФайл прочитан!')
    return data


def format_data(data) -> None:
    for row in data:
        row[0] = float(row[0])
        row[1] = float(row[1])
    print(f'\tДанные отформатированы!')


def draw(data: list[list[float]]) -> None:
    for i in range(len(data) - 1):
        t1, t2 = data[i], data[i + 1]
        x, y = [t1[0], t2[0]], [t1[1], t2[1]]
        # print(f'{t1=}; {t2=};')
        plt.plot(x, y, marker='o')
    plt.ylabel('Y')
    plt.xlabel('X')
    plt.show()


def calculation(data: list[list[float]]):
    dist_mm = 0  # (mm)  1g/m
    for i in range(len(data) - 1):
        t1, t2 = data[i], data[i + 1]
        t1_x, t1_y = t1[0], t1[1]
        t2_x, t2_y = t2[0], t2[1]
        dist_i = sqrt((t2_x - t1_x) ** 2 + (t2_y - t1_y) ** 2)
        dist_mm += dist_i
    dist_m = dist_mm / 1000
    expenditure = dist_m * 1
    round_expen = round(expenditure, 5)
    print(f'{dist_mm=}; {dist_m=}; {expenditure=}; {round_expen=}; ', "{:.5f}".format(expenditure))


def main():
    data = csv_read()
    format_data(data)
    # draw(data)
    calculation(data)


if __name__ == '__main__':
    main()
