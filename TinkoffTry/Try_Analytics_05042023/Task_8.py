from math import sqrt


def triangle_exists(a: int, b: int, c: int):
    if a + b > c and b + c > a and a + c > b:
        return True
    else:
        return False


def main():
    max_exp = 0
    max_a, max_b, max_c = 0, 0, 0
    for a in range(1, 200):
        for b in range(1, 200):
            for c in range(1, 200):
                if triangle_exists(a, b, c):
                    p = (a + b + c) / 2
                    S = sqrt(p * (p - a) * (p - b) * (p - c))  # Formula Gerona
                    P = a + b + c
                    R = (a * b * c) / (4 * S)
                    exp = (S * P) / (R ** 3)
                    print(f'{a=}; {b=}; {c=}; {exp=}')
                    if exp > max_exp:
                        max_exp = exp
                        max_a, max_b, max_c = a, b, c
    print(f'{max_a=}; {max_b=}; {max_c=}; {max_exp=}')


if __name__ == '__main__':
    main()
