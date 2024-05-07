def main():
    split_text = input().replace(',', ' , ').split()
    count_items = len(split_text)
    max_len = len(max(split_text, key=len)) * 3
    if count_items == 1:
        output_text = f"{split_text[0]}"
        begin_index = 1
        line_sym = len(split_text[0])
    elif count_items > 1 and split_text[1] == ',':
        output_text = f"{split_text[0]},"
        begin_index = 2
        line_sym = len(split_text[0]) + 1
    else:
        output_text = f"{split_text[0]}"
        begin_index = 1
        line_sym = len(split_text[0])

    while begin_index < count_items:
        len_word = len(split_text[begin_index])
        if begin_index + 1 != count_items and split_text[begin_index + 1] == ',':
            if line_sym + len_word + 2 <= max_len:
                output_text += f' {split_text[begin_index]},'
                line_sym += len_word + 2
            else:
                output_text += f'\n{split_text[begin_index]},'
                line_sym = len_word + 1
            begin_index += 2
        else:
            if line_sym + len_word + 1 <= max_len:
                output_text += f' {split_text[begin_index]}'
                line_sym += len_word + 1
            else:
                output_text += f'\n{split_text[begin_index]}'
                line_sym = len_word
            begin_index += 1
    print(output_text)


if __name__ == '__main__':
    main()

"""
once upon a time, in a land far far away lived a princess , whose beauty was yet unmatched

once upon a time, in a land
far far away lived a
princess, whose beauty was
yet unmatched

a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,yandex

a, b, c, d, e, f,
g, h, i, j, k, l,
m, n, o, p, yandex

"""
