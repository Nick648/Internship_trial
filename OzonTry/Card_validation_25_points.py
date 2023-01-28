"""
Up/North -> U/N
Down/South -> D/S
Left/West -> L/W
Right/East -> R/E
Up-Right/North-East -> UR/NE
Up-Left/North-West -> UL/NW
Down-Right/South-East -> DR/SE
Down-Left/South-West -> DL/SW
"""


def get_ans_file(file) -> str:
    n, m = map(int, file.readline().split())
    card = []
    passed_colors = []
    for _ in range(n):
        rgb = file.readline()
        rgd_add = [sym for sym in rgb]
        for i in range(m):
            if rgb[i] != '.' and rgb[i] not in passed_colors:
                passed_colors.append(rgb[i])
        card.append(rgd_add)
    for color in passed_colors:
        check_validate(color, card, n, m)
        for pos_l, line in enumerate(card):
            if color in line:
                return "NO"
    return "YES"


def read_data_file(file_path: str) -> str:
    answer_string = ""
    with open(file=file_path, mode='r', encoding='utf-8') as file:
        count_data = int(file.readline())
        while count_data:
            answer_string += get_ans_file(file) + "\n"
            count_data -= 1
    return answer_string


def change_item(card: list, color: str, pos_l: int, pos_s: int, n: int, m: int) -> None:
    card[pos_l][pos_s] = '0'
    if pos_s >= 2 and card[pos_l][pos_s - 2] == color:  # Left
        change_item(card, color, pos_l, pos_s - 2, n, m)
    if pos_s <= m - 3 and card[pos_l][pos_s + 2] == color:  # Right
        change_item(card, color, pos_l, pos_s + 2, n, m)
    if pos_s >= 1 and pos_l >= 1 and card[pos_l - 1][pos_s - 1] == color:  # Up-Left
        change_item(card, color, pos_l - 1, pos_s - 1, n, m)
    if pos_s <= m - 2 and pos_l >= 1 and card[pos_l - 1][pos_s + 1] == color:  # Up-Right
        change_item(card, color, pos_l - 1, pos_s + 1, n, m)
    if pos_s >= 1 and pos_l <= n - 2 and card[pos_l + 1][pos_s - 1] == color:  # Down-Left
        change_item(card, color, pos_l + 1, pos_s - 1, n, m)
    if pos_s <= m - 2 and pos_l <= n - 2 and card[pos_l + 1][pos_s + 1] == color:  # Down-Right
        change_item(card, color, pos_l + 1, pos_s + 1, n, m)
    return


def check_validate(color: str, card: list, n: int, m: int) -> None:
    for pos_l, line in enumerate(card):
        for pos_s, sym in enumerate(line):
            if sym == color:
                change_item(card, color, pos_l, pos_s, n, m)
                return


def get_ans() -> str:
    n, m = map(int, input().split())
    card = []
    passed_colors = []
    for _ in range(n):
        rgb = input()
        rgd_add = [sym for sym in rgb]
        # print(f"{rgd_add=}; {type(rgd_add)}")
        for i in range(m):
            if rgb[i] != '.' and rgb[i] not in passed_colors:
                passed_colors.append(rgb[i])
        card.append(rgd_add)
    # print(f"{card=}\n{passed_colors=}")
    for color in passed_colors:
        check_validate(color, card, n, m)
        # print(f"{color=} -> {card=}")
        for pos_l, line in enumerate(card):
            if color in line:
                return "NO"
    return "YES"


def main() -> None:
    count_data = int(input())
    while count_data:
        print(get_ans())
        count_data -= 1


if __name__ == '__main__':
    main()
