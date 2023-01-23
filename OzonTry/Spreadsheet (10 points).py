def output_array(mas: list) -> None:
    for i in range(len(mas)):
        for j in range(len(mas[i])):
            print(mas[i][j], end=' ')
        print()
    print()


if __name__ == '__main__':
    count_data = int(input())
    for _ in range(count_data):
        arr = list()
        input()
        n, m = map(int, input().split())
        for _ in range(n):
            arr.append(list(map(int, input().split())))
        k = int(input())
        query = list(map(int, input().split()))
        # print(f"{arr=}; {n=}; {m=}; {k=}; {query=};")
        for index in query:
            arr = sorted(arr, key=lambda x: x[index - 1])
        output_array(arr)

''' INPUT ->
3

4 3
3 4 1
2 2 5
2 4 2
2 2 1
3
2 1 3

3 1
100
9
10
2
1 1

3 3
2 11 72
99 11 13
2 8 13
5
2 3 2 1 2

OUTPUT ->
2 2 1
3 4 1
2 4 2
2 2 5

9
10
100

2 8 13
2 11 72
99 11 13


'''
