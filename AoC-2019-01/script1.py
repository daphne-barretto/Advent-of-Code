# @author Daphne Barretto
# 12/01/2019
# AoC-2019-01 Part 1

# import miscellaneous operating system interfaces
import os

# get filename input.txt assuming it is in the same folder as the script
filename = os.path.dirname(os.path.abspath(__file__)) + "/input.txt"
# open the file in read mode
file = open(filename, "r")

fuel = 0
for mass in file:
    fuel += int(int(mass) / 3) - 2

print("Total fuel requirement: " + str(fuel))
# Answer: 3452245