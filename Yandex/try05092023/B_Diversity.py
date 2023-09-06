if __name__ == '__main__':
    count_card_a, count_card_b, count_quest = map(int, input().split())
    cards_a = list(map(int, input().split()))
    cards_b = list(map(int, input().split()))
    count_diff = 0
    # answers = []
    for item in cards_a:
        if item not in cards_b:
            count_diff += 1
    for item in cards_b:
        if item not in cards_a:
            count_diff += 1
    for i in range(count_quest):
        type_q, player, card = map(str, input().split())
        card = int(card)
        if type_q == '1':
            count_diff_card_before = abs(cards_a.count(card) - cards_b.count(card))
            if player == 'A':
                cards_a.append(card)
            elif player == 'B':
                cards_b.append(card)
            count_diff_card_after = abs(cards_a.count(card) - cards_b.count(card))
            if count_diff_card_before < count_diff_card_after:
                count_diff += 1
            elif count_diff_card_before > count_diff_card_after:
                count_diff -= 1
        elif type_q == '-1':
            count_diff_card_before = abs(cards_a.count(card) - cards_b.count(card))
            if player == 'A':
                cards_a.remove(card)
            elif player == 'B':
                cards_b.remove(card)
            count_diff_card_after = abs(cards_a.count(card) - cards_b.count(card))
            if count_diff_card_before < count_diff_card_after:
                count_diff += 1
            elif count_diff_card_before > count_diff_card_after:
                count_diff -= 1
        # answers.append(count_diff)
        print(count_diff, end=' ')
    # for ans in answers:
    #     print(ans, end=' ')
