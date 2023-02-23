# def check_sum(a_list: list[int], x_sum: int) -> bool:
#     s_sum = 0
#     for pos, val in enumerate(a_list):
#         if pos % 2 != 0:
#             s_sum -= val
#         else:
#             s_sum += val
#     if s_sum == x_sum:
#         return True
#     else:
#         return False


def main():
    n, x, = map(int, input().split())
    a_list = list(map(int, input().split()))
    for i in range(n - 1):
        s_sum = 0
        pos = 0
        for j in range(i, n):
            if pos % 2 != 0:
                s_sum -= a_list[j]
            else:
                s_sum += a_list[j]
            if s_sum == x:
                print('YES')
                return
            pos += 1
            # if check_sum(a_list[i:j + 1], x):
            #     print('YES')
            #     return
    print('NO')


if __name__ == '__main__':
    main()
