def main():
    count_country = int(input())
    salary_country = list(map(int, input().split()))
    higher_country = list(map(int, input().split()))
    parents_country = list(map(int, input().split()))
    count_classmates = int(input())
    salary_class = list(map(int, input().split()))
    higher_class = list(map(int, input().split()))
    parents_class = list(map(int, input().split()))
    ans = ""
    for sal_cl, hig_cl, par_cl in zip(salary_class, higher_class, parents_class):
        num_country = 1
        for sal_cn, hig_cn, par_cn in zip(salary_country, higher_country, parents_country):
            if sal_cl >= sal_cn and hig_cl >= hig_cn:
                ans += f"{num_country} "
                break
            elif par_cl == num_country and par_cn == 1:
                ans += f"{num_country} "
                break
            else:
                num_country += 1
        if num_country == count_country + 1:
            ans += "0 "
    print(ans)


if __name__ == '__main__':
    main()
