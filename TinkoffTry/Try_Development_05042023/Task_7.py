def main():
    n, k = map(int, input().split())
    numbers = []
    ans = 0
    for _ in range(n):
        cur_num = int(input())
        numbers.append(cur_num)
    for i in range(0, n):
        for j in range(i, n):
            len_n = j - i + 1
            sum_n = sum(numbers[i:j + 1])
            # print(f'{numbers[i:j + 1]=}; {sum_n=}; {len_n=}; {sum_n/len_n=}')
            if sum_n / len_n >= k:
                ans += 1
    print(ans)


if __name__ == '__main__':
    main()

# 0 1 2 3 4 5 6 7
