import utils


def process(input):
    number_of_cases = int(input[0][0])
    pancakes_flipper = [interpreter(row) for row in input[1:]]
    solution = [solve(case, pancakes_flipper[case])
                for case in range(0, number_of_cases)]
    return solution


def interpreter(row):
    pancakes = row[0]
    flipper = row[1]
    return pancakes, int(flipper)


def solve(case, pancakes_flipper):
    pancakesStr, flipper = pancakes_flipper
    pancakes = [char for char in pancakesStr]
    steps = 0
    for index in range(0, len(pancakes) - flipper + 1):
        if pancakes[index] == "-":
            flip(pancakes, index, flipper)
            steps += 1
    return "Case #"+str(case + 1)+": " + possible(pancakes, flipper, steps)


def flip(pancakes, index, flipper):
    for pos in range(index, index + flipper):
        if pancakes[pos] == "+":
            pancakes[pos] = "-"
        elif pancakes[pos] == "-":
            pancakes[pos] = "+"
    return pancakes


def possible(pancakes, flipper, steps):
    if pancakes.count("-") == 0:
        return str(steps)
    else:
        return "IMPOSSIBLE"


filename = utils.getFilename()
input = utils.read_input(filename)
output = process(input)
utils.print_output(filename, output)
