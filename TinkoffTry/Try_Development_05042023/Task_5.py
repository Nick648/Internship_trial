def main():
    a = input()
    strs = []
    if len(set(a)) == 1:
        print(1)
        return
    else:
        for i in range(len(a) - 1):
            for j in range(i + 1, len(a)):
                if i == 0:
                    new_str = a[j::-1] + a[j + 1:]
                    # print(f'{i=}; {j=}; {new_str=}; {a[j::-1]=}; {a[j + 1:]=}')
                else:
                    new_str = a[:i] + a[j:i-1:-1] + a[j + 1:]
                    # print(f'{i=}; {j=}; {new_str=}; {a[:i]=}; {a[j:i-1:-1]=}; {a[j + 1:]=}')
                if new_str not in strs:
                    strs.append(new_str)
        print(len(strs))


if __name__ == '__main__':
    main()
