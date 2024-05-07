def main():
    a, b, c = map(int, input().split())
    d = b**2 - 4*a*c
    if d > 0:
        x1 = int((-b-d**0.5)/(2*a))
        x2 = int((-b+d**0.5)/(2*a))
        if x1 > x2:
            print(x2, x1)
        else:
            print(x1, x2)
    elif d == 0:
        x = int(-b/(2*a))
        print(x)
    else:
        print()


if __name__ == '__main__':
    main()