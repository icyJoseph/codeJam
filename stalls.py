import utils
import math


def process(input):
    number_of_cases = get_number_of_cases(input[0])
    cases = input[1:]
    #solution = [solve(case, cases[case]) for case in range(0, number_of_cases)]
    solution = [opti_solve(case, cases[case])
                for case in range(0, number_of_cases)]
    print(solution)
    return solution


def solve(case, stalls_people):
    print("Case: " + str(case))
    stalls, people = [int(element) for element in stalls_people]
    if stalls == people:
        return "Case #"+str(case + 1)+": " + str(0) + " " + str(0)
    ls_rs, length = compute(stalls, people)
    if (people - 1) >= length:
        y, z = nodeCalculator(1)
    else:
        y, z = nodeCalculator(ls_rs[people-1])
    return "Case #"+str(case + 1)+": " + str(int(y)) + " " + str(int(z))


def opti_solve(case, stalls_people):
    print("Case: " + str(case))
    stalls, last_person = [int(element) for element in stalls_people]
    if stalls == last_person:
        return "Case #"+str(case + 1)+": " + str(0) + " " + str(0)
    base, level = previous_power_of_2(last_person)
    nodes = [stalls]
    print(level)
    for step in range(0, level):
        print(step)
        new_nodes, flag = optimized(nodes)
        nodes = new_nodes
        if flag:
            break
    if len(new_nodes) < last_person - base - 1:
        y = 0
        z = 0
    else:
        y = max(nodeCalculator(new_nodes[last_person-base - 1]))
        z = min(nodeCalculator(new_nodes[last_person-base - 1]))
    return "Case #"+str(case + 1)+": " + str(int(y)) + " " + str(int(z))


def get_number_of_cases(row):
    return int(row[0])


def previous_power_of_2(x):
    return (1, 0) if x == 0 else (int(2**(x).bit_length() / 2), x.bit_length() - 1)


def nodeCalculator(node):
    a, b = 0, 0
    if node % 2 == 0:
            # even
        a = node/2
        b = node/2 - 1
    elif node % 2 != 0:
        # odd
        a = int(node/2)
        b = a
    return max(a, b), min(a, b)


def compute(stalls, people):
    flag = True
    index = 0
    ls_rs = [stalls]
    while flag:
        N = ls_rs[index]
        if N == 2 or N == 3:
            # the rest are just ones
            flag = False
        if N % 2 == 0:
            # even
            a = N/2
            b = N/2 - 1
        elif N % 2 != 0:
            # odd
            a = int(N/2)
            b = a
        ls_rs.append(a)
        ls_rs.append(b)
        index += 1
        if index > people:
            flag = False
    sorted_nodes = sorted(ls_rs, key=None, reverse=True)
    return sorted_nodes, len(sorted_nodes)


def optimized(nodes):
    arr = []
    flag = False
    for index in range(0, len(nodes)):
        new_nodes = breaker(nodes[index])
        if new_nodes == [0, 0] or new_nodes == [1, 0] or new_nodes == [0, 1] or new_nodes == [2, 1] or new_nodes == [1, 2]:
            flag = True
        arr.extend(new_nodes)
    return arr, flag


def breaker(node):
    if node % 2 == 0:
        return int(node/2 - 1), int(node/2)
    else:
        return int(node/2), int(node/2)


filename = utils.getFilename()
input = utils.read_input(filename)
output = process(input)
utils.print_output(filename, output)
