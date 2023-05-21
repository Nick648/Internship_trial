from itertools import permutations
if __name__ == '__main__':
    mat_oj = 0
    n = int(input())
    cubes = []
    for _ in range(n):
        cubes.append(list(map(int, input().split())))
    combs = permutations(cubes, 2)
    for i_comb in combs:
        print(i_comb)
        cube_1, cube_2 = i_comb[0], i_comb[1]
        for i in cube_1:
            for j in cube_2:
                result = max(i, j) ** 3
                probability = 1/12
                mat_oj += probability * result
    print(probability)

