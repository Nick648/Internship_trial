def gen(x: int):
    i = 1
    while i < x:
        yield i
        i += 1


def get_ans() -> str:
    count_report = int(input())
    data = input().split()
    data_1 = [data[0]]
    for pos in gen(count_report):
        if data[pos] != data[pos - 1]:
            data_1.append(data[pos])
    if len(data_1) == len(set(data)):
        return "YES"
    else:
        return "NO"


def main() -> None:
    count_data = int(input())
    while count_data:
        print(get_ans())
        count_data -= 1


if __name__ == '__main__':
    main()
    # read_file()
