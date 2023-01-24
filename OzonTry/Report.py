def gen(x: int):
    i = 0
    while i < x:
        yield i
        i += 1


def get_ans() -> str:
    count_report = int(input())
    reports = tuple(input().split())
    k = reports[0]
    passed = f" {k} "
    if len(reports) == len(set(reports)):
        return "YES"
    for pos in gen(count_report):
        if reports[pos] == k:
            continue
        elif f" {reports[pos]} " in passed:
            return "NO"
        else:
            k = reports[pos]
            passed = f"{passed} {k} "
    return "YES"


def main() -> None:
    count_data = int(input())
    while count_data:
        print(get_ans())
        count_data -= 1


if __name__ == '__main__':
    main()
