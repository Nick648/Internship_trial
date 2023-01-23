if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        print(a + b)

''' INPUT ->
5
256 42
1000 1000
-1000 1000
-1000 1000
20 22

OUTPUT ->
298
2000
0
0
42

'''
