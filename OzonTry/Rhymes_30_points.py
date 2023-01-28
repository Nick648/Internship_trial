from difflib import SequenceMatcher
from time import time


def get_ans_file_2(file, dictionary: list) -> str:
    word_query = file.readline().strip()
    len_word_query = len(word_query)
    ans, len_ans = "", 0
    for pos, word in enumerate(dictionary):
        if len_ans == len_word_query:
            return ans
        if word != word_query:
            coincidence = 0

            match = SequenceMatcher(None, word, word_query).find_longest_match(0, len(word), 0, len_word_query)

            # print(f"{match=}; {match.size=}")  # -> Match(a=0, b=15, size=9)
            # print(word[match.a:match.a + match.size])  # -> apple pie
            # print(word_query[match.b:match.b + match.size])  # -> apple pie

            # print(match, word, word_query)
            if match.size > len_ans:
                ans, len_ans = word, match.size

    if ans:
        return ans
    else:
        return "None"


def get_ans_file(file, dictionary: list) -> str:
    word_query = file.readline().strip()
    len_word_query = len(word_query)
    ans, len_ans = "", 0
    ans_add, len_ans_add = "", 0
    for pos, word in enumerate(dictionary):
        if len_ans == len_word_query:
            return ans
        if word != word_query:
            coincidence = 0
            # print(f"{word_query=}; {word=}")
            for i in range(1, len(word) + 1):
                # print(f"Eq: {word[-i:]} == {word_query[-i:]} -> {word[-i:] == word_query[-i:]}")
                if word[-i:] == word_query[-i:]:
                    coincidence += 1
                else:
                    break
            # print(f"{coincidence=}")
            if coincidence > len_ans:
                ans, len_ans = word, coincidence

            if not ans:
                match = SequenceMatcher(None, word, word_query).find_longest_match(0, len(word), 0, len_word_query)

                # print(f"{match=}; {match.size=}")  # -> Match(a=0, b=15, size=9)
                # print(word[match.a:match.a + match.size])  # -> apple pie
                # print(word_query[match.b:match.b + match.size])  # -> apple pie

                # print(match, word, word_query)
                if match.size > len_ans_add:
                    ans_add, len_ans_add = word, match.size

    if ans:
        return ans
    elif ans_add:
        return ans_add
    else:
        return "None"


def read_data_file(file_path: str) -> str:
    answer_string = ""
    with open(file=file_path, mode='r', encoding='utf-8') as file:
        count_data = int(file.readline())
        dictionary = []
        while count_data:
            word = file.readline().strip()
            dictionary.append(word)
            count_data -= 1
        count_query = int(file.readline())
        dictionary.sort(key=lambda x: len(x))
        # print(f"{dictionary=}")
        while count_query:
            answer_string += get_ans_file(file, dictionary) + "\n"
            count_query -= 1
    return answer_string


def get_ans(dictionary: list) -> str:
    word_query = input()
    len_word_query = len(word_query)
    ans, len_ans = "", 0
    ans_add, len_ans_add = "", 0
    for pos, word in enumerate(dictionary):
        if len_ans == len_word_query:
            return ans
        if word != word_query:
            coincidence = 0
            # print(f"{word_query=}; {word=}")
            for i in range(1, len(word) + 1):
                # print(f"Eq: {word[-i:]} == {word_query[-i:]} -> {word[-i:] == word_query[-i:]}")
                if word[-i:] == word_query[-i:]:
                    coincidence += 1
                else:
                    break
            # print(f"{coincidence=}")
            if coincidence > len_ans:
                ans, len_ans = word, coincidence

            if not ans:
                match = SequenceMatcher(None, word, word_query).find_longest_match(0, len(word), 0, len_word_query)
                # print(f"{match=}; {match.size=}")  # -> Match(a=0, b=15, size=9)
                # print(word[match.a:match.a + match.size])  # -> apple pie
                # print(word_query[match.b:match.b + match.size])  # -> apple pie
                if match.size > len_ans_add:
                    ans_add, len_ans_add = word, match.size

    if ans:
        return ans
    elif ans_add:
        return ans_add


def main() -> None:
    count_data = int(input())
    dictionary = []
    while count_data:
        word = input()
        dictionary.append(word)
        count_data -= 1
    count_query = int(input())
    dictionary.sort(key=lambda x: len(x))
    # print(f"{dictionary=}")
    while count_query:
        print(get_ans(dictionary))
        count_query -= 1


if __name__ == '__main__':
    main()
