import argparse


# Read a given filename
def read_input(filename):
    with open(filename) as file:
        input = file.readlines()
        inputArr = [i.replace("\n", "").split() for i in input]
        return inputArr


# Output a file given a list of strings
# list = ["string", "string", ....]
def print_output(filename, list):
    outputname = filename.split('.')
    output_file = open(outputname[0]+'.out', 'w')
    for element in list:
        output_file.write(element)
        output_file.write('\n')
    output_file.close()
    print("Done.")


# Reads the filename of the input passed in the terminal
def getFilename():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="Input filename to parse")
    args = parser.parse_args()
    return args.filename
