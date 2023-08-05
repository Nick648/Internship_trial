if __name__ == '__main__':
    n = int(input())
    api_inst = list(map(str, input().split()))
    tested_api = list(map(str, input().split()))
    choice_api = list(map(str, input().split()))
    print(f'{api_inst[0]} {api_inst[1]}')
    for i in range(n - 1):
        if tested_api[i] == api_inst[1]:
            api_inst[1] = choice_api[i]
        else:
            api_inst[0] = api_inst[1]
            api_inst[1] = choice_api[i]
        print(f'{api_inst[0]} {api_inst[1]}')
