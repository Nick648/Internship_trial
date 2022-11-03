from random import choice

# import time

probability_keys = []


def set_prob():
    global probability_keys
    for it in keys:
        count = len([item for item in keys if item == it])
        # x = float("{:.6f}".format(count / len(keys)))
        probability_keys.append(count / len(keys))  # x


def main():
    nums = []
    mat_expect = 0
    for _ in range(k):
        p_num = choice(keys)
        nums.append(p_num)
    # print(nums)
    for i in range(len(nums) - 1, 0, -1):
        if nums[i] == nums[i - 1]:
            del nums[i]
    # print(nums)
    for item in nums:
        # ind = keys.index(item)
        # p = probability_keys[ind]
        # print(f'\t{item}: {ind}: {p}')
        mat_expect += item * probability_keys[keys.index(item)]
        # print(f'mat_expect: {mat_expect}')
    return mat_expect


if __name__ == '__main__':
    # start = time.time()
    mat_expect = 0
    keys = list(map(int, input().split()))
    k = int(input())
    set_prob()
    for item in keys:
        mat_expect += item * probability_keys[keys.index(item)]
    print(f'mat_expect: {mat_expect}')
    print(main())

    # end = time.time()
    # print("Execution time of the program is:", end - start)
    # print(keys, k, probability_keys, sep='\n')
