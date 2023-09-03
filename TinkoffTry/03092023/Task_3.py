def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    i = 0
    while True:
        if a and a[i] == b[i]:
            del a[i]
            del b[i]
            i -= 1
        else:
            break
        i += 1
    if a:
        for i in range(len(a) - 1, -1, -1):
            if a and a[i] == b[i]:
                del a[i]
                del b[i]
            else:
                break
    else:
        print('YES')
        return
    if a:
        a.sort()
        if a == b:
            print('YES')
        else:
            print('NO')
    else:
        print('YES')


if __name__ == '__main__':
    main()
