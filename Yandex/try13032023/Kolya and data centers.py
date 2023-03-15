def main():
    n, s, q = map(int, input().split())
    data_centres = {}
    for i in range(1, n + 1):
        d = {'R': 0, 'A': s, 'R*A': 0, 'servers': [1 for _ in range(s)]}
        data_centres[i] = d
    # print(f'{data_centres=}')
    for _ in range(q):
        query = list(input().split())
        # print(f'{query} -> {data_centres=}')
        if query[0] == 'RESET':
            center_number = int(query[1])
            data_centres[center_number]['R'] += 1
            data_centres[center_number]['A'] = s
            data_centres[center_number]['servers'] = [1 for _ in range(s)]
            data_centres[center_number]['R*A'] = data_centres[center_number]['R'] * data_centres[center_number]['A']
        elif query[0] == 'DISABLE':
            center_number = int(query[1])
            server_number = int(query[2])
            val = data_centres[center_number]['servers'][server_number - 1]
            if val == 1:
                data_centres[center_number]['servers'][server_number - 1] = 0
                data_centres[center_number]['A'] -= 1
                data_centres[center_number]['R*A'] = data_centres[center_number]['R'] * data_centres[center_number]['A']
        elif query[0] == 'GETMAX':
            max_val = max([(data_centres[item]['R*A'],item) for item in data_centres], key=lambda x: x[0])
            print(max_val[1])
        elif query[0] == 'GETMIN':
            min_val = min([(data_centres[item]['R*A'], item) for item in data_centres], key=lambda x: x[0])
            print(min_val[1])


if __name__ == '__main__':
    main()

'''
3 3 12
DISABLE 1 2
DISABLE 2 1
DISABLE 3 3
GETMAX
RESET 1
RESET 2
DISABLE 1 2
DISABLE 1 3
DISABLE 2 2
GETMAX
RESET 3
GETMIN

2 3 9
DISABLE 1 1
DISABLE 2 2
RESET 2
DISABLE 2 1
DISABLE 2 3
RESET 1
GETMAX
DISABLE 2 1
GETMIN

'''