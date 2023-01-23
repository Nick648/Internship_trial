from timeit import timeit


def get_ans() -> str:
    count_report = int(input())
    reports = tuple(input().split())
    if len(reports) == len(set(reports)):
        return "YES"
    # for i in range(1, count_report):
    for pos, item in enumerate(reports):
        if item == reports[pos - 1]:
            continue
        elif item in reports[:pos]:
            return "NO"
    return "YES"


if __name__ == '__main__':
    count_data = int(input())
    %%timeit
    for _ in range(count_data):
        print(get_ans())
