from math import ceil


def get_max_size(list_sizes: list[int], k: int) -> int:
    list_max = [list_sizes.pop(list_sizes.index(max(list_sizes))) for _ in range(k)]
    return sum(list_max)


def get_min_size(list_sizes: list[int], k: int) -> int:
    list_min = [list_sizes.pop(list_sizes.index(min(list_sizes))) for _ in range(k)]
    return sum(list_min)


def main():
    w = int(input())
    n, k = map(int, input().split())
    sizes = []
    for _ in range(n):
        wi, hi = map(int, input().split('x'))
        h1 = ceil((hi * w) / wi)
        sizes.append(h1)
    print(get_min_size(sizes.copy(), k))
    print(get_max_size(sizes.copy(), k))


if __name__ == '__main__':
    main()
