from itertools import combinations


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


def find_sum():
    for n in range(n_cash * 2):
        for comb in combinations(cash, n + 1):
            if sum(comb) == need_sum:
                final_comb = comb
                return final_comb
    return ()


if __name__ == '__main__':
    # analytics()
    need_sum, n_cash = map(int, input().split())
    cash = list(map(int, input().split()))
    for i in range(0, n_cash + 1, 2):
        cash.insert(i, cash[i])
    ans = find_sum()
    if ans:
        print(len(ans))
        for item in ans:
            print(item, end=' ')
    else:
        print(-1)
