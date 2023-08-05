# def common_elements(list1: list[int], list2: list[int]) -> list[int]:
#     return_list = [element for element in list1 if element in list2]
#     return_list.sort()
#     return return_list


if __name__ == '__main__':
    n = int(input())
    n_op = list(map(int, input().split()))
    m = int(input())
    m_op = list(map(int, input().split()))
    rl = list(set(n_op).intersection(m_op))
    rl.sort()
    for item in rl:
        min_item = min(n_op.count(item), m_op.count(item))
        for i in range(min_item):
            print(item, end=' ')
    print()
