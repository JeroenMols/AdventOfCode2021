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
    print(max_x, 'x',max_y)
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
