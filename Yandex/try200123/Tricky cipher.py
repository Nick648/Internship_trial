# https://contest.yandex.ru/contest/39459/problems/A/

alphabet_en_str = 'abcdefghijklmnopqrstuvwxyz'
alphabet_ru_str = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
alphabet_en = dict()
alphabet_ru = dict()

for alpha in alphabet_en_str:
    alphabet_en[alpha] = alphabet_en_str.index(alpha) + 1
for alpha in alphabet_ru_str:
    alphabet_ru[alpha] = alphabet_ru_str.index(alpha) + 1


# print(f"{alphabet_en=}")
# print(f"{alphabet_ru=}")


def get_shifr(data: str) -> str:
    f, i, o, d, m, y = data.strip().split(',')
    letter_count = set()
    for letter in f:
        letter_count.add(letter)
    for letter in i:
        letter_count.add(letter)
    for letter in o:
        letter_count.add(letter)
    sum_d_m = 0
    for sym in d:
        sum_d_m += int(sym)
    for sym in m:
        sum_d_m += int(sym)
    first_f_num = alphabet_en[f[0].lower()]
    shifr = len(letter_count) + sum_d_m * 64 + first_f_num * 256
    hex_shifr = hex(shifr).upper()[2:]
    if len(hex_shifr) == 3:
        ans_shifr = hex_shifr
    elif len(hex_shifr) > 3:
        ans_shifr = hex_shifr[-3:]
    elif len(hex_shifr) < 3:  # never will be
        ans_shifr = hex_shifr
        while len(ans_shifr) != 3:
            ans_shifr = '0' + ans_shifr
    # print(f"{shifr=} -> {hex_shifr=};{type(hex_shifr)} -> {ans_shifr=}")
    return ans_shifr


if __name__ == '__main__':
    answer_string = ""
    count = int(input())
    for _ in range(count):
        candidate = input()
        answer_string += get_shifr(candidate) + ' '
    print(answer_string)

''' INPUT
2
Volozh,Arcady,Yurievich,11,2,1964
Segalovich,Ilya,Valentinovich,13,9,1964

OUTPUT: 710 64F 
'''
