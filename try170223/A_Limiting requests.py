def main():
    user_lim, serv_lim, duration = map(int, input().split())
    logs = {}
    time, user_id = map(int, input().split())
    logs[time] = [user_id]
    print(200)
    while True:
        t_list = input()
        if t_list == '-1':
            break

        time, user_id = map(int, t_list.split())
        count_user, count_service = 0, 0
        flag = False
        del_key = []
        for key in logs.keys():
            # print(f"\tcycle {logs=}")
            if time > duration and key < time - duration:
                del_key.append(key)
                continue
            else:
                count_user += logs[key].count(user_id)
                count_service += len(logs[key])
            if count_user >= user_lim:
                print(429)
                flag = True
                break
            elif count_service >= serv_lim:
                print(503)
                flag = True
                break
        for key in del_key:
            del logs[key]
        if flag:
            continue
        elif time in logs.keys():
            logs[time].append(user_id)
        else:
            logs[time] = [user_id]
        print(200)


if __name__ == '__main__':
    main()
