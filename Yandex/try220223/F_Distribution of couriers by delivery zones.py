def generator_sum(n: int):
    if n == 0:
        yield []
        return

    for p in generator_sum(n - 1):
        p.append(1)
        yield p
        p.pop()
        if p and (len(p) < 2 or p[-2] > p[-1]):
            p[-1] += 1
            yield p


def get_zone(zone: list, k_x: int, k_y: int, n: int, m: int):
    d_max = 0
    for i in range(n):
        if i + k_x > n:
            break
        new_zone = [zone[ind] for ind in range(i, i + k_x)]
        for j in range(m):
            new_d = 0
            if j + k_y > m:
                break
            for line in range(k_x):
                new_d += sum(new_zone[line][j:j + k_y])
            # print(f"{new_d=}")
            if new_d > d_max:
                d_max = new_d
    return d_max


def main():
    k = int(input())

    n, m = map(int, input().split())
    zone = []

    sums = []
    d_max = 0
    for item in generator_sum(k):
        if len(item) == 2 and max(item) <= n and max(item) <= m:
            sums.append(item.copy())

    for _ in range(n):
        arr = list(map(int, input().split()))
        zone.append(arr)

    for sizes in sums:
        new_d = get_zone(zone, sizes[0], sizes[1], n, m)
        if new_d > d_max:
            d_max = new_d
        if sizes[0] != sizes[1]:
            new_d = get_zone(zone, sizes[1], sizes[0], n, m)
            if new_d > d_max:
                d_max = new_d
    print(d_max)


if __name__ == '__main__':
    main()
