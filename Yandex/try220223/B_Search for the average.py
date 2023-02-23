def main() -> None:
    n = int(input())
    a_list = list(map(float, input().split()))
    q = int(input())
    while q:
        l, r = map(int, input().split())
        a_dop = [1 / a_list[item] for item in range(l, r + 1)]
        # ans = round((r - l + 1) / sum(a_dop), 6)
        ans = (r - l + 1) / sum(a_dop)
        print(ans)
        q -= 1


if __name__ == '__main__':
    main()
