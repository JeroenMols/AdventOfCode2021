# --- Day 13: Transparent Origami ---
# You reach another volcanically active part of the cave. It would be nice if you could do some kind of thermal imaging so you could tell ahead of time which caves are too hot to safely enter.
#
# Fortunately, the submarine seems to be equipped with a thermal camera! When you activate it, you are greeted with:
#
# Congratulations on your purchase! To activate this infrared thermal imaging
# camera system, please enter the code found on page 1 of the manual.
# Apparently, the Elves have never used this feature. To your surprise, you manage to find the manual; as you go to open it, page 1 falls out. It's a large sheet of transparent paper! The transparent paper is marked with random dots and includes instructions on how to fold it up (your puzzle input). For example:
#
# 6,10
# 0,14
# 9,10
# 0,3
# 10,4
# 4,11
# 6,0
# 6,12
# 4,1
# 0,13
# 10,12
# 3,4
# 3,0
# 8,4
# 1,10
# 2,14
# 8,10
# 9,0
#
# fold along y=7
# fold along x=5
# The first section is a list of dots on the transparent paper. 0,0 represents the top-left coordinate. The first value, x, increases to the right. The second value, y, increases downward. So, the coordinate 3,0 is to the right of 0,0, and the coordinate 0,7 is below 0,0. The coordinates in this example form the following pattern, where # is a dot on the paper and . is an empty, unmarked position:
#
# ...#..#..#.
# ....#......
# ...........
# #..........
# ...#....#.#
# ...........
# ...........
# ...........
# ...........
# ...........
# .#....#.##.
# ....#......
# ......#...#
# #..........
# #.#........
# Then, there is a list of fold instructions. Each instruction indicates a line on the transparent paper and wants you to fold the paper up (for horizontal y=... lines) or left (for vertical x=... lines). In this example, the first fold instruction is fold along y=7, which designates the line formed by all of the positions where y is 7 (marked here with -):
#
# ...#..#..#.
# ....#......
# ...........
# #..........
# ...#....#.#
# ...........
# ...........
# -----------
# ...........
# ...........
# .#....#.##.
# ....#......
# ......#...#
# #..........
# #.#........
# Because this is a horizontal line, fold the bottom half up. Some of the dots might end up overlapping after the fold is complete, but dots will never appear exactly on a fold line. The result of doing this fold looks like this:
#
# #.##..#..#.
# #...#......
# ......#...#
# #...#......
# .#.#..#.###
# ...........
# ...........
# Now, only 17 dots are visible.
#
# Notice, for example, the two dots in the bottom left corner before the transparent paper is folded; after the fold is complete, those dots appear in the top left corner (at 0,0 and 0,1). Because the paper is transparent, the dot just below them in the result (at 0,3) remains visible, as it can be seen through the transparent paper.
#
# Also notice that some dots can end up overlapping; in this case, the dots merge together and become a single dot.
#
# The second fold instruction is fold along x=5, which indicates this line:
#
# #.##.|#..#.
# #...#|.....
# .....|#...#
# #...#|.....
# .#.#.|#.###
# .....|.....
# .....|.....
# Because this is a vertical line, fold left:
#
# #####
# #...#
# #...#
# #...#
# #####
# .....
# .....
# The instructions made a square!
#
# The transparent paper is pretty big, so for now, focus on just completing the first fold. After the first fold in the example above, 17 dots are visible - dots that end up overlapping after the fold is completed count as a single dot.
#
# How many dots are visible after completing just the first fold instruction on your transparent paper?
#
# Your puzzle answer was 737.
#
# --- Part Two ---
# Finish folding the transparent paper according to the instructions. The manual says the code is always eight capital letters.
#
# What code do you use to activate the infrared thermal imaging camera system?
#
# Your puzzle answer was ZUJUAFHP.
#
# Both parts of this puzzle are complete! They provide two gold stars: **

from dataclasses import dataclass


def load_input(file_name):
    a_file = open(file_name, "r")
    dots = []
    folds = []
    for line in a_file:
        if line.startswith("fold"):
            raw_fold = line.split(' ')[-1].split('=')
            folds.append(Fold(raw_fold[0], int(raw_fold[1])))
        elif ',' in line:
            raw_dot = line.strip().split(',')
            dots.append(Point(int(raw_dot[0]), int(raw_dot[1])))
    return dots, folds


@dataclass(eq=True, frozen=True)
class Point:
    x: int
    y: int


@dataclass(eq=True, frozen=True)
class Fold:
    axes: str
    value: int


def problem_a():
    # dots, folds = load_input("day_13_sample.txt")
    dots, folds = load_input("day_13.txt")

    dots = fold_paper(dots, folds[0])

    print("Result: ", len(dots))


def problem_b():
    # dots, folds = load_input("day_13_sample.txt")
    dots, folds = load_input("day_13.txt")

    for fold in folds:
        dots = fold_paper(dots, fold)

    print("Result: ")
    print_dots(dots)


def fold_paper(dots, fold):
    new_dots = set()
    print(fold)
    for dot in dots:
        if fold.axes == 'y':
            if dot.y <= fold.value:
                new_dots.add(dot)
                print("  no need to fold", dot)
            else:
                folded_dot = Point(dot.x, fold.value - (dot.y - fold.value))
                print("  folding dot", dot, "to", folded_dot)
                if folded_dot.y < 0:
                    print(" dot off paper")
                else:
                    new_dots.add(folded_dot)
        else:
            if dot.x <= fold.value:
                new_dots.add(dot)
                print("  no need to fold", dot)
            else:
                folded_dot = Point(fold.value - (dot.x - fold.value), dot.y)
                print("  folding dot", dot, "to", folded_dot)
                if folded_dot.x < 0:
                    print(" dot off paper")
                else:
                    new_dots.add(folded_dot)
    dots = new_dots.copy()
    return dots


def print_dots(dots):
    max_x = max(list(map(lambda dot: dot.x, dots)))
    max_y = max(list(map(lambda dot: dot.y, dots)))
    print(max_x, 'x', max_y)
    print("-------------------------------------------")
    for y in range(0, max_y + 1):
        line = ''
        for x in range(0, max_x + 1):
            if Point(x, y) in dots:
                line += "#"
            else:
                line += "."
        print(line)
    pass


if __name__ == '__main__':
    problem_b()
