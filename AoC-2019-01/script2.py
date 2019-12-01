# @author Daphne Barretto
# 12/01/2019
# AoC-2019-01 Part 2

def calcFuel(mass):
    fuel = int(int(mass) / 3) - 2
    if fuel <= 0:
        return 0;
    return fuel + calcFuel(fuel)

# import miscellaneous operating system interfaces
import os

# get filename input.txt assuming it is in the same folder as the script
filename = os.path.dirname(os.path.abspath(__file__)) + "/input.txt"
# open the file in read mode
file = open(filename, "r")

fuel = 0
for mass in file:
    fuel += calcFuel(mass)

print("Total fuel requirement: " + str(fuel))
# Answer: 3452245