if __name__ == '__main__':
    price_tariff, size_mb_tariff, cost_mb, spent_mb = map(int, input().split())
    if (spent_mb - size_mb_tariff) > 0:
        print(price_tariff + (spent_mb - size_mb_tariff) * cost_mb)
    else:
        print(price_tariff)
