import utils


def process(input):
    number_of_cases = get_number_of_cases(input[0])
    cases = input[1:]
    solution = [solve(case, cases[case]) for case in range(0, number_of_cases)]
    return solution


def solve(case, stalls_people):
    stalls, people = [int(element) for element in stalls_people]
    stalls_dict = buildModel(stalls)
    y = 0
    z = 0
    for person in range(0, people):
        ls_rs = computeLsRs(stalls_dict)
        decision = decide(ls_rs, stalls_dict)
        modifyModel(decision, stalls_dict)
        # print(stalls_dict)
        # print(ls_rs)
        # print(ls_rs[decision])
        if person == people - 1:
            y = max(ls_rs[decision])
            z = min(ls_rs[decision])
    return "Case #"+str(case + 1)+": " + str(y) + " " + str(z)


def get_number_of_cases(row):
    return int(row[0])


def buildModel(stalls):
    model = []
    for index in range(0, stalls):
        model.extend([{'index': index, 'state': 0}])
    return model


def modifyModel(index, stalls):
    toRemove = stalls[index]
    stalls.remove(toRemove)
    stalls.insert(index, {'index': index, 'state': 1})


def computeLsRs(stalls_dict):
    ls_rs = []
    for index in range(0, len(stalls_dict)):
        if stalls_dict[index]['state'] == 1:
            left_s = -100
            right_s = -100
        else:
            left_s = left(index, stalls_dict)
            right_s = right(index, stalls_dict)
        ls_rs.append([left_s, right_s])
    return ls_rs


def left(index, stalls_dict):
    left = index
    for i in range(index - 1, -1, -1):
        if stalls_dict[i]['state'] == 1:
            left = index - i - 1
            break
    return left


def right(index, stalls_dict):
    right = len(stalls_dict) - index - 1
    for i in range(index + 1, len(stalls_dict)):
        if stalls_dict[i]['state'] == 1:
            right = i - index - 1
            break
    return right


def decide(ls_rs, stalls_dict):
    # These are all by default ordered left to right
    mins = [min(pair) for pair in ls_rs]
    maximal = max(mins)
    decision = [elem for elem in ls_rs if min(elem) == maximal]
    if len(decision) > 1:
        maxes = max([max(elem) for elem in decision])
        narrow_decision = [
            elem for elem in decision if max(elem) == maxes]
        if len(narrow_decision) > 1:
            start = 0
            # THIS LOOP IS TOO EXPENSIVE!
            print(len(narrow_decision))
            for index in range(0, len(narrow_decision)):
                suggested = narrow_decision[index]
                temp_index = ls_rs.index(suggested)
                if stalls_dict[temp_index]['state'] == 0:
                    return ls_rs.index(suggested, start)
                elif stalls_dict[temp_index]['state'] == 1:
                    start = stalls_dict[temp_index]['index']
        elif len(narrow_decision) == 1:
            return ls_rs.index(narrow_decision[0])
    else:
        return ls_rs.index(decision[0])


filename = utils.getFilename()
input = utils.read_input(filename)
output = process(input)
utils.print_output(filename, output)
