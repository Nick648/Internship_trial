def read_data():
    with open(file="21", mode="r", encoding="utf-8") as file:
        count_data = int(file.readline())
        for _ in range(count_data):
            flag = True
            count_report = int(file.readline())
            reports = list(map(str, file.readline().split()))
            # print(f'{count_data=}; {count_report=}; {len(reports)}; {len(set(reports))}')
            for i in range(1, len(reports)):
                if reports[i] == reports[i - 1]:
                    continue
                elif reports[i] in reports[:i]:
                    flag = False
                    break
            if flag:
                print('YES')
            else:
                print('NO')


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
