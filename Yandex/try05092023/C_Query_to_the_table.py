if __name__ == '__main__':
    count_line, count_column, count_query = map(int, input().split())
    name_columns = list(map(str, input().split()))
    table = []
    for i in range(count_line):
        table.append(list(map(int, input().split())))
    for q in range(count_query):
        column_name, sign, val = map(str, input().split())
        val = int(val)
        index_name = name_columns.index(column_name)
        if sign == '>':
            table = list(filter(lambda element: element[index_name] > val, table))
            # any(item in main_list for item in main_list if item == 22)
        else:
            table = list(filter(lambda element: element[index_name] < val, table))
        if not table:
            break
    # answer = sum(map(sum, table))
    print(sum(map(sum, table)))
