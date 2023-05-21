def main():
    n = int(input())
    d = {}
    for _ in range(n):
        a, b = map(int, input().split())
        d[a] = b
    sp = list(map(int, input().split()))
    for i in range(len(sp)):
        sp[i] = d[sp[i]]
    min_l = n
    for i in range(len(sp) - 1):
        for j in range(i + 1, len(sp)):
            if sp[j] == sp[i] and j - i < min_l:
                min_l = j - i
    print(min_l)


if __name__ == '__main__':
    main()
