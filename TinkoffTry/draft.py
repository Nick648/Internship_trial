def check_req(quotes: list, wood: int, count_q: int, count_wood: int, count_day: int, cur_i: int) -> int:
    count_day += 1
    new_quotes = quotes[cur_i:]
    for i in range(len(new_quotes)):
        count_wood += max(0, new_quotes[i] - i)
        if count_wood >= wood:
            return count_day  # yield
        check_req(new_quotes, wood, count_q, count_wood, count_day, i + 1)


def main() -> None:
    count_q, wood = map(int, input().split())
    quotes = list(map(int, input().split()))
    if sum(quotes) < wood:
        print(-1)
        return
    min_day = count_q
    quotes.sort(reverse=True)
    count_wood, count_day = 0, 1
    for i in range(count_q):
        count_wood += max(0, quotes[i] - i)
        if count_wood >= wood:
            print(1)
            return
        day = check_req(quotes, wood, count_q, count_wood, count_day, i + 1)
        if day and day < min_day:
            min_day = day
        # for day in check_req(quotes, wood, count_q, count_wood, count_day, i + 1):
        #     print(f"{day=}")
        #     if day and day < min_day:
        #         min_day = day
    print(min_day)


if __name__ == '__main__':
    main()
