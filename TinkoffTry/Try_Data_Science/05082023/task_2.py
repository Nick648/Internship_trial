if __name__ == '__main__':
    x = int(input())
    y = int(input())
    n = int(input())
    bugs = [x, x + y]
    if n > 2:
        for i in range(3, n + 1):
            current_bugs = sum(bugs)
            bugs[0] = bugs[1]
            bugs[1] = current_bugs
        print(current_bugs)
    else:
        print(bugs[n - 1])
