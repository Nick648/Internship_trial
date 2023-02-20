def main():
    calc = {}
    count_done_fig = 0
    ans = []
    count_fig, count_ice, count_time = map(int, input().split())
    shapes = list(map(int, input().split()))
    for pos, val in enumerate(shapes):
        calc[pos + 1] = abs(val - count_ice)
    calc = sorted(calc.items(), key=lambda x: x[1])  # sort vals
    for item in calc:
        if item[1] <= count_time:
            count_time -= item[1]
            ans.append(str(item[0]))
            count_done_fig += 1
        else:
            break
    print(count_done_fig)
    if count_done_fig:
        print(' '.join(ans))


if __name__ == '__main__':
    main()
