class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return f'(x={self.x};y={self.y})'


class Section:
    def __init__(self, x1: int, y1: int, x2: int, y2: int):
        self.point_1 = Point(x=x1, y=y1)
        self.point_2 = Point(x=x2, y=y2)
        self.intersects = False

    def __str__(self):
        return f'p1 = {self.point_1}; p2 = {self.point_2}'


def inter(sec_1: Section, sec_2: Section) -> bool:
    a1 = sec_1.point_1.y - sec_1.point_2.y
    b1 = sec_1.point_2.x - sec_1.point_1.x
    c1 = sec_1.point_1.x * sec_1.point_2.y - sec_1.point_2.x * sec_1.point_1.y
    a2 = sec_2.point_1.y - sec_2.point_2.y
    b2 = sec_2.point_2.x - sec_2.point_1.x
    c2 = sec_2.point_1.x * sec_2.point_2.y - sec_2.point_2.x * sec_2.point_1.y

    # print(f'\n{sec_1} | {sec_2}')
    if b1 * a2 - b2 * a1 and a1:
        y = (c2 * a1 - c1 * a2) / (b1 * a2 - b2 * a1)
        x = (-c1 - b1 * y) / a1
        if min(sec_1.point_1.x, sec_1.point_2.x) <= x <= max(sec_1.point_1.x, sec_1.point_2.x):
            # print('Точка пересечения отрезков есть, координаты: ({0:f}, {1:f}).'.format(x, y))
            sec_1.intersects = True
            sec_2.intersects = True
            return True
        else:
            # print('Точки пересечения отрезков нет.')
            return False
    elif b1 * a2 - b2 * a1 and a2:
        y = (c2 * a1 - c1 * a2) / (b1 * a2 - b2 * a1)
        x = (-c2 - b2 * y) / a2
        if min(sec_1.point_1.x, sec_1.point_2.x) <= x <= max(sec_1.point_1.x, sec_1.point_2.x):
            # print('Точка пересечения отрезков есть, координаты: ({0:f}, {1:f}).'.format(x, y))
            sec_1.intersects = True
            sec_2.intersects = True
            return True
        else:
            # print('Точки пересечения отрезков нет.')
            return False
    else:
        # print('Точки пересечения отрезков нет, отрезки ||.')
        return False


def main():
    n = int(input())
    sections = []
    count_intersects = 0
    for _ in range(n):
        a, b = map(int, input().split())
        sections.append(Section(x1=0, y1=a, x2=1, y2=b))
    for i in range(n - 1):
        section_1 = sections[i]
        for j in range(i + 1, n):
            section_2 = sections[j]
            inter(section_1, section_2)
    for i in range(n):
        if not sections[i].intersects:
            count_intersects += 1
    print(count_intersects)


if __name__ == '__main__':
    main()

"""
5
1 4
2 5
3 1
4 5
5 6

1

=========
5
2 6
3 9
4 2
6 9
9 10

1
"""