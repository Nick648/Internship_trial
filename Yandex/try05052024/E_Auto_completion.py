words = {}


def autocomplete(search_str: str) -> int:
    for key in words.keys():
        if not search_str:
            return words[key][1]
        elif key.startswith(search_str):
            return words[key][1]
    return -1


def main():
    global words
    search_str = ''
    n, q = map(int, input().split())
    for i in range(1, n + 1):
        word, pop = input().split()
        words[word] = (pop, i)
    words = dict(sorted(words.items(), key=lambda x: x[1][0], reverse=True))
    for _ in range(q):
        query = input()
        if query == '-':
            search_str = search_str[:-1]
            print(autocomplete(search_str))
        else:
            q_sign, q_char = query.split()
            search_str += q_char
            print(autocomplete(search_str))


if __name__ == '__main__':
    main()

"""
3 6
yandex 10
yacht 1
yoghurt 15
+ y
+ a
+ n
-
-
+ o

3
1
1
1
3
3

"""
