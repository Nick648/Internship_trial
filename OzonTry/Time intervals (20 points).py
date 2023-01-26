from datetime import time


def check_valid_2(arr_times: list, cur_t1, cur_t2) -> int:
    if cur_t1 > cur_t2:
        return 0
    # print(f"Begin {arr_times=}")
    left, right = 0, len(arr_times)
    while left != right:
        mid = (left + right) // 2
        t1, t2 = arr_times[mid]
        # print(f"\tBEGIN {left=}; {right=}; {mid=}; {arr_times=}; {(cur_t1, cur_t2,)}; {arr_times[mid]=}")
        if cur_t1 < t1 and cur_t2 < t1:
            right = mid
        elif cur_t1 > t2 and cur_t2 > t2:
            left = mid + 1
        else:
            return 0
    arr_times.insert(right, (cur_t1, cur_t2,))
    # print(f"End {left=}; {right=}; {mid=}; {arr_times=}")
    return 1


def get_ans() -> str:
    count_time = int(input())
    arr = []
    flag = 1
    while count_time:
        count_time -= 1
        t1, t2 = tuple(input().split('-'))
        h1, m1, s1 = map(int, t1.split(':'))
        h2, m2, s2 = map(int, t2.split(':'))
        if 0 <= h1 <= 23 and 0 <= m1 <= 59 and 0 <= s1 <= 59 and 0 <= h2 <= 23 and 0 <= m2 <= 59 and 0 <= s2 <= 59:
            t1 = time(h1, m1, s1)
            t2 = time(h2, m2, s2)
            if not check_valid_2(arr, t1, t2):
                flag = 0
                break
        else:
            flag = 0
            break
    if flag:
        return "YES"
    else:
        while count_time:
            input()
            count_time -= 1
        return "NO"


def main() -> None:
    count_data = int(input())
    while count_data:
        print(get_ans())
        count_data -= 1


if __name__ == '__main__':
    main()
