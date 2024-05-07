def main():
    count_team = int(input())
    teams = list(map(int, input().split()))
    if teams[0] == -1:
        print('NO')
    else:
        new_index = teams[0]
        passed_points = [0, new_index]
        while True:
            new_index = teams[new_index]
            # print(f'{passed_points=}; {new_index=}')
            if new_index == -1:
                print('NO')
                break
            else:
                if new_index in passed_points:
                    print('YES')
                    break
                else:
                    passed_points.append(new_index)


if __name__ == '__main__':
    main()
