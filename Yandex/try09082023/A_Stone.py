if __name__ == '__main__':
    n = int(input())
    quests = list(map(int, input().split()))
    flag = False
    for a in range(len(quests)):
        for i in range(len(quests)):
            if len(set(quests)) == 1:
                break
            if quests[i] != -1:
                if quests[quests[i] - 1] == -1:
                    quests[i] = -1
        if len(set(quests)) == 1 and set(quests) != {-1}:
            break
        elif len(set(quests)) == 1 and set(quests) == {-1}:
            flag = True
            break
    if flag:
        print('Yes')
    else:
        print('No')

'''
6
3 3 5 1 -1 -1

5
3 -1 4 1 2
'''
