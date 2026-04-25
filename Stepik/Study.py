def filling_line(kb, ke, con, side, st, count) -> int:
    if side == 'h':
        for g in range(kb, ke, st):
            a[con][g] = count
            count += 1
    elif side == 'v':
        for g in range(kb, ke, st):
            a[g][con] = count
            count += 1
    return count


if __name__ == '__main__':
    n, m = map(int, input().split())
    n, m = 3, 3
    a = [[0] * m for _ in range(n)]
    count = 1
    i_line, j_line = n - 1, m - 1
    north, south, west, east = 0, n - 1, 0, m - 1
    while count <= n * m:
        count = filling_line(kb=west, ke=east + 1, con=north, side='h', st=1, count=count)
        north += 1
        if count > n * m:
            break
        count = filling_line(kb=north, ke=south + 1, con=east, side='v', st=1, count=count)
        east -= 1
        if count > n * m:
            break
        count = filling_line(kb=east, ke=west - 1, con=south, side='h', st=-1, count=count)
        south -= 1
        if count > n * m:
            break
        count = filling_line(kb=south, ke=north - 1, con=west, side='v', st=-1, count=count)
        west += 1
    # print(count)
    for el in a:
        print(*[str(el_i).ljust(3) for el_i in el])
