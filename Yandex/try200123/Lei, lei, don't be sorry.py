# https://contest.yandex.ru/contest/39459/problems/D/

def get_answer(start: int, end: int, typ: int) -> str:
    sum_ans = 0
    for item in data_base:
        if typ == 1:
            if start <= item[0] <= end:
                sum_ans += item[2]
        elif typ == 2:
            if start <= item[1] <= end:
                sum_ans += (item[1] - item[0])
    return str(sum_ans)


def get_answer_1(start: int, end: int) -> str:
    sum_ans = 0
    for item in data_base_1:
        if start <= item[0] <= end:
            sum_ans += item[2]
        elif item[0] > end:
            break
    return str(sum_ans)


def get_answer_2(start: int, end: int) -> str:
    sum_ans = 0
    for item in data_base_2:
        if start <= item[1] <= end:
            sum_ans += (item[1] - item[0])
        elif item[1] > end:
            break
    return str(sum_ans)


if __name__ == '__main__':
    answer_string = ""
    data_base = list()
    count = int(input())
    for _ in range(count):
        data_base.append(tuple(map(int, input().split())))
    data_base_1 = sorted(data_base, key=lambda x: x[0])
    data_base_2 = sorted(data_base, key=lambda x: x[1])
    query_count = int(input())
    for _ in range(query_count):
        s, e, t = map(int, input().split())
        # answer_string += get_answer(s, e, t) + ' '
        if t == 1:
            answer_string += get_answer_1(s, e) + ' '
        elif t == 2:
            answer_string += get_answer_2(s, e) + ' '
    print(answer_string)

''' INPUT ->
7
3 6 1
4 6 2
3 4 3
4 10 100500
4 11 777
3 8 365
4 8 31
6
6 6 2
6 8 2
5 9 2
3 12 2
9 12 2
8 12 2

OUTPUT: 5 14 14 28 13 22 
'''
