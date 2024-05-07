def main() -> None:
    a, b, c, d = map(int, input().split())
    r = d - b
    if r > 0:
        m = a + c * r
    else:
        m = a
    print(m)


if __name__ == '__main__':
    main()
