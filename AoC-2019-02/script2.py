# @author Daphne Barretto
# 12/02/2019
# AoC-2019-02 Part 2

# import miscellaneous operating system interfaces
import os, csv, sys

# get filename input.txt assuming it is in the same folder as the script
filename = os.path.dirname(os.path.abspath(__file__)) + "/input.txt"
# open the file in read mode
file = open(filename, "r")

def program(line, noun, verb):
    i = 0
    line[1] = noun
    line[2] = verb
    while i < len(line):
        num = int(line[i])
        if num == 1:
            line[int(line[i+3])] = int(line[int(line[i+1])]) + int(line[int(line[i+2])])
        elif num == 2:
            line[int(line[i+3])] = int(line[int(line[i+1])]) * int(line[int(line[i+2])])
        elif num == 99:
            return line[0] 
        else:
            print("Error: " + str(num))
        i += 4

goal = 19690720

reader = csv.reader(file, delimiter = ',')
for line in reader:
    noun = 0
    while noun < 100:
        verb = 0
        while verb < 100:
            if program(line.copy(), noun, verb) == goal:
                print("100 * noun + verb: " + str(100 * noun + verb))   # Answer: 4019
            verb += 1
        noun += 1