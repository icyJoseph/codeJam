import utils


def process(input):
    number_of_cases = int(input[0][0])
    control = 0
    solution = []
    cases = input[1:]
    for case in range(1, number_of_cases + 1):
        destination, number_of_horses = [int(elem) for elem in cases[control]]
        control += 1
        horses = cases[control:number_of_horses+control]
        case_solution = solve(case, destination, number_of_horses, horses)
        control += number_of_horses
        solution.append(case_solution)
    return solution


def solve(case, destination, number_of_horses, horses):
    speed = 0
    if len(horses) != number_of_horses:
        print('PROBLEM')
    horses = [[int(horse[0]), int(horse[1])] for horse in horses]
    # Initial state orders the horses according to their initial point
    initial_state = sorted(horses, key=lambda k: k[0])
    bottle_neck = 0
    top_speed = initial_state[0][1]
    for index in range(0, number_of_horses):
        curr = initial_state[index][1]
        if initial_state[index][1] < top_speed:
            top_speed = curr
            if cross_before_destination(initial_state[bottle_neck], initial_state[index], destination):
                bottle_neck = index
    time = get_time(initial_state[bottle_neck], destination)
    speed = get_speed(time, destination)
    print(speed)
    return "Case #"+str(case)+": " + str(speed)


def get_time(horse, destination):
    init, speed = horse
    time = (destination - init) / speed
    return time


def get_speed(time, destination):
    return destination / time


def cross_before_destination(horse_a, horse_b, destination):
    init_a, speed_a = horse_a
    init_b, speed_b = horse_b
    return (init_b * speed_a - init_a * speed_b) / (speed_a - speed_b) < destination


filename = utils.getFilename()
input = utils.read_input(filename)
output = process(input)
utils.print_output(filename, output)
