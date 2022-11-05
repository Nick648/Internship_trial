import itertools


def main():
    # letters = []
    combinations = []

    with open('input.txt', 'r') as file:
        s_input = file.read()

    # for letter in s_input:
    #     letters.append(letter)

    st = set(s_input)
    if len(st) == 1:
        with open('output.txt', 'w', encoding='utf-8') as file:
            file.write(str(len(s_input)))
        exit()

    for i in range(2, len(s_input) + 1):
        perm_set = itertools.permutations(s_input, i)
        for item in perm_set:
            if item not in combinations:
                combinations.append(item)

    # for item in combinations:
    #     print(item)

    with open('output.txt', 'w', encoding='utf-8') as file:
        file.write(str(len(combinations) + len(set(s_input))))


if __name__ == '__main__':
    main()
