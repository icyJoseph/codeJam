import utils


def process(input):
    number_of_cases = int(input[0][0])
    sheeps = [row for row in input[1:]]
    solution = [solve(case, sheeps[case])
                for case in range(0, number_of_cases)]
    return solution


def solve(case, sheeps):
    N = int(sheeps[0])
    digits = set()
    i = 1
    while len(digits) < 10:
        M = N * i
        digitsArr = getDigits(M)
        for digit in digitsArr:
            digits.add(digit)
        i += 1
        if N == 0:
            return "Case #"+str(case + 1)+": INSOMNIA"
    return "Case #"+str(case + 1)+": " + str(M)


def getDigits(N):
    Ns = [int(d) for d in str(N)]
    return Ns


filename = utils.getFilename()
input = utils.read_input(filename)
output = process(input)
utils.print_output(filename, output)
