def read_data_file(file_path: str) -> str:
    with open(file=file_path, mode='r', encoding='utf-8') as file:
        count_cpu, count_task = map(int, file.readline().split())
        cpu = {}
        energy_spent = 0
        energy_use = file.readline().split()
        for pos in range(count_cpu):
            cpu[int(energy_use[pos])] = 0
        cpu = dict(sorted(cpu.items(), key=lambda x: x[0]))  # sort keys
        while count_task:
            start_task, duration_task = map(int, file.readline().split())
            energy_spent += scheduler(cpu, start_task, duration_task)
            count_task -= 1
        return str(energy_spent) + "\n"


def scheduler(cpu: dict, start_task: int, duration_task: int) -> int:
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
