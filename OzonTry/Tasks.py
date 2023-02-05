def check_place(sort_times: list, place: int, place_dict: dict) -> int:
    if sort_times[place] in place_dict:
        return place_dict[sort_times[place]]
    if place > 0:
        if sort_times[place] - sort_times[place - 1] <= 1:
            place = sort_times.index(sort_times[place - 1])
            return check_place(sort_times, place, place_dict)
        else:
            return place + 1
    return place + 1


def check(times: list, num_times: int) -> str:
    sort_times = sorted(times)
    # print(f"{sort_times=}")
    place_dict = {}
    str_ans = ""
    for pos, value in enumerate(times):
        if value in place_dict:
            place = place_dict[value]
        else:
            place = sort_times.index(value)
            # print(f"{place=} AFTER -> ", end=' ')
            place = check_place(sort_times, place, place_dict)
            # print(f"{pos=}; {value=}; {place=}")
            place_dict[value] = place
        str_ans += str(place) + " "
    return str_ans


def main() -> None:
    t = int(input())
    while t:
        num_times = int(input())
        times = list(map(int, input().split()))
        print(check(times, num_times))
        t -= 1


if __name__ == '__main__':
    main()
