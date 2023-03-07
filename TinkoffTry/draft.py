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


def reg(n: list[int], d: int):
    if sum(n) > 141:
        return 0
    if sum(n) == 141:
        return n
    # print(f'{n=}')
    n.append(n[-1] + d)
    return reg(n, d)


def test():
    for i in range(1, 101):
        for j in range(1, 101):
            a = reg([i], j)
            if a:
                print(f'{a=}; {len(a)=}; {sum(a)=}; {i=}; {j=}')


def check_l_r(desk):
    nw = desk[0][0]
    n = desk[0][1]
    ne = desk[0][2]
    w = desk[1][0]
    c = desk[1][1]
    e = desk[1][2]
    sw = desk[2][0]
    s = desk[2][1]
    se = desk[2][2]
    if n + s + w + e >= 2 and c == 1 or n + s + w + e <= 2 and c == 0:
        return 0
    if nw + c + ne >= 2 and n == 1 or nw + c + ne < 2 and n == 0:
        return 0
    if nw + c + sw >= 2 and w == 1 or nw + c + sw < 2 and w == 0:
        return 0
    if ne + c + se >= 2 and e == 1 or ne + c + se < 2 and e == 0:
        return 0
    if sw + c + se >= 2 and s == 1 or sw + c + se < 2 and s == 0:
        return 0
    if n + w >= 1 and nw == 1 or n + w <= 1 and nw == 0:
        return 0
    if n + e >= 1 and ne == 1 or n + e <= 1 and ne == 0:
        return 0
    if s + w >= 1 and sw == 1 or s + w <= 1 and sw == 0:
        return 0
    if s + e >= 1 and se == 1 or s + e <= 1 and se == 0:
        return 0
    return desk


def l_r():  # 1 -> r; 0 -> l
    op = []
    mat = []
    for i in range(512):
        o = bin(i)[2:]
        while len(o) != 9:
            o = '0' + o
        op.append(o)
    for item in op:
        mat_dop = [[0 for _ in range(3)] for _ in range(3)]
        s = 0
        for i in range(3):
            for j in range(3):
                mat_dop[i][j] = int(item[s])
                s += 1
        mat.append(mat_dop)
    for item in mat:
        a = check_l_r(item)
        if a:
            print(a)


def prob():
    n = 15
    d = {}
    for i in range(n):
        d_dop = {
            'p': n - i,
            'q': i,
            'c': i * 2
        }
        d[i] = d_dop
    mat_x = 0
    for key in d:
        p = d[key]['p']
        q = d[key]['q']
        c = d[key]['c']
        mat_x += 0.8 ** p * 0.2 ** q * c
    print(mat_x)




if __name__ == '__main__':
    # main()
    # test()
    # l_r()
    prob()
