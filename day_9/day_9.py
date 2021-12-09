# --- Day 9: Smoke Basin ---
# These caves seem to be lava tubes. Parts are even still volcanically active; small hydrothermal vents release smoke into the caves that slowly settles like rain.
#
# If you can model how the smoke flows through the caves, you might be able to avoid it and be that much safer. The submarine generates a heightmap of the floor of the nearby caves for you (your puzzle input).
#
# Smoke flows to the lowest point of the area it's in. For example, consider the following heightmap:
#
# 2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678
# Each number corresponds to the height of a particular location, where 9 is the highest and 0 is the lowest a location can be.
#
# Your first goal is to find the low points - the locations that are lower than any of its adjacent locations. Most locations have four adjacent locations (up, down, left, and right); locations on the edge or corner of the map have three or two adjacent locations, respectively. (Diagonal locations do not count as adjacent.)
#
# In the above example, there are four low points, all highlighted: two are in the first row (a 1 and a 0), one is in the third row (a 5), and one is in the bottom row (also a 5). All other locations on the heightmap have some lower adjacent location, and so are not low points.
#
# The risk level of a low point is 1 plus its height. In the above example, the risk levels of the low points are 2, 1, 6, and 6. The sum of the risk levels of all low points in the heightmap is therefore 15.
#
# Find all of the low points on your heightmap. What is the sum of the risk levels of all low points on your heightmap?
#
# Your puzzle answer was 532.
#
# The first half of this puzzle is complete! It provides one gold star: *
#
# --- Part Two ---
# Next, you need to find the largest basins so you know what areas are most important to avoid.
#
# A basin is all locations that eventually flow downward to a single low point. Therefore, every low point has a basin, although some basins are very small. Locations of height 9 do not count as being in any basin, and all other locations will always be part of exactly one basin.
#
# The size of a basin is the number of locations within the basin, including the low point. The example above has four basins.
#
# The top-left basin, size 3:
#
# 2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678
# The top-right basin, size 9:
#
# 2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678
# The middle basin, size 14:
#
# 2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678
# The bottom-right basin, size 9:
#
# 2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678
# Find the three largest basins and multiply their sizes together. In the above example, this is 9 * 14 * 9 = 1134.
#
# What do you get if you multiply together the sizes of the three largest basins?


from dataclasses import dataclass


def load_input(file_name):
    a_file = open(file_name, "r")
    input = []
    for line in a_file:
        input.append(line.strip())
    return input


def getValueAtPosition(lines, x, y, default):
    if y < 0 or y >= len(lines) or x < 0 or x >= len(lines[0]):
        return default
    else:
        return int(lines[y][x])


def problem_a():
    # lines = load_input("day_9_sample.txt")
    lines = load_input("day_9.txt")

    minima = []
    for y, line in enumerate(lines):
        for x, pointStr in enumerate(line):
            if isMinimum(lines, x, y):
                minima.append(int(pointStr))

    print('Result:', sum(minima) + len(minima))


def isMinimum(lines, x, y):
    point = getValueAtPosition(lines, x, y, 9)
    left = getValueAtPosition(lines, x - 1, y, 9)
    right = getValueAtPosition(lines, x + 1, y, 9)
    up = getValueAtPosition(lines, x, y - 1, 9)
    down = getValueAtPosition(lines, x, y + 1, 9)
    return point < left and point < right and point < up and point < down


def getMinimumSize(lines, x, y, minimum_size=1):
    new_lines = lines.copy()
    new_lines[y] = new_lines[y][:x] + '9' + new_lines[y][x + 1:]

    left = isMinimum(new_lines, x - 1, y)
    right = isMinimum(new_lines, x + 1, y)
    up = isMinimum(new_lines, x, y - 1)
    down = isMinimum(new_lines, x, y + 1)
    if left:
        minimum_size += getMinimumSize(new_lines, x - 1, y)

    if right:
        minimum_size += getMinimumSize(new_lines, x + 1, y)

    if up:
        minimum_size += getMinimumSize(new_lines, x, y - 1)

    if down:
        minimum_size += getMinimumSize(new_lines, x, y + 1)

    return minimum_size


@dataclass(eq=True, frozen=True)
class Point:
    x: int
    y: int


def problem_b():
    # lines = load_input("day_9_sample.txt")
    lines = load_input("day_9.txt")

    minima = []
    for y, line in enumerate(lines):
        for x, pointStr in enumerate(line):
            if isMinimum(lines, x, y):
                minima.append(getMinimumSize(lines, Point(x, y)))

    print(minima)
    minima.sort(reverse=True)
    print(minima)
    print('Result:', minima[0]*minima[1]*minima[2])


# Does not fully work, because this searches linearly for minima, whereas in reality a minimum could appear
# depending on the order in which the points around it are marked as a mimimum.
# Hence this misses some minima from the basin (that aren't discovered on the first pass)
def getMinimumSize(lines, start_point):
    new_lines = lines.copy()
    new_lines[start_point.y] = new_lines[start_point.y][:start_point.x] + '9' + new_lines[start_point.y][start_point.x + 1:]

    minimum_size = 1
    minima = [start_point]
    while len(minima) > 0:
        new_minima = []
        for min in minima:
            x = min.x
            y = min.y

            if isMinimum(new_lines, x - 1, y):
                minimum_size += 1
                point = Point(x - 1, y)
                new_lines[point.y] = new_lines[point.y][:point.x] + '9' + new_lines[point.y][point.x + 1:]
                new_minima.append(point)

            if isMinimum(new_lines, x + 1, y):
                minimum_size += 1
                point = Point(x + 1, y)
                new_lines[point.y] = new_lines[point.y][:point.x] + '9' + new_lines[point.y][point.x + 1:]
                new_minima.append(point)

            if isMinimum(new_lines, x, y - 1):
                minimum_size += 1
                point = Point(x, y - 1)
                new_lines[point.y] = new_lines[point.y][:point.x] + '9' + new_lines[point.y][point.x + 1:]
                new_minima.append(point)

            if isMinimum(new_lines, x, y + 1):
                minimum_size += 1
                point = Point(x, y + 1)
                new_lines[point.y] = new_lines[point.y][:point.x] + '9' + new_lines[point.y][point.x + 1:]
                new_minima.append(point)

        minima = new_minima

    print(start_point, " - ", minimum_size)

    return minimum_size


if __name__ == '__main__':
    problem_b()
