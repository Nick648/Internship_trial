def insertion_sort(arr: list, reverse: bool = False) -> list:
    for i in range(len(arr)):
        cursor = arr[i]
        pos = i
        # print(f'For {i=}; {cursor=}; {pos=}; {arr=}')

        while pos > 0 and arr[pos - 1] > cursor and not reverse:
            # Меняем местами число, продвигая по списку
            arr[pos] = arr[pos - 1]
            pos = pos - 1
            # print(f'\tWhile {pos=}; {arr[pos]=}; {arr[pos-1]=}; {arr=}')
        while pos > 0 and arr[pos - 1] < cursor and reverse:
            # Меняем местами число, продвигая по списку
            arr[pos] = arr[pos - 1]
            pos = pos - 1
            # print(f'\tWhile {pos=}; {arr[pos]=}; {arr[pos-1]=}; {arr=}')
        # Остановимся и сделаем последний обмен
        arr[pos] = cursor
        # print(f'\tLast for {pos=}; {arr[pos]=}; {cursor=}; {arr=}')

    return arr


def output_arr(arr: list[int], mes: str = "") -> None:
    if mes:
        print(mes)
    arr_for_output = [str(i) for i in arr]
    print(" ".join(arr_for_output))


def main() -> None:
    count = int(input())
    input_arr = list(map(int, input().split()))
    sorted_arr = insertion_sort(input_arr)
    output_arr(sorted_arr, "Sorted arr:")
    reverse_arr = insertion_sort(input_arr, reverse=True)
    output_arr(reverse_arr, "Reverse sorted arr:")


if __name__ == '__main__':
    main()

'''
10
1 5 5 0 2 7 3 4 3 9

0 1 2 3 3 4 5 5 7 9


7
5 0 1 -2 -7 9 1

9 5 1 1 0 -2 -7
'''
