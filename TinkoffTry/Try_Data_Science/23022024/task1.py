def main():
    words = list(map(str, input().split()))
    words_out = []
    for word in words:
        if word == word[::-1]:
            words_out.append(word)
    print(" ".join(words_out))


if __name__ == '__main__':
    main()
