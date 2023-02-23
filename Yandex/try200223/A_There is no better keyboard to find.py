def main():
    count_key = int(input())
    keys = list(map(int, input().split()))
    index_row = list(map(int, input().split()))
    count_sym = int(input())
    symbols = list(map(int, input().split()))
    count_switch_row = 0
    previous_row = index_row[keys.index(symbols[0])]
    for i in range(1, count_sym):
        if symbols[i] == symbols[i - 1]:
            continue
        current_row = index_row[keys.index(symbols[i])]
        if current_row != previous_row:
            previous_row = current_row
            count_switch_row += 1
    print(count_switch_row)


if __name__ == '__main__':
    main()
