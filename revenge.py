import utils


def process(input):
    number_of_cases = int(input[0][0])
    cases = [row for row in input[1:]]
    solution = [solve(case, cases[case])
                for case in range(0, number_of_cases)]
    return solution


def solve(case, situation):
    print("Solving: " + str(case))
    stack = [char for char in situation[0]]
    flag = True
    i = 0
    if stack.count('-') == 0:
        return "Case #"+str(case + 1)+": " + str(0)
    while flag:
        result = xray(stack)
        i += 1
        if result.count('-') == 0:
            flag = False
        stack = result
    return "Case #"+str(case + 1)+": " + str(i)


def xray(stack):
    revStack = list(reversed(stack))
    for pancake in range(0, len(stack)):
        if revStack[pancake] == '-':
            if revStack[len(stack) - 1] == '+':
                index = revStack.index('+', pancake)
                toFlip = revStack[index:]
                stayTheSame = revStack[:index]
            elif pancake == len(stack) - 2:
                if revStack[pancake + 1] == '-':
                    toFlip = revStack[pancake:]
                    stayTheSame = revStack[:pancake]
                else:
                    toFlip = revStack[pancake + 1:]
                    stayTheSame = revStack[:pancake+1]
            else:
                toFlip = revStack[pancake:]
                stayTheSame = revStack[:pancake]
            flipped = flip(toFlip)
            stayTheSame.extend(flipped)
            return list(reversed(stayTheSame))


def flip(arr):
    rev = list(reversed(arr))
    ans = []
    for index in range(0, len(rev)):
        if rev[index] == '-':
            ans.append('+')
        elif rev[index] == '+':
            ans.append('-')
    return ans


filename = utils.getFilename()
input = utils.read_input(filename)
output = process(input)
utils.print_output(filename, output)
