# --- Day 5: Hydrothermal Venture ---
# You come across a field of hydrothermal vents on the ocean floor! These vents constantly produce large, opaque clouds, so it would be best to avoid them if possible.
#
# They tend to form in lines; the submarine helpfully produces a list of nearby lines of vents (your puzzle input) for you to review. For example:
#
# 0,9 -> 5,9
# 8,0 -> 0,8
# 9,4 -> 3,4
# 2,2 -> 2,1
# 7,0 -> 7,4
# 6,4 -> 2,0
# 0,9 -> 2,9
# 3,4 -> 1,4
# 0,0 -> 8,8
# 5,5 -> 8,2
# Each line of vents is given as a line segment in the format x1,y1 -> x2,y2 where x1,y1 are the coordinates of one end the line segment and x2,y2 are the coordinates of the other end. These line segments include the points at both ends. In other words:
#
# An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
# An entry like 9,7 -> 7,7 covers points 9,7, 8,7, and 7,7.
# For now, only consider horizontal and vertical lines: lines where either x1 = x2 or y1 = y2.
#
# So, the horizontal and vertical lines from the above list would produce the following diagram:
#
# .......1..
# ..1....1..
# ..1....1..
# .......1..
# .112111211
# ..........
# ..........
# ..........
# ..........
# 222111....
# In this diagram, the top left corner is 0,0 and the bottom right corner is 9,9. Each position is shown as the number of lines which cover that point or . if no line covers that point. The top-left pair of 1s, for example, comes from 2,2 -> 2,1; the very bottom row is formed by the overlapping lines 0,9 -> 5,9 and 0,9 -> 2,9.
#
# To avoid the most dangerous areas, you need to determine the number of points where at least two lines overlap. In the above example, this is anywhere in the diagram with a 2 or larger - a total of 5 points.
#
# Consider only horizontal and vertical lines. At how many points do at least two lines overlap?
#
# Your puzzle answer was 5169.
#
# --- Part Two ---
# Unfortunately, considering only horizontal and vertical lines doesn't give you the full picture; you need to also consider diagonal lines.
#
# Because of the limits of the hydrothermal vent mapping system, the lines in your list will only ever be horizontal, vertical, or a diagonal line at exactly 45 degrees. In other words:
#
# An entry like 1,1 -> 3,3 covers points 1,1, 2,2, and 3,3.
# An entry like 9,7 -> 7,9 covers points 9,7, 8,8, and 7,9.
# Considering all lines from the above example would now produce the following diagram:
#
# 1.1....11.
# .111...2..
# ..2.1.111.
# ...1.2.2..
# .112313211
# ...1.2....
# ..1...1...
# .1.....1..
# 1.......1.
# 222111....
# You still need to determine the number of points where at least two lines overlap. In the above example, this is still anywhere in the diagram with a 2 or larger - now a total of 12 points.
#
# Consider all of the lines. At how many points do at least two lines overlap?
#
# Your puzzle answer was 22083.
#
# Both parts of this puzzle are complete! They provide two gold stars: **

from dataclasses import dataclass

@dataclass(eq=True, frozen=True)
class Point:
    x: int
    y: int


@dataclass
class Line:
    start: Point
    end: Point

    def is_horizontal(self):
        return self.start.y == self.end.y

    def is_vertical(self):
        return self.start.x == self.end.x


def load_input(file_name):
    a_file = open(file_name, "r")
    input = []
    for line in a_file:
        points = line.split('->')
        start = points[0].split(',')
        end = points[1].split(',')
        input.append(Line(Point(int(start[0]), int(start[1])), Point(int(end[0]), int(end[1]))))
    return input


def problem_a():
    # lines = load_input("day_5_sample.txt")
    lines = load_input("day_5.txt")

    points = {Point(-1, -1): 0}
    for line in lines:
        if line.is_vertical():
            if line.start.y < line.end.y:
                start = line.start.y
                end = line.end.y + 1
            else:
                start = line.end.y
                end = line.start.y + 1

            for i in range(start, end):
                new_point = Point(line.start.x, i)
                points[new_point] = points.get(new_point, 0) + 1

        elif line.is_horizontal():
            if line.start.x < line.end.x:
                start = line.start.x
                end = line.end.x + 1
            else:
                start = line.end.x
                end = line.start.x + 1

            for i in range(start, end):
                new_point = Point(i, line.start.y)
                points[new_point] = points.get(new_point, 0) + 1

    duplicate_points = list(filter(lambda it: it > 1, list(points.values())))
    print('Result: ', len(duplicate_points))


def problem_b():
    # lines = load_input("day_5_sample.txt")
    lines = load_input("day_5.txt")

    points = {Point(-1, -1): 0}
    for line in lines:
        if line.is_vertical():
            if line.start.y < line.end.y:
                start = line.start.y
                end = line.end.y + 1
            else:
                start = line.end.y
                end = line.start.y + 1

            for i in range(start, end):
                new_point = Point(line.start.x, i)
                points[new_point] = points.get(new_point, 0) + 1

        elif line.is_horizontal():
            if line.start.x < line.end.x:
                start = line.start.x
                end = line.end.x + 1
            else:
                start = line.end.x
                end = line.start.x + 1

            for i in range(start, end):
                new_point = Point(i, line.start.y)
                points[new_point] = points.get(new_point, 0) + 1

        else:
            current = line.start
            points[current] = points.get(current, 0) + 1
            while current != line.end:
                if current.x < line.end.x:
                    if current.y < line.end.y:
                        current = Point(current.x + 1, current.y + 1)
                    else:
                        current = Point(current.x + 1, current.y - 1)
                else:
                    if current.y < line.end.y:
                        current = Point(current.x - 1, current.y + 1)
                    else:
                        current = Point(current.x - 1, current.y - 1)
                points[current] = points.get(current, 0) + 1

    duplicate_points = list(filter(lambda it: it > 1, list(points.values())))
    print('Result: ', len(duplicate_points))


if __name__ == '__main__':
    problem_b()
