def main():
    n = int(input())
    pics = list(map(int, input().split()))
    pics.sort()
    # print(pics)
    k = n
    for i in range(n):
        if pics[i] >= k ** 2:
            break
        else:
            k -= 1
    print(k)


if __name__ == '__main__':
    main()
