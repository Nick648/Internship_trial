from os import path, listdir
from time import time, sleep
from colorama import Fore, Style, init
from Task_Scheduler_30_points import read_data_file as test_func
import threading

# import pyperclip


init(autoreset=True)

# Constants module colorama
RED = Fore.LIGHTRED_EX
GREEN = Fore.LIGHTGREEN_EX
YELLOW = Fore.LIGHTYELLOW_EX
CYAN = Fore.LIGHTCYAN_EX
RESET = Style.RESET_ALL

# Constants for path
DOWNLOADS_DIR = path.expanduser('~') + r'\Downloads'
dir_name = 'tests/tests'
TESTS_PATH = path.join(DOWNLOADS_DIR, dir_name)

# Constant for time control (in seconds) *for thread
TIME_TEST_LIMIT = 10
flag_stop = False


def error_out(s: str) -> None:  # Вывод красного текста
    print(RED + s, sep='')


def done_out(s: str) -> None:  # Вывод зелёного текста
    print(GREEN + s, sep='')


def yellow_out(s: str) -> None:  # Вывод жёлтого текста
    print(YELLOW + s, sep='')


# Thread counter for check time limit
def time_counter_control() -> None:  # Add exit code here!
    global flag_stop
    # print(CYAN + f'Запуск потока {threading.currentThread()} name: {threading.currentThread().getName()}' + RESET)
    for _ in range(TIME_TEST_LIMIT):
        if flag_stop:
            flag_stop = False
            return
        sleep(1)
    print(RED + f"RuntimeError: Time limit exceeded: {TIME_TEST_LIMIT} s\n" + RESET)
    # print(CYAN + f'\tПоток {threading.currentThread()} выполнился.' + RESET)


def generator_files_tests_str() -> str:
    for file in listdir(TESTS_PATH):
        if file[-2:] != '.a':
            file_path = path.join(TESTS_PATH, file)
            with open(file=file_path, mode='r', encoding='utf-8') as f:
                print(file_path)
                yield f.read()


def generator_files_answers_str() -> str:
    for file in listdir(TESTS_PATH):
        if file[-2:] == '.a':
            file_path = path.join(TESTS_PATH, file)
            with open(file=file_path, mode='r', encoding='utf-8') as f:
                print(file_path, type(f))
                yield f.read()


def generator_files_tests_name() -> str:
    for file in listdir(TESTS_PATH):
        if file[-2:] != '.a':
            file_path = path.join(TESTS_PATH, file)
            yield file_path


def generator_files_answers_name() -> str:
    for file in listdir(TESTS_PATH):
        if file[-2:] == '.a':
            file_path = path.join(TESTS_PATH, file)
            yield file_path


def generator_files_name() -> tuple:
    cur_file = ""
    for file in listdir(TESTS_PATH):
        # print(f"{file=}; {cur_file=}; {file[-2:]}; {file[:-1]}")
        if file[-2:] == '.a' and cur_file == file[:-2]:
            test_path = path.join(TESTS_PATH, cur_file)
            answer_path = path.join(TESTS_PATH, file)
            yield file[:-2], test_path, answer_path
        else:
            cur_file = file


# Question and get answer from user
def user_query(question="Output error details?") -> bool:
    y_ans = ['+', 'y', 'ye', 'yes', 'yeah']
    n_ans = ['-', 'n', 'no', 'non', 'none']
    while True:
        op = input(f'{question} (Y/N) \n>>> ' + RESET).strip().lower()
        if op in n_ans:
            return False
        elif op in y_ans:
            return True
        else:
            print(RED + 'Enter the appropriate answer: (Y/N)\n' + RESET)


def check_validate_tests():
    global flag_stop
    for name, test_name_file, answer_name_file in generator_files_name():
        # print(f"{name=}; {test_name_file}; {answer_name_file=}")
        log = f"Test {name}: "
        print(log, end='')
        thread = threading.Thread(target=time_counter_control, name='time_control', daemon=True)
        thread.start()
        # print(YELLOW + f"{threading.enumerate()=}" + RESET)
        begin_test_time = time()
        code_answer = test_func(test_name_file)  # Check test
        end_test_time = time()

        flag_stop = True
        thread.join()
        total_test_time = round(end_test_time - begin_test_time, 5)
        log = "Result -> "
        with open(file=answer_name_file, mode='r', encoding='utf-8') as file:
            correct_answer = file.read()
        if code_answer == correct_answer:
            log += GREEN + 'Right ' + RESET
        else:
            log += RED + 'Wrong ' + RESET
            print(log, '\n')
            if user_query():
                print(f"\tCode answer:\n{code_answer}\n\tCorrect answer:\n{correct_answer}")
                # pyperclip.copy(code_answer)
                code_answer = code_answer.split('\n')
                correct_answer = correct_answer.split('\n')
                for i in range(min(len(correct_answer), len(code_answer))):
                    if code_answer[i] != correct_answer[i]:
                        print(f"\n\tError in {i + 1} line  ->  {code_answer[i]=} != {correct_answer[i]=}")
                        break
            break
        log += f"/ Time spent = {total_test_time} s"
        print(log)


# запускаем тестирование
if __name__ == '__main__':
    start_message = YELLOW + " Autotest for code " + RESET
    print("\n", "{:*^75}".format(start_message), "\n", sep='')
    print(YELLOW + f"\tDon't forget to change the imported code file!" + RESET)
    print(f"Current Working Directory where tests: {TESTS_PATH}\n")
    if not path.exists(TESTS_PATH):
        print(RED + "There is no given folder on the current path. Change the path!" + RESET)
    else:
        check_validate_tests()
