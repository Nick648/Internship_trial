def search(k: int, p: str):
    f_l = p[0]
    pos = 0
    for key in words.keys():
        if key > f_l:
            return -1
        elif key == f_l:
            if len(words[key]) < k:
                return -1
            cur_pos = 0
            for item in words[key]:
                if item.startswith(p) and cur_pos == k - 1:
                    return pos + 1
                elif item.startswith(p):
                    cur_pos += 1
                    pos += 1
                else:
                    pos += 1
        else:
            pos += len(words[key])


def main():
    for _ in range(q):
        k, p = input().split()
        k = int(k)
        print(search(k, p))


if __name__ == '__main__':
    n, q = map(int, input().split())
    words = {}
    for _ in range(n):
        word = input()
        f_l_k = word[0]
        if f_l_k in words:
            words[f_l_k].append(word)
        else:
            words[f_l_k] = [word]
    del f_l_k
    main()

"""
10 3
aa
aaa
aab
ab
abc
ac
ba
daa
dab
dadba
4 a
2 da
4 da

4
9
-1

"""
