from math import ceil


def input_data() -> int:
    with open(file='input.txt', mode='r') as file:
        n = int(file.readline().strip())
    return n


def output_data(ans: str) -> None:
    with open(file='output.txt', mode='w') as file:
        file.write(ans)


def get_steps(x: int, i_count: int = 1, corner: float = 0):
    # print(f'Begin get_steps {x=}; {i_count=}; {corner=}')
    x -= i_count * 2
    if x <= 0:
        return x, i_count, corner
    else:
        return get_steps(x, i_count + 1, corner + 0.5)


def move_pol(begin_x: int, begin_y: int, step_x: int, step_y: int, stay_n: int) -> tuple[int, int]:
    # print(f'Begin move_pol {begin_x=}; {begin_y=}; {step_x=}; {step_y=}; {stay_n=}')
    if stay_n <= step_x:
        return begin_x + stay_n, begin_y
    begin_x += step_x
    stay_n -= step_x
    # print(f'Update move_pol {begin_x=}; {begin_y=}; {step_x=}; {step_y=}; {stay_n=}')
    return begin_x, begin_y + stay_n


def move_neg(begin_x: int, begin_y: int, step_x: int, step_y: int, stay_n: int) -> tuple[int, int]:
    # print(f'Begin move_neg {begin_x=}; {begin_y=}; {step_x=}; {step_y=}; {stay_n=}')
    if stay_n <= step_x:
        return begin_x - stay_n, begin_y
    begin_x -= step_x
    stay_n -= step_x
    # print(f'Update move_neg {begin_x=}; {begin_y=}; {step_x=}; {step_y=}; {stay_n=}')
    return begin_x, begin_y - stay_n


def main() -> None:
    n = input_data()
    # print(f'Begin program {n=}')
    stay_step, level, corner = get_steps(n)
    # print(f'After get_steps -> {stay_step=}; {level=}; {corner=}')
    if stay_step <= 0:
        stay_step += level * 2
        level -= 1
        corner = ceil(corner)
    # print(f'Update {stay_step=}; {level=}; {corner=}')
    if level % 2 == 0:
        begin_x, begin_y = corner, corner
        x, y = begin_x, begin_y
        if stay_step:
            x, y = move_neg(begin_x, begin_y, level + 1, level + 1, stay_step)
    elif level % 2 != 0:
        begin_x, begin_y = -corner, -corner
        x, y = begin_x, begin_y
        if stay_step:
            x, y = move_pol(begin_x, begin_y, level + 1, level + 1, stay_step)
    output_data(f"{x} {y}")


if __name__ == '__main__':
    main()
