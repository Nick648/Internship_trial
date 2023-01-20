# https://contest.yandex.ru/contest/39459/problems/E/

def add_potion_to_book(count_potion: str, potion: list) -> None:
    recipe = dict()
    for piece in potion:
        key = str(piece)
        if piece == 1:
            if "1" in recipe:
                recipe["1"] += 1
            else:
                recipe["1"] = 1
        elif piece == 2:
            if "2" in recipe:
                recipe["2"] += 1
            else:
                recipe["2"] = 1
        elif key in recipe_book:
            for item in recipe_book[key]:
                if item in recipe:
                    recipe[item] += recipe_book[key][item]
                else:
                    recipe[item] = recipe_book[key][item]
        else:
            if piece in recipe:
                recipe[key] += 1
            else:
                recipe[key] = 1
    recipe_book[count_potion] = recipe


def get_answer(x: int, y: int, s: str) -> str:
    if s in recipe_book:
        if 1 <= len(recipe_book[s]) <= 2:
            recipe = recipe_book[s]
            if x > 0:
                if ["1"] in recipe and recipe["1"] >= x:
                    return "1"
                else:
                    return "0"
            if y > 0:
                if ["2"] in recipe and recipe["2"] >= y:
                    return "1"
                else:
                    return "0"
    return "0"


if __name__ == '__main__':
    answer_string = ""
    recipe_book = dict()
    data_base = list()
    count = int(input())
    for count_potion in range(3, count + 1):
        potion = list(map(str, input().split()))[1:]
        add_potion_to_book(str(count_potion), potion)
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
