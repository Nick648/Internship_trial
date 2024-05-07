from itertools import combinations


def t_j():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    min_l = max(a)
    min_comb = []
    for comb in combinations(a, k):
        max_el = max(comb)
        min_el = min(comb)
        if (max_el - min_el) / min_el < min_l:
            min_l = (max_el - min_el) / min_el
            min_comb = comb
    print("{:.6f}".format(min_l))
    print(' '.join(map(str, min_comb)))


def t_j_2():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    min_l = max(a)
    min_el_a = sorted(a)
    min_comb = []
    for i in range(0, n - k + 1):
        seg = min_el_a[i:i + k]
        max_el = seg[-1]
        min_el = seg[0]
        if (max_el - min_el) / min_el < min_l:
            min_l = (max_el - min_el) / min_el
            min_comb = seg
    print("{:.6f}".format(min_l))
    print(' '.join(map(str, min_comb)))


def t_k():
    n = int(input())
    n_lines = []
    for _ in range(n):
        n_lines.append(tuple(map(int, input().split())))
    q = int(input())
    q_lines = []
    for _ in range(q):
        count = 0
        # q_lines.append(tuple(map(int, input().split())))
        q_a, q_b, q_c = map(int, input().split())
        for item in n_lines:
            if item[0] * q_a + item[1] * q_b == 0:
                count += 1
        q_lines.append(count)

    for ans in q_lines:
        print(ans)


if __name__ == '__main__':
    # t_j()
    # t_j_2()
    t_k()
