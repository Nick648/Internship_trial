def main():
    s = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    max_a, max_b = len(a) - 1, len(b) - 1
    # index_1, index_2 = 0, max_b
    count = 0
    for i in range(max_a + 1):
        for j in range(max_b + 1):
            if a[i] + b[j] == s:
                count += 1
    print(count)
    # while True:
    #     if a[index_1] + b[index_2] == s:
    #         count += 1
    #         if index_1 + 1 > max_a and index_2 - 1 < 0:
    #             break
    #         elif index_1 + 1 <= max_a and index_2 - 1 >= 0:
    #             index_1 += 1
    #             index_2 -= 1
    #         elif index_1 + 1 > max_a and index_2 - 1 >= 0:
    #             index_2 -= 1
    #         elif index_1 + 1 <= max_a and index_2 - 1 < 0:
    #             index_1 += 1
    #     elif a[index_1] + b[index_2] > s:
    #         if index_1 + 1 > max_a and index_2 - 1 < 0:
    #             break
    #         elif index_1 + 1 <= max_a and index_2 - 1 >= 0:
    #             index_1 += 1
    #             index_2 -= 1
    #         elif index_1 + 1 > max_a and index_2 - 1 >= 0:
    #             index_2 -= 1
    #         elif index_1 + 1 <= max_a and index_2 - 1 < 0:
    #             index_1 += 1


if __name__ == '__main__':
    main()
