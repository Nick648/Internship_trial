from math import gcd


def main():
    count_black = 1
    count_step = int(input())
    probability_up = 1 * 2 * 6
    probability_down = (1 + 1) * (2 + 1) * (6 + 1)
    count_black += 1
    for i in range(1, count_step):
        print(f'Game {i + 1}')
        new_down = (1 + count_black) * (2 + count_black) * (6 + count_black)
        nok = (probability_down * new_down) // gcd(probability_down, new_down)
        print(probability_down, new_down, nok)
        old_nok = nok // probability_down
        new_nok = nok // new_down
        probability_up = probability_up * old_nok + (1 * 2 * 6) * new_nok
        probability_down = probability_down * old_nok + new_down * new_nok
        count_black += 1
    nod = gcd(probability_up, probability_down)
    print(probability_up, probability_down, nod, count_black)
    print(probability_up // nod, probability_down // nod)


if __name__ == '__main__':
    main()
