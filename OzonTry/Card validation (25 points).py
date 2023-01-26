def get_ans() -> str:
    n, m = map(int, input().split())
    card = []
    passed_colors = []
    for _ in range(n):
        rgb = input()
        card.append(rgb)
    for pos, item in enumerate(card):
        # print(item)
        for pos_s, item_s in enumerate(item):
            if item_s != '.' and item_s not in passed_colors:
                passed_colors.append(item_s)
            elif item_s != '.':
                # print(f"{pos} -> {item} -> {pos_s} -> {item_s}")
                # print(f"{card[pos][pos_s-2] != item_s} -> {card[pos][pos_s-2]}")
                # print(f"{card[pos-1][pos_s-1] != item_s} -> {card[pos-1][pos_s-1]}")
                # print(f"{card[pos-1][pos_s+1] != item_s} -> {card[pos-1][pos_s+1]}")
                if pos_s >= 2:
                    a = card[pos][pos_s - 2] != item_s
                else:
                    a = 1
                if pos_s <= m - 3:
                    b = card[pos][pos_s + 2] != item_s
                else:
                    b = 1
                if pos_s >= 1 and pos >= 1:
                    c = card[pos - 1][pos_s - 1] != item_s
                else:
                    c = 1
                if pos_s <= m - 2 and pos >= 1:
                    d = card[pos - 1][pos_s + 1] != item_s
                else:
                    d = 1
                # if pos_s >= 1 and pos <= n - 2:
                #     e = card[pos + 1][pos_s - 1] != item_s
                # else:
                #     e = 1
                # if pos_s <= m - 2 and pos <= n - 2:
                #     f = card[pos + 1][pos_s + 1] != item_s
                # else:
                #     f = 1
                if a and b and c and d:  # and e and f:
                    return "NO"
    # print(f"{passed_colors=}")
    return "YES"


def main() -> None:
    count_data = int(input())
    while count_data:
        print(get_ans())
        count_data -= 1


if __name__ == '__main__':
    main()
