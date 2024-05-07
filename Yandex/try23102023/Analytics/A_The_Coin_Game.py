def main():
    probability = 1
    for i in range(1, 26):
        probability *= (0.9 ** i)
        print(f'Drop: {i=}; {probability=}')
    probability = probability ** 15
    print(probability, "{:.10f}".format(probability))
    print(1-probability, "{:.10f}".format(1-probability))


if __name__ == '__main__':
    main()
