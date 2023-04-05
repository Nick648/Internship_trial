def main() -> None:
    total_number = int(input())
    numbers = list(map(int, input().split()))
    sum_numbers = sum(numbers)
    sr_val = round(sum_numbers / total_number)
    # print(f'{sum_numbers/total_number=}; {sr_val=}')
    cost = 0
    for item in numbers:
        cost += (item - sr_val) ** 2
    print(cost)


if __name__ == '__main__':
    main()
