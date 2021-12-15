# --- Day 15: Chiton ---
# You've almost reached the exit of the cave, but the walls are getting closer together. Your submarine can barely still fit, though; the main problem is that the walls of the cave are covered in chitons, and it would be best not to bump any of them.
#
# The cavern is large, but has a very low ceiling, restricting your motion to two dimensions. The shape of the cavern resembles a square; a quick scan of chiton density produces a map of risk level throughout the cave (your puzzle input). For example:
#
# 1163751742
# 1381373672
# 2136511328
# 3694931569
# 7463417111
# 1319128137
# 1359912421
# 3125421639
# 1293138521
# 2311944581
# You start in the top left position, your destination is the bottom right position, and you cannot move diagonally. The number at each position is its risk level; to determine the total risk of an entire path, add up the risk levels of each position you enter (that is, don't count the risk level of your starting position unless you enter it; leaving it adds no risk to your total).
#
# Your goal is to find a path with the lowest total risk. In this example, a path with the lowest total risk is highlighted here:
#
# 1163751742
# 1381373672
# 2136511328
# 3694931569
# 7463417111
# 1319128137
# 1359912421
# 3125421639
# 1293138521
# 2311944581
# The total risk of this path is 40 (the starting position is never entered, so its risk is not counted).
#
# What is the lowest total risk of any path from the top left to the bottom right?
#
# Your puzzle answer was 696.
#
# The first half of this puzzle is complete! It provides one gold star: *
#
# --- Part Two ---
# Now that you know how to find low-risk paths in the cave, you can try to find your way out.
#
# The entire cave is actually five times larger in both dimensions than you thought; the area you originally scanned is just one tile in a 5x5 tile area that forms the full map. Your original map tile repeats to the right and downward; each time the tile repeats to the right or downward, all of its risk levels are 1 higher than the tile immediately up or left of it. However, risk levels above 9 wrap back around to 1. So, if your original map had some position with a risk level of 8, then that same position on each of the 25 total tiles would be as follows:
#
# 8 9 1 2 3
# 9 1 2 3 4
# 1 2 3 4 5
# 2 3 4 5 6
# 3 4 5 6 7
# Each single digit above corresponds to the example position with a value of 8 on the top-left tile. Because the full map is actually five times larger in both dimensions, that position appears a total of 25 times, once in each duplicated tile, with the values shown above.
#
# Here is the full five-times-as-large version of the first example above, with the original map in the top left corner highlighted:
#
# 11637517422274862853338597396444961841755517295286
# 13813736722492484783351359589446246169155735727126
# 21365113283247622439435873354154698446526571955763
# 36949315694715142671582625378269373648937148475914
# 74634171118574528222968563933317967414442817852555
# 13191281372421239248353234135946434524615754563572
# 13599124212461123532357223464346833457545794456865
# 31254216394236532741534764385264587549637569865174
# 12931385212314249632342535174345364628545647573965
# 23119445813422155692453326671356443778246755488935
# 22748628533385973964449618417555172952866628316397
# 24924847833513595894462461691557357271266846838237
# 32476224394358733541546984465265719557637682166874
# 47151426715826253782693736489371484759148259586125
# 85745282229685639333179674144428178525553928963666
# 24212392483532341359464345246157545635726865674683
# 24611235323572234643468334575457944568656815567976
# 42365327415347643852645875496375698651748671976285
# 23142496323425351743453646285456475739656758684176
# 34221556924533266713564437782467554889357866599146
# 33859739644496184175551729528666283163977739427418
# 35135958944624616915573572712668468382377957949348
# 43587335415469844652657195576376821668748793277985
# 58262537826937364893714847591482595861259361697236
# 96856393331796741444281785255539289636664139174777
# 35323413594643452461575456357268656746837976785794
# 35722346434683345754579445686568155679767926678187
# 53476438526458754963756986517486719762859782187396
# 34253517434536462854564757396567586841767869795287
# 45332667135644377824675548893578665991468977611257
# 44961841755517295286662831639777394274188841538529
# 46246169155735727126684683823779579493488168151459
# 54698446526571955763768216687487932779859814388196
# 69373648937148475914825958612593616972361472718347
# 17967414442817852555392896366641391747775241285888
# 46434524615754563572686567468379767857948187896815
# 46833457545794456865681556797679266781878137789298
# 64587549637569865174867197628597821873961893298417
# 45364628545647573965675868417678697952878971816398
# 56443778246755488935786659914689776112579188722368
# 55172952866628316397773942741888415385299952649631
# 57357271266846838237795794934881681514599279262561
# 65719557637682166874879327798598143881961925499217
# 71484759148259586125936169723614727183472583829458
# 28178525553928963666413917477752412858886352396999
# 57545635726865674683797678579481878968159298917926
# 57944568656815567976792667818781377892989248891319
# 75698651748671976285978218739618932984172914319528
# 56475739656758684176786979528789718163989182927419
# 67554889357866599146897761125791887223681299833479
# Equipped with the full map, you can now find a path from the top left corner to the bottom right corner with the lowest total risk:
#
# 11637517422274862853338597396444961841755517295286
# 13813736722492484783351359589446246169155735727126
# 21365113283247622439435873354154698446526571955763
# 36949315694715142671582625378269373648937148475914
# 74634171118574528222968563933317967414442817852555
# 13191281372421239248353234135946434524615754563572
# 13599124212461123532357223464346833457545794456865
# 31254216394236532741534764385264587549637569865174
# 12931385212314249632342535174345364628545647573965
# 23119445813422155692453326671356443778246755488935
# 22748628533385973964449618417555172952866628316397
# 24924847833513595894462461691557357271266846838237
# 32476224394358733541546984465265719557637682166874
# 47151426715826253782693736489371484759148259586125
# 85745282229685639333179674144428178525553928963666
# 24212392483532341359464345246157545635726865674683
# 24611235323572234643468334575457944568656815567976
# 42365327415347643852645875496375698651748671976285
# 23142496323425351743453646285456475739656758684176
# 34221556924533266713564437782467554889357866599146
# 33859739644496184175551729528666283163977739427418
# 35135958944624616915573572712668468382377957949348
# 43587335415469844652657195576376821668748793277985
# 58262537826937364893714847591482595861259361697236
# 96856393331796741444281785255539289636664139174777
# 35323413594643452461575456357268656746837976785794
# 35722346434683345754579445686568155679767926678187
# 53476438526458754963756986517486719762859782187396
# 34253517434536462854564757396567586841767869795287
# 45332667135644377824675548893578665991468977611257
# 44961841755517295286662831639777394274188841538529
# 46246169155735727126684683823779579493488168151459
# 54698446526571955763768216687487932779859814388196
# 69373648937148475914825958612593616972361472718347
# 17967414442817852555392896366641391747775241285888
# 46434524615754563572686567468379767857948187896815
# 46833457545794456865681556797679266781878137789298
# 64587549637569865174867197628597821873961893298417
# 45364628545647573965675868417678697952878971816398
# 56443778246755488935786659914689776112579188722368
# 55172952866628316397773942741888415385299952649631
# 57357271266846838237795794934881681514599279262561
# 65719557637682166874879327798598143881961925499217
# 71484759148259586125936169723614727183472583829458
# 28178525553928963666413917477752412858886352396999
# 57545635726865674683797678579481878968159298917926
# 57944568656815567976792667818781377892989248891319
# 75698651748671976285978218739618932984172914319528
# 56475739656758684176786979528789718163989182927419
# 67554889357866599146897761125791887223681299833479
# The total risk of this path is 315 (the starting position is still never entered, so its risk is not counted).
#
# Using the full map, what is the lowest total risk of any path from the top left to the bottom right?
#
# Answer:
#
#
# Although it hasn't changed, you can still get your puzzle input.

from dataclasses import dataclass


def load_input(file_name):
    a_file = open(file_name, "r")
    cavern = []
    for line in a_file:
        cavern.append([int(element) for element in list(line.strip())])
    return cavern


@dataclass(eq=True, frozen=True)
class Path:
    points: []


@dataclass(eq=True, frozen=True)
class Point:
    x: int
    y: int


def problem_a():
    # cavern = load_input("day_15_sample.txt")
    cavern = load_input("day_15.txt")

    min_cost = brute_force_all_paths(cavern)

    print("Result: ", min_cost)


# Very fast approach, but only considers moving down + right
def down_right_minimum(cavern):
    min_cost = []
    for y in range(0, len(cavern)):
        min_cost.append([0] * len(cavern[0]))
    for y in range(0, len(cavern)):
        cost_down = get(min_cost, 0, y - 1) + get(cavern, 0, y)
        min_cost[y][0] = cost_down
    for x in range(0, len(cavern[0])):
        cost_right = get(min_cost, x - 1, 0) + get(cavern, x, 0)
        min_cost[0][x] = cost_right
    for y in range(1, len(cavern)):
        for x in range(1, len(cavern[0])):
            cost_down = get(min_cost, x, y - 1) + get(cavern, x, y)
            cost_right = get(min_cost, x - 1, y) + get(cavern, x, y)
            min_cost[y][x] = min(cost_down, cost_right)

    return min_cost[-1][-1] - cavern[0][0]


def get(data, x, y, default=0):
    if x < 0 or y < 0:
        return default
    else:
        return data[y][x]


def print_data(data):
    for y in range(0, len(data)):
        line = ''
        for x in range(0, len(data[0])):
            if data[y][x] < 10:
                line += '0' + str(data[y][x]) + '|'
            else:
                line += str(data[y][x]) + '|'
        print(line)


# Steps in all directions, tries to smartly discard paths but is still very slow
def brute_force_all_paths(cavern):
    next_paths = [Path([Point(0, 0)])]

    # take path straight down and to right as first guess of minimum
    min_cost = down_right_minimum(cavern) + cavern[0][0]

    end_point = Point(len(cavern[0]) - 1, len(cavern) - 1)

    for step in range(0, len(cavern) * len(cavern[0])):

        print(step, '/', len(cavern) * len(cavern[0]))
        paths = next_paths
        next_paths_dict = {}
        for path in paths:
            next_points = []
            if path.points[-1].x > 0:
                left = Point(path.points[-1].x - 1, path.points[-1].y)
                next_points.append(left)
            if path.points[-1].x < len(cavern[0]) - 1:
                right = Point(path.points[-1].x + 1, path.points[-1].y)
                next_points.append(right)
            if path.points[-1].y > 0:
                up = Point(path.points[-1].x, path.points[-1].y - 1)
                next_points.append(up)
            if path.points[-1].y < len(cavern) - 1:
                down = Point(path.points[-1].x, path.points[-1].y + 1)
                next_points.append(down)

            for point in next_points:
                # Reached end point
                if point == end_point:
                    new_points = path.points.copy()
                    new_points.append(point)
                    min_cost = min(calculate_cost(cavern, new_points), min_cost)
                    continue

                # Don't allow loops
                if point in path.points:
                    continue

                new_points = path.points.copy()
                new_points.append(point)
                new_cost = calculate_cost(cavern, new_points)

                # Stop processing path when cost higher than current min
                if new_cost > min_cost:
                    continue

                # Only consider path if cheaper than other path to same point
                elif point in next_paths_dict:
                    cost = calculate_cost(cavern, next_paths_dict[point].points)
                    if new_cost < cost:
                        next_paths_dict[point] = Path(new_points)
                else:
                    next_paths_dict[point] = Path(new_points)

        next_paths = next_paths_dict.values()

        if len(next_paths) == 0:
            print("done")
            break

    return min_cost - cavern[0][0]


def calculate_min_cost(cavern, paths_to_end):
    costs = []
    for path in paths_to_end:
        cost = 0
        for point in path.points:
            cost += cavern[point.y][point.x]
        costs.append(cost)
    return min(costs)


def calculate_cost(cavern, points):
    cost = 0
    for point in points:
        cost += cavern[point.y][point.x]
    return cost


def problem_b():
    pass


if __name__ == '__main__':
    problem_a()
