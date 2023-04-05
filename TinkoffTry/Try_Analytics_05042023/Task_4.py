def main():
    # print(2021**2021)
    # print(2021**2022)
    a1 = 2021**2021
    an = a1
    for i in range(2, 2021**2022+1):
        for k in range(1, i):
            if i % 2 == 0:
                if (an - k) % k == 0:
                    print(f'{i=}; {k=};')
                    an -= k
                    break
            else:
                if (an + k) % k == 0:
                    print(f'{i=}; {k=};')
                    an += k
                    break


if __name__ == '__main__':
    main()