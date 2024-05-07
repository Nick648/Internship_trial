def merge(list_1: list, list_2: list, reverse: bool = False):
    merge_list = []
    index_1, index_2 = 0, 0
    for _ in range(len(list_1) + len(list_2)):
        try:
            item_1 = list_1[index_1]
        except IndexError:
            try:
                item_2 = list_2[index_2]
                merge_list.append(item_2)
                index_2 += 1
                continue
            except IndexError:
                return merge_list
        try:
            item_2 = list_2[index_2]
            if item_1 <= item_2 and not reverse:
                merge_list.append(item_1)
                index_1 += 1
            else:
                merge_list.append(item_2)
                index_2 += 1
        except IndexError:
            merge_list.append(item_1)
            index_1 += 1
    return merge_list


def merge_sort(unsorted_list: list, reverse: bool = False):
    if len(unsorted_list) <= 1:
        return unsorted_list
    mid = len(unsorted_list) // 2
    # print(f'{unsorted_list=}; {len(unsorted_list)=}; {mid=}')
    # print(f'\t{unsorted_list[:mid]=}; {unsorted_list[mid::]=}')
    left_list = merge_sort(unsorted_list[:mid], reverse)
    right_list = merge_sort(unsorted_list[mid::], reverse)

    return merge(left_list, right_list, reverse)


def output_arr(arr):
    print(" ".join([str(i) for i in arr]))


def main():
    a_n = int(input())
    a = list(map(int, input().split()))
    c1 = merge_sort(a)
    output_arr(c1)


if __name__ == '__main__':
    main()

'''
5
1 5 2 4 3

1 2 3 4 5
'''
