def main():
    candidates_a, candidates_b = 0, 0
    candidates = []
    n = int(input())
    for _ in range(n):
        a, b = map(int, input().split())
        candidates_a += a
        candidates.append((a, b))
    candidates.sort(key=lambda x: (x[0], x[1]), reverse=True)
    index = 0
    while candidates_a >= candidates_b:
        candidates_a -= candidates[index][0]
        candidates_b += candidates[index][0] + candidates[index][1]
        index += 1
    print(index)


if __name__ == '__main__':
    main()

"""
4
2 1
2 2
5 1
1 3

1

5
2 1
2 1
2 1
2 1
2 1

3

1
273 691

"""