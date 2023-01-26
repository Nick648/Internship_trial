def read_data(file) -> str:
    count_report = int(file.readline())
    reports = tuple(file.readline().split())
    k = reports[0]
    passed = f" {k} "
    if len(reports) == len(set(reports)):
        return "YES"
    for pos in gen(count_report):
        if reports[pos] == k:
            continue
        elif f" {reports[pos]} " in passed:
            return "NO"
        else:
            k = reports[pos]
            passed = f"{passed} {k} "
    return "YES"


def read_file():
    with open(file="37", mode="r", encoding="utf-8") as file:  # file=<_io.TextIOWrapper name='37' ...>
        count_data = int(file.readline())
        while count_data:
            ans = read_data(file)
            print(f"{ans}")
            count_data -= 1

if __name__ == '__main__':
    # read_data()
    # exit()
    count_data = int(input())
    for _ in range(count_data):
        flag = True
        count_report = int(input())
        reports = list(map(int, input().split()))
        for i in range(1, len(reports)):
            if reports[i] == reports[i-1]:
                continue
            elif reports[i] in reports[:i]:
                flag = False
                break
            print(f"\t{reports[i]}")
            # if reports[i] in reports[:i] and reports[i - 1] != reports[i]:
            #     flag = False
            #     break
        if flag:
            print('YES')
        else:
            print('NO')


import time

global_start = time.time()

with open('data.data', 'r') as input_file:
    for report_num in range(int(input_file.readline())):
        time_in_cycle = time.time()
        number_of_data = int(input_file.readline())
        data = input_file.readline().split()
        for i in range(number_of_data-1):
            if data[i] == data[i+1]:
                data = data[:i] + data[i+1:]
        data.sort()
        for i in range(number_of_data-1):
            if data[i] == data[i+1]:
                print(i, data[i])
        print(f'ITER #{report_num}: {round(time.time() - time_in_cycle, 3)}')
    print('TOTAL:', round(time.time() - global_start, 3))


    # reports = tuple(input().split())
    # k = reports[0]
    # passed = f" {k} "
    # if len(reports) == len(set(reports)):  # For test 36
    #     return "YES"
    # for pos in gen(count_report):
    #     if reports[pos] == k:
    #         continue
    #     elif f" {reports[pos]} " in passed:
    #         return "NO"
    #     else:
    #         k = reports[pos]
    #         passed = f"{passed} {k} "
    # return "YES"

''' INPUT ->
5
5
1 2 3 4 5
4
1 2 3 1
8
2 3 4 8 5 5 5 5
5
1 1 3 2 2
5
1 1 2 3 2

OUTPUT ->
YES
NO
YES
YES
NO

'''

