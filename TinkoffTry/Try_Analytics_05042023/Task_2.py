def main() -> None:
    values = []
    for a in range(1, 10001):
        for b in range(1, 10001):
            try:
                exp_1 = (a ** 2 + b) / (b ** 2 - a)
                exp_2 = (b ** 2 + a) / (a ** 2 - b)
                if exp_1 % 10 == 0 and exp_2 % 10 == 0:
                    print(f'{a=}; {b=}; {exp_1=}; {exp_2=}')
                    values.append((a, b))
            except ZeroDivisionError:
                # print(f'{a=}; {b=}; division by zero')
                pass
    print(values, '\n', len(values))


if __name__ == '__main__':
    main()
