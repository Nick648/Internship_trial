import json


def write_data_json(dump_dict: dict) -> None:
    """ Writes the dictionary to a json file """
    with open(file="data.json", mode="w", encoding="utf-8") as write_file:
        json.dump(dump_dict, write_file, ensure_ascii=False, indent=4)


def read_json_file() -> dict:
    def update_type_keys(dict_in: dict, type_key: type) -> dict:
        cash_dict = {}
        for key, val in dict_in.items():
            key = type_key(key)
            if isinstance(val, dict):
                cash_dict[key] = update_type_keys(val, type_key)
            else:
                cash_dict[key] = val
        return cash_dict

    with open("data.json", "r", encoding="utf-8") as read_file:
        d = json.load(read_file)
    return d


def main():
    d = {}
    summa = 0
    for i in range(1, 101):
        dd = {
            'An': [i, i + 1],
            'p': [i * 0.5, (i + 1) * 0.5]
        }
        d[i] = dd
        summa += i * 0.5 + (i + 1) * 0.5
    write_data_json(d)
    print(summa)


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a + b)
    main()
