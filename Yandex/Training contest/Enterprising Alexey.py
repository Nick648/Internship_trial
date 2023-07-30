tasks = {}
workers = {}
ans_tasks = {}


def read_input() -> list[str]:
    with open(file='input.txt') as file:
        input_data = file.readlines()
    return input_data


def write_output(answer_dict: dict) -> None:
    with open(file='output.txt', mode='w') as file:
        for key, value in answer_dict.items():
            file.write(f'{key} {value}\n')


if __name__ == '__main__':
    data = read_input()
    for line in data:
        items = line.split()
        if len(items) == 2:
            tasks[items[0]] = int(items[1])
        elif len(items) == 3:
            worker = items[0]
            task = items[1]
            answer = int(items[2])
            if task in tasks:
                if answer == tasks[task]:
                    worker_ans = 1
                else:
                    worker_ans = 0
                if worker in workers:
                    workers[worker] += worker_ans
                else:
                    workers[worker] = worker_ans
            else:
                if worker in workers:
                    if workers[worker] / len(tasks) < 0.6:
                        continue
                if task in ans_tasks:
                    if answer in ans_tasks[task]:
                        ans_tasks[task][answer] += 1
                    else:
                        ans_tasks[task][answer] = 1
                else:
                    ans_tasks[task] = {answer: 1}

    for answer in ans_tasks:
        end_ans = None
        max_count = max(ans_tasks[answer].values())
        for key_ans, val_ans in ans_tasks[answer].items():
            if end_ans and val_ans == max_count:
                if end_ans > key_ans:
                    end_ans = key_ans
            elif end_ans is None and val_ans == max_count:
                end_ans = key_ans
        ans_tasks[answer] = end_ans

    ans_tasks = dict(sorted(ans_tasks.items()))
    write_output(ans_tasks)
