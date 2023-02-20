alphabet_index = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l',
                  12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w',
                  23: 'x', 24: 'y', 25: 'z'}

alphabet_chr = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11,
                'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22,
                'x': 23, 'y': 24, 'z': 25}


def check_create_alphabet():
    a = ord('a')
    alphabet_1 = {}
    alphabet_2 = {}
    for i in range(26):
        print(f"{chr(a + i)} -> {a + i}")
        alphabet_1[i] = chr(a + i)
        alphabet_2[chr(a + i)] = i
    print(alphabet_1)
    print(alphabet_2)


def create_spell(max_len_spell: int, symbols: str, p_index: list[int], d_shift: list[int], begin_index: int) -> int:
    total_power = 0
    total_spell = ''
    m_repetition = [0 for _ in range(len(symbols))]
    total_spell += symbols[begin_index]
    m_repetition[begin_index] += 1
    total_power += 1
    next_index = p_index[begin_index] - 1
    total_len = 1
    for _ in range(max_len_spell - 1):
        m_repetition[next_index] += 1
        m_repeat = m_repetition[next_index]
        new_sym = symbols[next_index]
        if m_repeat > 1:
            index_chr = alphabet_chr[new_sym]
            index_another_sym = (index_chr + (m_repeat - 1) * d_shift[next_index]) % 26
            # index_another_sym = (ord(new_sym) + (m_repeat - 1) * d_shift[next_index]) % 123
            new_sym = alphabet_index[index_another_sym]
        total_spell += new_sym
        # total_power += len(set(total_spell))
        if new_sym not in total_spell:
            total_len += 1
        total_power += total_len
        next_index = p_index[next_index] - 1
    # print(f"\t{total_spell=}; {total_power=}")
    return total_power


def main():
    count_sym, max_len_spell = map(int, input().split())
    symbols = input()
    p_index = list(map(int, input().split()))
    d_shift = list(map(int, input().split()))
    total_power = 0
    for index in range(count_sym):
        total_power += create_spell(max_len_spell, symbols, p_index, d_shift, index)
    print(total_power)


if __name__ == '__main__':
    main()
    # check_create_alphabet()
