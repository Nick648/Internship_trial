def main():
    count_array = int(input())
    all_array = []
    sum_intimacy = 0
    for _ in range(count_array):
        size_array = int(input())
        arr = list(map(int, input().split()))
        # print(f'\t{arr=}')
        for any_arr in all_array:
            current_intimacy = 0
            # print(f'{any_arr=}; {min(any_arr[1], size_array)=}')
            for min_i in range(min(any_arr[1], size_array)):
                if any_arr[0][min_i] != arr[min_i]:
                    # print(f' !!! {any_arr[min_i]=}; {arr[min_i]=}')
                    break
                current_intimacy += 1
            # print(f'{current_intimacy=}')
            sum_intimacy += current_intimacy
        all_array.append((arr, size_array))
    print(sum_intimacy)


if __name__ == '__main__':
    main()
