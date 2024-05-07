def radix_sort(arr: list[int]) -> list[int]:
    max_bit_depth = get_max_bit_depth(arr)
    for bit_depth in range(max_bit_depth):
        bucket = {b: [] for b in range(10)}
        for dig in arr:
            bucket[(dig // (10 ** bit_depth) % 10)].append(dig)
        output_bucket(bucket=bucket, phase=bit_depth + 1, max_bit_depth=max_bit_depth)
        arr.clear()
        for key, list_item in bucket.items():
            for item in list_item:
                arr.append(item)
    return arr


def get_max_bit_depth(source_array: list[int]) -> int:
    max_num = max(source_array)
    max_bit_depth = len(str(max_num))
    return max_bit_depth


def output_bucket(bucket: dict, phase: int, max_bit_depth: int) -> None:
    print(f"Phase {phase}")
    for key, list_item in bucket.items():
        if list_item:
            arr_for_output = [str(i).rjust(max_bit_depth, '0') for i in list_item]
            print(f"Bucket {key}: {', '.join(arr_for_output)}")
        else:
            print(f"Bucket {key}: empty")
    print("*" * 10)


def output_arr(arr: list[int], mes: str = "") -> None:
    if mes:
        print(mes)
    max_bit_depth = get_max_bit_depth(arr)
    arr_for_output = [str(i).rjust(max_bit_depth, '0') for i in arr]
    print(", ".join(arr_for_output))


def main() -> None:
    count_item = int(input())
    start_arr = []
    for _ in range(count_item):
        start_arr.append(int(input()))
    output_arr(start_arr, "Initial array:")
    print("*" * 10)
    sort_arr = radix_sort(start_arr)
    output_arr(sort_arr, "Sorted array:")


if __name__ == '__main__':
    main()

'''
9
12
32
45
67
98
29
61
35
09

Initial array:
12, 32, 45, 67, 98, 29, 61, 35, 09
**********
Phase 1
Bucket 0: empty
Bucket 1: 61
Bucket 2: 12, 32
Bucket 3: empty
Bucket 4: empty
Bucket 5: 45, 35
Bucket 6: empty
Bucket 7: 67
Bucket 8: 98
Bucket 9: 29, 09
**********
Phase 2
Bucket 0: 09
Bucket 1: 12
Bucket 2: 29
Bucket 3: 32, 35
Bucket 4: 45
Bucket 5: empty
Bucket 6: 61, 67
Bucket 7: empty
Bucket 8: empty
Bucket 9: 98
**********
Sorted array:
09, 12, 29, 32, 35, 45, 61, 67, 98

'''
