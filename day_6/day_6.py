# --- Day 6: Lanternfish ---
# The sea floor is getting steeper. Maybe the sleigh keys got carried this way?
#
# A massive school of glowing lanternfish swims past. They must spawn quickly to reach such large numbers - maybe exponentially quickly? You should model their growth rate to be sure.
#
# Although you know nothing about this specific species of lanternfish, you make some guesses about their attributes. Surely, each lanternfish creates a new lanternfish once every 7 days.
#
# However, this process isn't necessarily synchronized between every lanternfish - one lanternfish might have 2 days left until it creates another lanternfish, while another might have 4. So, you can model each fish as a single number that represents the number of days until it creates a new lanternfish.
#
# Furthermore, you reason, a new lanternfish would surely need slightly longer before it's capable of producing more lanternfish: two more days for its first cycle.
#
# So, suppose you have a lanternfish with an internal timer value of 3:
#
# After one day, its internal timer would become 2.
# After another day, its internal timer would become 1.
# After another day, its internal timer would become 0.
# After another day, its internal timer would reset to 6, and it would create a new lanternfish with an internal timer of 8.
# After another day, the first lanternfish would have an internal timer of 5, and the second lanternfish would have an internal timer of 7.
# A lanternfish that creates a new fish resets its timer to 6, not 7 (because 0 is included as a valid timer value). The new lanternfish starts with an internal timer of 8 and does not start counting down until the next day.
#
# Realizing what you're trying to do, the submarine automatically produces a list of the ages of several hundred nearby lanternfish (your puzzle input). For example, suppose you were given the following list:
#
# 3,4,3,1,2
# This list means that the first fish has an internal timer of 3, the second fish has an internal timer of 4, and so on until the fifth fish, which has an internal timer of 2. Simulating these fish over several days would proceed as follows:
#
# Initial state: 3,4,3,1,2
# After  1 day:  2,3,2,0,1
# After  2 days: 1,2,1,6,0,8
# After  3 days: 0,1,0,5,6,7,8
# After  4 days: 6,0,6,4,5,6,7,8,8
# After  5 days: 5,6,5,3,4,5,6,7,7,8
# After  6 days: 4,5,4,2,3,4,5,6,6,7
# After  7 days: 3,4,3,1,2,3,4,5,5,6
# After  8 days: 2,3,2,0,1,2,3,4,4,5
# After  9 days: 1,2,1,6,0,1,2,3,3,4,8
# After 10 days: 0,1,0,5,6,0,1,2,2,3,7,8
# After 11 days: 6,0,6,4,5,6,0,1,1,2,6,7,8,8,8
# After 12 days: 5,6,5,3,4,5,6,0,0,1,5,6,7,7,7,8,8
# After 13 days: 4,5,4,2,3,4,5,6,6,0,4,5,6,6,6,7,7,8,8
# After 14 days: 3,4,3,1,2,3,4,5,5,6,3,4,5,5,5,6,6,7,7,8
# After 15 days: 2,3,2,0,1,2,3,4,4,5,2,3,4,4,4,5,5,6,6,7
# After 16 days: 1,2,1,6,0,1,2,3,3,4,1,2,3,3,3,4,4,5,5,6,8
# After 17 days: 0,1,0,5,6,0,1,2,2,3,0,1,2,2,2,3,3,4,4,5,7,8
# After 18 days: 6,0,6,4,5,6,0,1,1,2,6,0,1,1,1,2,2,3,3,4,6,7,8,8,8,8
# Each day, a 0 becomes a 6 and adds a new 8 to the end of the list, while each other number decreases by 1 if it was present at the start of the day.
#
# In this example, after 18 days, there are a total of 26 fish. After 80 days, there would be a total of 5934.
#
# Find a way to simulate lanternfish. How many lanternfish would there be after 80 days?
#
# Your puzzle answer was 386755.
#
# --- Part Two ---
# Suppose the lanternfish live forever and have unlimited food and space. Would they take over the entire ocean?
#
# After 256 days in the example above, there would be a total of 26984457539 lanternfish!
#
# How many lanternfish would there be after 256 days?
#
# Your puzzle answer was 1732731810807.
#
# Both parts of this puzzle are complete! They provide two gold stars: **

def load_input(file_name):
    a_file = open(file_name, "r")
    input = []
    for line in a_file:
        input = [int(element) for element in line.split(',')]
    return input


def problem_a():
    # initial = load_input("day_6_sample.txt")
    initial = load_input("day_6.txt")

    print("Initial state: ", initial)
    population = initial
    for day in range(0, 80):
        for i, fish in enumerate(population.copy()):
            if fish == 0:
                population.append(8)
                population[i] = 6
            else:
                population[i] = fish - 1
        print("After day ", (day + 1), "days: ", population)

    print('Result: ', len(population))


def group_fish(ungrouped_fish):
    grouped_fish = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for fish in ungrouped_fish:
        grouped_fish[fish] = grouped_fish[fish] + 1
    return grouped_fish


def problem_b():
    # initial = load_input("day_6_sample.txt")
    initial = load_input("day_6.txt")

    population = group_fish(initial)
    for day in range(0, 256):
        population_end = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        population_end[0] = population[1]
        population_end[1] = population[2]
        population_end[2] = population[3]
        population_end[3] = population[4]
        population_end[4] = population[5]
        population_end[5] = population[6]
        population_end[6] = population[7] + population[0]
        population_end[7] = population[8]
        population_end[8] = population[0]
        population = population_end
        print("After day ", (day + 1), "days: ", population)

    count = 0
    for fish in population :
        count += fish
    print('Result: ', count)


if __name__ == '__main__':
    problem_b()
