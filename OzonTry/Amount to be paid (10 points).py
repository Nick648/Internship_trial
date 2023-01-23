if __name__ == '__main__':
    count_prod = int(input())
    for _ in range(count_prod):
        products = dict()
        sum_price = 0
        count_price = int(input())
        prices = input().split()
        for price in prices:
            if price in products:
                products[price] += 1
            else:
                products[price] = 1
        for item in products:
            sum_price += ((products[item] - products[item] // 3) * int(item))
        print(sum_price)

''' INPUT ->
6
12
2 2 2 2 2 2 2 3 3 3 3 3
12
2 3 2 3 2 2 3 2 3 2 2 3
1
10000
9
1 2 3 1 2 3 1 2 3
6
10000 10000 10000 10000 10000 10000
6
300 100 200 300 200 300

OUTPUT ->
22
22
10000
12
40000
1100

'''
