def main():
    n = int(input())
    stickers = list(map(int, input().split()))
    k = int(input())
    q_sticker = list(map(int, input().split()))
    stick_sort = set(stickers)
    # stickers.sort()
    for num in q_sticker:
        count = 0
        for stick in stick_sort:
            if stick >= num:
                break
            count += 1
        print(count)


if __name__ == '__main__':
    main()
