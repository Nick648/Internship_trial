def input_data() -> list:
    with open(file="input.txt", mode="r", encoding="utf-8") as file:
        text = file.read()
    return text.strip().split()


def output_data(text: str) -> None:
    with open(file="output.txt", mode="w", encoding="utf-8") as file:
        file.write(text)


def get_text_ans(histogram: dict) -> None:
    total_str = ""
    for line in range(max(histogram.values()) - 1, -1, -1):
        new_str = ""
        for index, key in enumerate(histogram):
            if histogram[key] != 0:
                histogram[key] -= 1
                new_str += '#'
            else:
                new_str += ' '
        total_str = f"{new_str}\n{total_str}"
    for key in histogram:
        total_str += chr(key)
    output_data(total_str)


def main():
    data = input_data()
    histogram = {}
    for word in data:
        for sym in word:
            key = ord(sym)
            if key in histogram:
                histogram[key] += 1
            else:
                histogram[key] = 1
    histogram = dict(sorted(histogram.items(), key=lambda x: x[0]))  # sort keys
    get_text_ans(histogram)


if __name__ == '__main__':
    main()
