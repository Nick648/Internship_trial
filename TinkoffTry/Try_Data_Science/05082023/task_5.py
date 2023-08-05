if __name__ == '__main__':
    s = input()
    count_o = s.count('O')
    count_w = s.count('W')
    if len(s) % 2 == 0:
        if count_o == count_w:
            count_color = 0
            color_paint = 'X'
        else:
            count_color = abs(count_w - count_o) // 2
            if count_o > count_w:
                color_paint = 'O'
            else:
                color_paint = 'W'
        for i in range(len(s)):
            if i == 0 and s[0] == s[1] and count_color > 0:
                if s[0] == 'W':
                    s = 'O' + s[1::]
                else:
                    s = 'W' + s[1::]
                count_color -= 1
            elif i == len(s) - 1 and s[-1] == s[-2] and count_color > 0:
                if s[0] == 'W':
                    s = s[:-1] + 'O'
                else:
                    s = s[:-1] + 'W'
                count_color -= 1
            else:
                if

    else:
        pass
