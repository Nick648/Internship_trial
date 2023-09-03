def main(s=None):
    s = input()  # sheriff
    sc = s.count('s')
    hc = s.count('h')
    ec = s.count('e')
    rc = s.count('r')
    ic = s.count('i')
    fc = s.count('f') // 2
    ans = min([sc, hc, ec, rc, ic, fc])
    print(ans)


if __name__ == '__main__':
    # input_data = ['fheriherffazfszkisrrs', 'rifftratatashe', 'thegorillaiswatching']
    main()
