if __name__ == '__main__':
    need_money = int(input())
    salary = int(input())
    wastes = int(input())
    # money_month = salary - wastes
    count_month = need_money // salary
    count_month += salary // (salary - wastes)
    count_month += 2
    print(count_month)


