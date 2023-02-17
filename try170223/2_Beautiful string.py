def main():
    count_replace = int(input())
    data = input()
    length = len(data)
    total_max = 1
    for i in range(length):
        max_s = 1
        k = count_replace
        sym = data[i]
        for j in range(i + 1, length):
            if data[j] == sym:
                max_s += 1
            elif k != 0:
                max_s += 1
                k -= 1
            else:
                break
        if max_s > total_max:
            total_max = max_s
    print(total_max)


if __name__ == '__main__':
    main()
