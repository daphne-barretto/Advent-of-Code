# @author Daphne Barretto
# 12/02/2019
# AoC-2019-02 Part 1

# import miscellaneous operating system interfaces
import os, csv, sys

# get filename input.txt assuming it is in the same folder as the script
filename = os.path.dirname(os.path.abspath(__file__)) + "/input.txt"
# open the file in read mode
file = open(filename, "r")

reader = csv.reader(file, delimiter = ',')
for line in reader:
    i = 0
    line[1] = 12
    line[2] = 2
    while i < len(line):
        num = int(line[i])
        if num == 1:
            line[int(line[i+3])] = int(line[int(line[i+1])]) + int(line[int(line[i+2])])
        elif num == 2:
            line[int(line[i+3])] = int(line[int(line[i+1])]) * int(line[int(line[i+2])])
        elif num == 99:
            print("Position 0 at halt: " + str(line[0])) # Answer: 6627023
            sys.exit()
        else:
            print("Error: " + str(num))
        i += 4