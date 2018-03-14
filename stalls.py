import utils
import math


def process(input):
    number_of_cases = get_number_of_cases(input[0])
    cases = input[1:]
    solution = [solve(case, cases[case]) for case in range(0, number_of_cases)]
    return solution


def solve(case, stalls_people):
    print("Case: " + str(case))
    stalls, people = [int(element) for element in stalls_people]
    if stalls == people:
        return "Case #"+str(case + 1)+": " + str(0) + " " + str(0)
    ls_rs, length = compute(stalls)
    if (people - 1) > length:
        y, z = nodeCalculator(1)
    else:
        y, z = nodeCalculator(ls_rs[people-1])

    return "Case #"+str(case + 1)+": " + str(int(y)) + " " + str(int(z))


def get_number_of_cases(row):
    return int(row[0])


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


def compute(stalls):
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
    sorted_nodes = sorted(ls_rs, key=None, reverse=True)
    return sorted_nodes, len(sorted_nodes)


filename = utils.getFilename()
input = utils.read_input(filename)
output = process(input)
utils.print_output(filename, output)
