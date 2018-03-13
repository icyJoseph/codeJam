import utils


def process(input):
    number_of_cases = int(input[0][0])
    untidy_numbers = [row for row in input[1:]]
    solution = [solve(case, untidy_numbers[case])
                for case in range(0, number_of_cases)]
    return solution


def solve(case, num):
    digits = numberArr(num[0])
    result = makeNumber(digits)
    while not isTidy(result):
        for index in range(0, len(digits) - 1):
            if digits[index] > digits[index + 1]:
                digits[index] = digits[index] - 1
                for change in range(index+1, len(digits)):
                    digits[change] = 9
        result = makeNumber(digits)
    if not validateAnswer(num[0], result):
        print("Invalid")
    return "Case #"+str(case + 1)+": " + str(result)


def numberArr(number):
    return [int(c) for c in str(number)]


def isTidy(number):
    digits = numberArr(number)
    flag = True
    for index in range(0, len(digits) - 1):
        if digits[index] > digits[index+1]:
            flag = False
    return flag


def validateAnswer(untidy, tidy):
    return int(untidy) >= int(tidy)


def makeNumber(number):
    decomposed = 0
    for index in range(0, len(number)):
        power = len(number) - index
        decomposed += number[index] * pow(10, power - 1)
    return decomposed


filename = utils.getFilename()
input = utils.read_input(filename)
output = process(input)
utils.print_output(filename, output)
