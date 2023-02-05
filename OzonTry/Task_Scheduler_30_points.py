from time import perf_counter


# def filtered_items():
#     filtered_cpu = list(filter(lambda x: cpu[x] <= start_task, cpu))
#     if filtered_cpu:
#         energy_spent += filtered_cpu[0] * duration_task
#         cpu[filtered_cpu[0]] = start_task + duration_task


def read_data_file(file_path: str) -> str:
    with open(file=file_path, mode='r', encoding='utf-8') as file:
        count_cpu, count_task = map(int, file.readline().split())
        cpu = {}
        energy_spent = 0
        energy_use = file.readline().split()
        for pos in range(count_cpu):
            cpu[int(energy_use[pos])] = 0

        # time_begin = perf_counter()
        cpu = dict(sorted(cpu.items(), key=lambda x: x[0]))  # sort keys
        min_value = {'min_value': 0}
        # time_end = perf_counter()
        # total_time = round(time_end - time_begin, 5)
        # print(f"\tTime sort spent = {total_time} s")
        while count_task:
            start_task, duration_task = map(int, file.readline().split())

            # filtered_cpu = list(filter(lambda x: cpu[x] <= start_task, cpu.keys()))
            # if filtered_cpu:
            #     energy_spent += filtered_cpu[0] * duration_task
            #     cpu[filtered_cpu[0]] = start_task + duration_task

            # print(f"{start_task=} -> {filtered_cpu=}")
            # energy_spent += scheduler(cpu, start_task, duration_task)

            energy_spent += scheduler_1(cpu, min_value, start_task, duration_task)
            count_task -= 1
        return str(energy_spent) + "\n"


def scheduler_1(cpu: dict, min_value: dict, start_task: int, duration_task: int) -> int:
    if min_value['min_value'] > start_task:
        return 0
    for key, value in cpu.items():  # key = number cpu(energy), value = ent time task
        if value <= start_task:
            if start_task + duration_task < min_value['min_value']:
                min_value['min_value'] = start_task + duration_task
            cpu[key] = start_task + duration_task
            return key * duration_task
    return 0


def scheduler(cpu: dict, start_task: int, duration_task: int) -> int:
    if min(cpu.values()) > start_task:
        return 0
    for key, value in cpu.items():  # key = number cpu(energy), value = ent time task
        if value <= start_task:
            cpu[key] = start_task + duration_task
            return key * duration_task
    return 0


def main() -> None:
    count_cpu, count_task = map(int, input().split())
    cpu = {}
    energy_spent = 0
    energy_use = input().split()
    for pos in range(count_cpu):
        cpu[int(energy_use[pos])] = 0
    cpu = dict(sorted(cpu.items(), key=lambda x: x[0]))  # sort keys
    while count_task:
        start_task, duration_task = map(int, input().split())
        energy_spent += scheduler(cpu, start_task, duration_task)
        count_task -= 1
    print(energy_spent)


if __name__ == '__main__':
    main()
