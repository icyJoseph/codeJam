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
    y = 0
    z = 0
    ls_rs = [stalls]
    for person in range(0, people):
        response, new_ls_rs = compute(ls_rs)
        ls_rs = new_ls_rs
        if person == people - 1:
            y = max(response)
            z = min(response)
    return "Case #"+str(case + 1)+": " + str(y) + " " + str(z)


def get_number_of_cases(row):
    return int(row[0])


def compute(ls_rs):
    max_segment = max(ls_rs)
    ls_rs.remove(max_segment)
    a, b = 0, 0
    if max_segment == 1:
        ls_rs.append(a)
        ls_rs.append(b)
        return [a, b], ls_rs
    if max_segment % 2 == 0:
        # even procedure
        a = int(max_segment / 2) - 1
        b = int(max_segment / 2)
    else:
        a = int(math.floor((max_segment) / 2))
        b = a
    ls_rs.append(a)
    ls_rs.append(b)
    return [a, b], ls_rs


filename = utils.getFilename()
input = utils.read_input(filename)
output = process(input)
utils.print_output(filename, output)
