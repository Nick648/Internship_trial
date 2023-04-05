def test_2():
    s = input()
    count_n, count_s = s.count('N'), s.count('S')
    count_e, count_w = s.count('E'), s.count('W')
    if count_n == count_s and count_e == count_w:
        print('Yes')
    else:
        print('No')


def main() -> None:
    s = input()
    coordinates = {'x': 0, 'y': 0}
    for direction in s:
        if direction == 'N':  # up -> +y
            coordinates['y'] += 1
        elif direction == 'S':  # down -> -y
            coordinates['y'] -= 1
        elif direction == 'E':  # right -> +x
            coordinates['x'] += 1
        elif direction == 'W':  # left -> -x
            coordinates['x'] -= 1
        # print(f'{direction=}; {coordinates=}')
    if coordinates['x'] or coordinates['y']:
        print('No')
    else:
        print('Yes')


if __name__ == '__main__':
    test_2()
    main()
