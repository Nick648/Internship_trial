# import sys
# from memory_profiler import profile
# print(sys.getsizeof(screen))
def out_mat(arr):
    for line in range(len(arr)):
        for row in range(len(arr[line])):
            print(chr(arr[line][row]), end='')
        print()


def comparison(orig, arr):
    for i in range(len(orig)):
        for j in range(len(arr)):
            if orig[i][j] != arr[i][j]:
                return False
    return True


def comparison_arr(orig, arr):
    if orig == arr:
        print('Yes')
        exit()


def main():
    n1, m1 = map(int, input().split())
    pic = [['0' for _ in range(m1)] for _ in range(n1)]
    for i in range(n1):
        a = input()
        for j in range(m1):
            pic[i][j] = ord(a[j])

    n2, m2 = map(int, input().split())
    if (n1 != n2 and m1 != m2) and (n1 != m2 and m1 != n2):
        print('No')
        exit()
    screen = [['0' for _ in range(m2)] for _ in range(n2)]
    for i in range(n2):
        a = input()
        for j in range(m2):
            screen[i][j] = ord(a[j])

    comparison_arr(pic, screen)

    if n1 == n2 and m1 == m2:  # comparison rotate 180 degrees
        screen = [[screen[n1 - i - 1][m1 - j - 1] for j in range(m1)] for i in range(n1)]  # rotate 180
        comparison_arr(pic, screen)

    if n1 == m2 and m1 == n2:  # comparison 90 and 270 degrees
        screen_270 = [[screen[j][i] for j in range(len(screen))] for i in range(len(screen[0]) - 1, -1, -1)]  # left 90
        comparison_arr(pic, screen_270)
        # screen = [[screen[m1 - i - 1][n1 - j - 1] for j in range(n1)] for i in range(m1)]  # rotate 180
        screen = [list(reversed(col)) for col in zip(*screen)]  # rotate right 90
        comparison_arr(pic, screen)
    print('No')


if __name__ == '__main__':
    main()
