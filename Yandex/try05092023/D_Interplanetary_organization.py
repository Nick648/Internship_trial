class Employee:
    def __init__(self, name: int, lang: str, parent=None):
        self.name = name
        self.lang = lang
        self.parent = parent
        if parent:
            if self.lang == 'A' and self.lang in parent.lang:
                self.barrier = 0
                self.barrier_a = 0
                self.barrier_b = parent.barrier_b + 1
            elif self.lang == 'B' and self.lang in parent.lang:
                self.barrier = 0
                self.barrier_a = parent.barrier_a + 1
                self.barrier_b = 0
            elif parent.lang != self.lang == 'B':
                self.barrier = parent.barrier_b
                self.barrier_a = 1
                self.barrier_b = 0
            elif parent.lang != self.lang == 'A':
                self.barrier = parent.barrier_a
                self.barrier_a = 0
                self.barrier_b = 1

        else:
            self.barrier = 0
            self.barrier_a = 0
            self.barrier_b = 0
        # self.birthday()

    def birthday(self):
        if self.parent is None:
            parent = 'Boss'
        else:
            parent = self.parent.name
        print(
            f'{self.name} was born from {parent}; {self.lang=}; {self.barrier_a=}; {self.barrier_b=}; {self.barrier=}')


def main():
    count_employees = int(input())
    langs_employees = list(map(str, input().split()))
    hierarchy = list(map(int, input().split()))
    employees = []
    len_employees = 1
    parent = 0
    employees.append(Employee(0, 'AB'))
    for i in range(1, 2 * (count_employees + 1) - 1):
        if hierarchy[i] != hierarchy[i - 1] and hierarchy[i] >= len_employees:
            for p in range(hierarchy[i] - 1, -1, -1):
                l_index = hierarchy.index(p)
                r_index = hierarchy.index(p, l_index + 1)
                # print(f'{p=}; {l_index=}; {r_index=}; {hierarchy[l_index+1:r_index]}')
                if hierarchy[i] in hierarchy[l_index + 1:r_index]:
                    parent = p
                    break
            employees.append(Employee(hierarchy[i], langs_employees[hierarchy[i] - 1], employees[parent]))
            len_employees += 1
    for em in range(1, len_employees):
        print(employees[em].barrier, end=' ')


if __name__ == '__main__':
    main()
