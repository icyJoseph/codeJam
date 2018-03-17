import utils
import math


def process(input):
    number_of_cases = get_number_of_cases(input[0])
    cases = input[1:]
    optimal = [opti_solve(case, cases[case])
               for case in range(0, number_of_cases)]
    return optimal


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


def opti_solve(case, stalls_people):
    print("Case: " + str(case))
    stalls, last_person = [int(element) for element in stalls_people]
    # PYTHON SETS TO THE RESCUE!
    N = {stalls}
    atoms = {stalls: 1}
    flag = True
    coverage = 0
    while flag:
        M = max(N)
        if M % 2 == 0:
            b = math.floor((M - 1) // 2)
            a = b + 1
        else:
            b = math.floor((M-1) // 2)
            a = b
        coverage += atoms[M]
        if coverage >= last_person:
            flag = False
            return "Case #"+str(case + 1)+": " + str(int(a)) + " " + str(int(b))
        else:
            N.remove(M)
            N.add(a)
            N.add(b)
            atoms = progression(atoms, a, b, atoms[M])


def progression(atoms, a, b, c):
    if a in atoms:
        curr = atoms[a]
        atoms[a] = curr + c
    elif a not in atoms:
        atoms[a] = c
    if b in atoms:
        curr = atoms[b]
        atoms[b] = curr + c
    elif b not in atoms:
        atoms[b] = c
    return atoms


filename = utils.getFilename()
input = utils.read_input(filename)
output = process(input)
utils.print_output(filename, output)
