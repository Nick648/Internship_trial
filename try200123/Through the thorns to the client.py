# https://contest.yandex.ru/contest/39459/problems/B/

def get_time(d1: int, h1: int, m1: int, d2: int, h2: int, m2: int) -> int:
    if d1 == d2:
        if h1 == h2:
            if m2 >= m1:
                return m2 - m1
            else:
                return -1
        elif h2 > h1:
            hm21 = (h2 - h1) * 60
            return hm21 + (m2 - m1)
        else:
            return -1
    elif d2 > d1:
        dm21 = (d2 - d1) * 24 * 60
        hm21 = (h2 - h1) * 60
        return dm21 + hm21 + (m2 - m1)
    else:
        return -1


def get_time_rocket(list_logs: list) -> str:
    # print(f"\t--- {cur_id=} ->  {list_logs}")
    status_rocket = "S"
    cur_data_rocket = list()
    next_data_rocket = list()
    total_minute = 0
    while list_logs:
        for log_str in list_logs:
            if status_rocket == "S" or status_rocket == "C":  # New status -> A
                if log_str[4] == "A":
                    cur_data_rocket = log_str
                    next_data_rocket = list()
                    status_rocket = "A"
                    list_logs.remove(log_str)
                    break
            elif status_rocket == "A":  # New status -> B/C
                if log_str[4] == "B" or log_str[4] == "C":
                    if next_data_rocket:
                        t1 = get_time(cur_data_rocket[0], cur_data_rocket[1], cur_data_rocket[2],
                                      next_data_rocket[0], next_data_rocket[1], next_data_rocket[2])
                        t2 = get_time(cur_data_rocket[0], cur_data_rocket[1], cur_data_rocket[2],
                                      log_str[0], log_str[1], log_str[2])
                        if t1 > t2 > 0:
                            next_data_rocket = log_str
                    else:
                        t = get_time(cur_data_rocket[0], cur_data_rocket[1], cur_data_rocket[2],
                                     log_str[0], log_str[1], log_str[2])
                        if t > 0:
                            next_data_rocket = log_str
            elif status_rocket == "B":  # New status -> C/S
                if log_str[4] == "C" or log_str[4] == "S":
                    if next_data_rocket:
                        t1 = get_time(cur_data_rocket[0], cur_data_rocket[1], cur_data_rocket[2],
                                      next_data_rocket[0], next_data_rocket[1], next_data_rocket[2])
                        t2 = get_time(cur_data_rocket[0], cur_data_rocket[1], cur_data_rocket[2],
                                      log_str[0], log_str[1], log_str[2])
                        if t1 > t2 > 0:
                            next_data_rocket = log_str
                    else:
                        t = get_time(cur_data_rocket[0], cur_data_rocket[1], cur_data_rocket[2],
                                     log_str[0], log_str[1], log_str[2])
                        if t > 0:
                            next_data_rocket = log_str
        if status_rocket == "A" or status_rocket == "B":
            if next_data_rocket:
                t = get_time(cur_data_rocket[0], cur_data_rocket[1], cur_data_rocket[2],
                             next_data_rocket[0], next_data_rocket[1], next_data_rocket[2])
                total_minute += t
                cur_data_rocket = next_data_rocket
                status_rocket = next_data_rocket[4]
                list_logs.remove(next_data_rocket)
                next_data_rocket = list()
    return str(total_minute)


if __name__ == '__main__':
    answer_string = ""
    id_logs = dict()
    count = int(input())
    for _ in range(count):
        log = input().split()
        log1 = list()
        for i in range(len(log) - 1):
            log1.append(int(log[i]))
        log1.append(log[-1])
        log = log1
        key = log[3]
        if key not in id_logs:
            new_list = [log]
            id_logs[key] = new_list
        else:
            mas = id_logs[key]
            mas.append(log)
            id_logs[key] = mas

    for id_r in sorted(id_logs):
        # print(f"{id_r} -> {id_logs[id_r]}")
        answer_string += get_time_rocket(id_logs[id_r]) + ' '
    print(answer_string)

''' INPUT ->
8
50 7 25 3632 A
14 23 52 212372 S
15 0 5 3632 C
14 21 30 212372 A
50 7 26 3632 C
14 21 30 3632 A
14 21 40 212372 B
14 23 52 3632 B

OUTPUT: 156 142
'''
