def check_map(i_pos: int, j_pos: int):
    map_steps[i_pos][j_pos] = '!'
    # print(f'{map_steps=}')
    if i_pos < h - 1 and j_pos < w - 1 and map_steps[i_pos + 1][j_pos] == '#' and map_steps[i_pos][j_pos + 1] == '#':
        # print('false 1')
        return False
    elif i_pos < h - 1 and map_steps[i_pos + 1][j_pos] == '#':
        return check_map(i_pos + 1, j_pos)
    elif j_pos < w - 1 and map_steps[i_pos][j_pos + 1] == '#':
        return check_map(i_pos, j_pos + 1)
    elif i_pos == h - 1 and j_pos == w - 1:
        # print('true return')
        return True
    else:
        # print('false last')
        return False


def check_remains():
    for line in map_steps:
        if '#' in line:
            return False
    return True


if __name__ == '__main__':
    h, w = map(int, input().split())
    map_steps = []
    for _ in range(h):
        new_line = input()
        line_mas = [item for item in new_line]
        map_steps.append(line_mas)
    if check_map(0, 0):
        # print('all done')
        if check_remains():
            # print('check remains done')
            print('Possible')
        else:
            # print('check remains fail')
            print('Impossible')
    else:
        # print('fail check map')
        print('Impossible')
