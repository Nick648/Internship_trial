from itertools import combinations
import math


class Analytic:
    def __init__(self, number: int, salary: int):
        self.number = number
        self.salary = salary

    def dif_salary(self, another) -> bool:
        if abs(another.salary - self.salary) <= 8:
            return True
        else:
            return False

    def __str__(self):
        return f"{self.number=}; {self.salary=}"


def analytics():  # For another test
    person = [n for n in range(1, 20)]
    salary = [n for n in range(121, 141)]
    for not_include in range(20):
        count_less = 0
        choose = []
        pers = 0
        for j in range(len(salary)):
            if j == not_include:
                continue
            else:
                choose.append(Analytic(person[pers], salary[j]))
                pers += 1
        for it in choose:
            print(it)
        for comb in combinations(choose, 2):
            if comb[0].dif_salary(comb[1]):
                count_less += 1
        print(f'{count_less=}')


def test_2():
    for a in range(1, 10 ** 4):
        for b in range(1, 10 ** 4):
            if a * a + b == a * (999 - b):
                print(f'{a=}; {b=}')


def test_3():
    a = [1, 1]
    print('i=1 -> 1\ni=2 -> 1')
    for i in range(3, 21):
        a.append(a[i - 2] + a[i - 3] + math.gcd(a[i - 2], a[i - 3]))
        print(f'i={i-1} -> {a[i-1]}')


if __name__ == '__main__':
    # analytics()
    # test_2()
    test_3()
