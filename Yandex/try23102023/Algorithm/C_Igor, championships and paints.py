def get_ans(i: int, j: int) -> int:
    return i & j


def main() -> None:
    count_input = int(input())
    for _ in range(count_input):
        n = int(input())
        sum_n = 0
        sum_list = []
        for i in range(1, n + 1):
            for k in range(i, 1, -1):
                sum_n += sum_list[-((i-k)*3)]
            for j in range(i, n + 1):
                sum_n += get_ans(i, j)
                sum_list.append(get_ans(i, j))

        print(sum_n % (10 ** 9 + 7))


if __name__ == '__main__':
    main()
