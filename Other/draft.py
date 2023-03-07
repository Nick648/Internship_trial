# from check_im import *
from time import sleep


def play(n_disks: int, sourse, receiver, storage, steps: int = 0) -> int:
    """
    Функция перемещения n дисков в головоломке Ханойская башня.
    Аргументы функции:
    Первый аргумент n - integer (целое число), количество дисков в пирамиде.
    sourse, receiver, storage - любого типа.
    Второй аргумент - sourse, стержень с которого перекладываем диски.
    Третий аргумент - receiver, стержень на который перекладываем диски.
    Четвёртый аргумент - storage, стержень на который перекладываем n-1 дисков
    для временного хранения в процессе общей работы.
    Пятый аргумент - steps, количество ходов в игре, возвращаемый аргумент
    Не трудно заметить, что минимальное число ходов, необходимое для решения головоломки,
    равно (2^n − 1), где n — число дисков.
    """
    if n_disks <= 0:
        return steps
    steps = play(n_disks - 1, sourse, storage, receiver, steps + 1)
    print("Диск ", n_disks, " : ", sourse, " --> ", receiver, 'Step =', steps)
    steps = play(n_disks - 1, storage, receiver, sourse, steps)
    return steps


def main():
    count_disks = 3
    steps = play(count_disks, 'a', 'b', 'c')
    print(f'Количество шагов = {steps}')


if __name__ == '__main__':
    main()
