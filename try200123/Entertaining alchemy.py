# https://contest.yandex.ru/contest/39459/problems/E/

def add_potion_to_book(count_potion: str, potion: list) -> None:
    recipe = dict()
    for piece in potion:
        if piece == "1":
            if "A" in recipe:
                recipe["A"] += 1
            else:
                recipe["A"] = 1
        elif piece == "2":
            if "B" in recipe:
                recipe["B"] += 1
            else:
                recipe["B"] = 1
        elif piece in recipe_book:
            for item in recipe_book[piece]:
                if item in recipe:
                    recipe[item] += recipe_book[piece][item]
                else:
                    recipe[item] = recipe_book[piece][item]
        else:
            if piece in recipe:
                recipe[piece] += 1
            else:
                recipe[piece] = 1
    recipe_book[count_potion] = recipe


def get_answer(x: int, y: int, s: str) -> str:
    if s in recipe_book:
        if 1 <= len(recipe_book[s]) <= 2:
            recipe = recipe_book[s]
            count_x, count_y = 0, 0
            if "A" in recipe:
                count_x = recipe["A"]
            if "B" in recipe:
                count_y = recipe["B"]
            # print(f"{recipe=};{count_x=};{count_y=};{x=};{y=}")
            if x >= count_x and y >= count_y:
                if count_y == 0 and count_x == 0:
                    return "0"
                return "1"
    return "0"


if __name__ == '__main__':
    answer_string = ""
    recipe_book = dict()
    data_base = list()
    count = int(input())
    for count_potion in range(3, count + 1):
        potion = list(map(str, input().split()))[1:]
        add_potion_to_book(str(count_potion), potion)
    # print(f"{recipe_book=}")
    query_count = int(input())
    for _ in range(query_count):
        x, y, s = map(int, input().split())
        answer_string += get_answer(x, y, str(s))
    print(answer_string)

''' INPUT ->
7
3 1 1 2
2 1 3
3 4 3 4
1 7
1 6
3
8 4 5
9 2 5
10 10 6

OUTPUT: 100
'''
