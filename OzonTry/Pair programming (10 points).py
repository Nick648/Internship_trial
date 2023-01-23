if __name__ == '__main__':
    count_data = int(input())
    for _ in range(count_data):
        count_developer = int(input())
        developers = list(map(int, input().split()))
        for i in range(len(developers) - 1):
            if developers[i] == 0:
                continue
            current_num = i
            next_num = 0
            difference = 120
            for j in range(i + 1, len(developers)):
                if developers[j] == 0:
                    continue
                if abs(developers[current_num] - developers[j]) < difference:
                    next_num = j
                    difference = abs(developers[current_num] - developers[next_num])
                # print(f"{current_num=}; {next_num=}")
            # print(f"{developers=}")
            print(current_num + 1, next_num + 1, sep=' ')
            developers[current_num] = 0
            developers[next_num] = 0
        print()

''' INPUT ->
3
6
2 1 3 1 1 4
2
5 5
8
1 4 2 5 4 2 6 3

OUTPUT ->
1 2
3 6
4 5

1 2

1 3
2 5
4 7
6 8

'''

''' INPUT ->
5
6
7 7 4 4 8 2
8
6 1 2 2 4 1 7 3
4
3 6 2 4
4
3 2 1 3
8
5 4 8 2 1 1 4 4

OUTPUT ->
1 2
3 4
5 6

1 7
2 6
3 4
5 8

1 3
2 4

1 4
2 3

1 2
3 7
4 5
6 8


'''