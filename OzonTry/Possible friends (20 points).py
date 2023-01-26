def get_ans(users: dict, user: int) -> str:
    if user in users:
        a = []
        answer = [0]
        max_coincidence = 0
        # friends = users[user]
        for friend in users[user]:
            for fr in users[friend]:
                if fr != user and fr not in a and fr not in users[user]:
                    a.append(fr)
                    con = len(set(users[user]) & set(users[fr]))
                    if con == max_coincidence:
                        answer.append(fr)
                    elif con > max_coincidence:
                        answer = [fr]
                        max_coincidence = con
        answer.sort()
        answer_str = f"{answer[0]}"
        answer.pop(0)
        for it in answer:
            answer_str = f"{answer_str} {it}"
        return answer_str
    else:
        return "0"


def main() -> None:
    n, m = map(int, input().split())
    friends = dict()
    while m:
        f1, f2 = map(int, input().split())
        if f1 in friends:
            friends[f1].append(f2)
        else:
            friends[f1] = [f2]
        if f2 in friends:
            friends[f2].append(f1)
        else:
            friends[f2] = [f1]
        m -= 1
    m = 1
    # for item in friends:
    #     print(f"{item} -> {friends[item]}")
    while m <= n:
        print(get_ans(friends, m))
        m += 1


if __name__ == '__main__':
    main()
