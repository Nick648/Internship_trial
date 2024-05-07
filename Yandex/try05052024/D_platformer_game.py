solvers = {'': (0, 1)}


def get_solver_string(cmd_s: str, i: int) -> tuple:
    pos = solvers[cmd_s[:i]][0]
    side = solvers[cmd_s[:i]][1]
    for i in range(i, len(cmd_s)):
        if cmd_s[i] == 'R':
            side = 1
        elif cmd_s[i] == 'L':
            side = -1
        elif cmd_s[i] == 'F':
            pos += side
    return pos, side


def solver_string(cmd_s: str) -> int:
    pos = 0
    side = 1
    for c in cmd_s:
        if c == 'R':
            side = 1
        elif c == 'L':
            side = -1
        elif c == 'F':
            pos += side
    return pos


def main():
    possible_pos = set()
    n = int(input())
    cmd_s = input()
    for i in range(n):
        if cmd_s[i] == 'R':
            possible_pos.add(solver_string(cmd_s[:i] + 'L' + cmd_s[i + 1::]))
            possible_pos.add(solver_string(cmd_s[:i] + 'F' + cmd_s[i + 1::]))
        elif cmd_s[i] == 'L':
            possible_pos.add(solver_string(cmd_s[:i] + 'R' + cmd_s[i + 1::]))
            possible_pos.add(solver_string(cmd_s[:i] + 'F' + cmd_s[i + 1::]))
        elif cmd_s[i] == 'F':
            possible_pos.add(solver_string(cmd_s[:i] + 'L' + cmd_s[i + 1::]))
            possible_pos.add(solver_string(cmd_s[:i] + 'R' + cmd_s[i + 1::]))
    print(len(possible_pos))


def main_2():
    global solvers
    possible_pos = set()
    n = int(input())
    cmd_s = input()
    for i in range(n):
        solvers[cmd_s[:i + 1]] = get_solver_string(cmd_s[:i + 1], i)
    final_pos, final_side = solvers[cmd_s][0], solvers[cmd_s][1]
    for i in range(n):
        pos, side = solvers[cmd_s[:i]][0], solvers[cmd_s[:i]][1]
        abs_dist = abs(final_pos - pos)
        side_cur = final_pos > pos
        if cmd_s[i] == 'R':
            if side == 1:
                possible_pos.add(final_pos + 1)  # F
                if side_cur:
                    possible_pos.add(pos - abs_dist)  # L
                else:
                    possible_pos.add(pos + abs_dist)  # L
            else:
                possible_pos.add(final_pos - 1)  # F
                if side_cur:
                    possible_pos.add(pos - abs_dist)  # L
                else:
                    possible_pos.add(pos + abs_dist)  # L
        elif cmd_s[i] == 'L':
            if side == 1:
                possible_pos.add(final_pos + 1)  # F
                if side_cur:
                    possible_pos.add(pos - abs_dist)  # L
                else:
                    possible_pos.add(pos + abs_dist)  # L
            else:
                possible_pos.add(final_pos - 1)  # F
                if side_cur:
                    possible_pos.add(pos - abs_dist)  # L
                else:
                    possible_pos.add(pos + abs_dist)  # L
        elif cmd_s[i] == 'F':
            possible_pos.add(solver_string(cmd_s[:i] + 'L' + cmd_s[i + 1::]))
            possible_pos.add(solver_string(cmd_s[:i] + 'R' + cmd_s[i + 1::]))


def main_3():
    possible_pos = set()
    n = int(input())
    cmd_s = input()
    for i in range(n):
        solvers[cmd_s[:i + 1]] = get_solver_string(cmd_s[:i + 1], i)
    for i in range(n):
        if cmd_s[i] == 'R':
            possible_pos.add(get_solver_string(cmd_s[:i] + 'L' + cmd_s[i + 1::], i)[0])
            possible_pos.add(get_solver_string(cmd_s[:i] + 'F' + cmd_s[i + 1::], i)[0])
        elif cmd_s[i] == 'L':
            possible_pos.add(get_solver_string(cmd_s[:i] + 'R' + cmd_s[i + 1::], i)[0])
            possible_pos.add(get_solver_string(cmd_s[:i] + 'F' + cmd_s[i + 1::], i)[0])
        elif cmd_s[i] == 'F':
            possible_pos.add(get_solver_string(cmd_s[:i] + 'L' + cmd_s[i + 1::], i)[0])
            possible_pos.add(get_solver_string(cmd_s[:i] + 'R' + cmd_s[i + 1::], i)[0])
    print(len(possible_pos))


if __name__ == '__main__':
    # main()
    # main_2()
    main_3()

"""
3
RLF

4

6
LRFFLR

6

3
FFF

3
"""
