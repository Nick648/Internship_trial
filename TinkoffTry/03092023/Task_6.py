if __name__ == '__main__':
    spirits = {}
    count_spirit, count_quest = map(int, input().split())
    count_gang = count_spirit
    for i in range(1, count_spirit + 1):
        spirits[i] = {'gang': i, 'count_gang': 1}
    for _ in range(count_quest):
        quest = list(map(int, input().split()))
        num_quest = quest[0]
        if num_quest == 1:
            spirit_1, spirit_2 = quest[1], quest[2]
            gang_spirit_1, gang_spirit_2 = spirits[spirit_1]['gang'], spirits[spirit_2]['gang']
            if gang_spirit_1 != gang_spirit_2:
                count_gang += 1
                spirits[spirit_1]['count_gang'] += 1
                spirits[spirit_1]['gang'] = count_gang
                spirits[spirit_2]['count_gang'] += 1
                spirits[spirit_2]['gang'] = count_gang
                for key, value in spirits.items():
                    if value['gang'] == gang_spirit_1 or value['gang'] == gang_spirit_2:
                        spirits[key]['gang'] = count_gang
                        spirits[key]['count_gang'] += 1
        elif num_quest == 2:
            spirit_1, spirit_2 = quest[1], quest[2]
            gang_spirit_1, gang_spirit_2 = spirits[spirit_1]['gang'], spirits[spirit_2]['gang']
            if gang_spirit_1 != gang_spirit_2:
                print('NO')
            else:
                print('YES')
        elif num_quest == 3:
            spirit = quest[1]
            print(spirits[spirit]['count_gang'])
        # print(quest, spirits, sep='\n\t')
