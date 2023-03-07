def task_1():
    h = list(map(int, input().split()))
    h1 = sorted(h)
    h2 = sorted(h, reverse=True)
    if h == h1 or h == h2:
        print('YES')
    else:
        print('NO')


def task_2():
    n, m, k = map(int, input().split())


def task_3():
    n = int(input())
    s = input()
    min_len = n + 1
    for i in range(n - 4):
        for j in range(i + 3, n):
            s1 = s[i:j + 1]
            # print(f'{i=}; {j=}; {s1=}')
            if len(s1) > min_len:
                break
            if 'a' in s1 and 'b' in s1 and 'c' in s1 and 'd' in s1:
                if len(s1) < min_len:
                    min_len = len(s1)
                # print(f'here {n=}; {min_len=}; {len(s1)=}')
                break
        if min_len == n or min_len == n + 1:
            break
    if min_len == n + 1:
        print(-1)
    else:
        print(min_len)


if __name__ == '__main__':
    # task_1()
    # task_2()
    task_3()
