def add_point(abcd: list[int], points: list[tuple[int, int]]):
    # a != c and b != d
    # p1 = (a, b)
    # p2 = (a, d)
    # p3 = (c, b)
    # p4 = (c, d)
    for i in range(len(abcd)):
        for j in range(len(abcd)):
            if len(abcd) > 2:
                for k in range(len(abcd)):
                    if len(abcd) > 3:
                        for f in range(len(abcd)):
                            a, b, c, d = abcd[i], abcd[j], abcd[k], abcd[f]
                            if a != c and b != d:
                                if (a, b) in points and (a, d) in points and (c, b) in points and (c, d) not in points:
                                    points.append((c, d))
                                    return True
                                if (a, b) in points and (a, d) in points and (c, b) not in points and (c, d) in points:
                                    points.append((c, b))
                                    return True
                                if (a, b) in points and (a, d) not in points and (c, b) in points and (c, d) in points:
                                    points.append((a, d))
                                    return True
                                if (a, b) not in points and (a, d) in points and (c, b) in points and (c, d) in points:
                                    points.append((a, b))
                                    return True
                    a, b, c, d = abcd[i], abcd[j], abcd[k], abcd[i]
                    if a != c and b != d:
                        if (a, b) in points and (a, d) in points and (c, b) in points and (c, d) not in points:
                            points.append((c, d))
                            return True
                        if (a, b) in points and (a, d) in points and (c, b) not in points and (c, d) in points:
                            points.append((c, b))
                            return True
                        if (a, b) in points and (a, d) not in points and (c, b) in points and (c, d) in points:
                            points.append((a, d))
                            return True
                        if (a, b) not in points and (a, d) in points and (c, b) in points and (c, d) in points:
                            points.append((a, b))
                            return True
            a, b, c, d = abcd[i], abcd[j], abcd[j], abcd[i]
            if a != c and b != d:
                if (a, b) in points and (a, d) in points and (c, b) in points and (c, d) not in points:
                    points.append((c, d))
                    return True
                if (a, b) in points and (a, d) in points and (c, b) not in points and (c, d) in points:
                    points.append((c, b))
                    return True
                if (a, b) in points and (a, d) not in points and (c, b) in points and (c, d) in points:
                    points.append((a, d))
                    return True
                if (a, b) not in points and (a, d) in points and (c, b) in points and (c, d) in points:
                    points.append((a, b))
                    return True
    return False


def main() -> None:
    count_point = int(input())
    abcd = []
    points = []
    for _ in range(count_point):
        x, y = map(int, input().split())
        if x not in abcd:
            abcd.append(x)
        if y not in abcd:
            abcd.append(y)
        points.append((x, y))
    begin_points = len(points)
    if begin_points < 3 or len(points) < 2:
        print(0)
        return
    while True:
        if not add_point(abcd, points):
            break
    print(len(points) - begin_points)


if __name__ == '__main__':
    main()
