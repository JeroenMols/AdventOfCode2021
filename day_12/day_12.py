# --- Day 12: Passage Pathing ---
# With your submarine's subterranean subsystems subsisting suboptimally, the only way you're getting out of this cave anytime soon is by finding a path yourself. Not just a path - the only way to know if you've found the best path is to find all of them.
#
# Fortunately, the sensors are still mostly working, and so you build a rough map of the remaining caves (your puzzle input). For example:
#
# start-A
# start-b
# A-c
# A-b
# b-d
# A-end
# b-end
# This is a list of how all of the caves are connected. You start in the cave named start, and your destination is the cave named end. An entry like b-d means that cave b is connected to cave d - that is, you can move between them.
#
# So, the above cave system looks roughly like this:
#
#     start
#     /   \
# c--A-----b--d
#     \   /
#      end
# Your goal is to find the number of distinct paths that start at start, end at end, and don't visit small caves more than once. There are two types of caves: big caves (written in uppercase, like A) and small caves (written in lowercase, like b). It would be a waste of time to visit any small cave more than once, but big caves are large enough that it might be worth visiting them multiple times. So, all paths you find should visit small caves at most once, and can visit big caves any number of times.
#
# Given these rules, there are 10 paths through this example cave system:
#
# start,A,b,A,c,A,end
# start,A,b,A,end
# start,A,b,end
# start,A,c,A,b,A,end
# start,A,c,A,b,end
# start,A,c,A,end
# start,A,end
# start,b,A,c,A,end
# start,b,A,end
# start,b,end
# (Each line in the above list corresponds to a single path; the caves visited by that path are listed in the order they are visited and separated by commas.)
#
# Note that in this cave system, cave d is never visited by any path: to do so, cave b would need to be visited twice (once on the way to cave d and a second time when returning from cave d), and since cave b is small, this is not allowed.
#
# Here is a slightly larger example:
#
# dc-end
# HN-start
# start-kj
# dc-start
# dc-HN
# LN-dc
# HN-end
# kj-sa
# kj-HN
# kj-dc
# The 19 paths through it are as follows:
#
# start,HN,dc,HN,end
# start,HN,dc,HN,kj,HN,end
# start,HN,dc,end
# start,HN,dc,kj,HN,end
# start,HN,end
# start,HN,kj,HN,dc,HN,end
# start,HN,kj,HN,dc,end
# start,HN,kj,HN,end
# start,HN,kj,dc,HN,end
# start,HN,kj,dc,end
# start,dc,HN,end
# start,dc,HN,kj,HN,end
# start,dc,end
# start,dc,kj,HN,end
# start,kj,HN,dc,HN,end
# start,kj,HN,dc,end
# start,kj,HN,end
# start,kj,dc,HN,end
# start,kj,dc,end
# Finally, this even larger example has 226 paths through it:
#
# fs-end
# he-DX
# fs-he
# start-DX
# pj-DX
# end-zg
# zg-sl
# zg-pj
# pj-he
# RW-he
# fs-DX
# pj-RW
# zg-RW
# start-pj
# he-WI
# zg-he
# pj-fs
# start-RW
# How many paths through this cave system are there that visit small caves at most once?
#
# Your puzzle answer was 5457.
#
# --- Part Two ---
# After reviewing the available paths, you realize you might have time to visit a single small cave twice. Specifically, big caves can be visited any number of times, a single small cave can be visited at most twice, and the remaining small caves can be visited at most once. However, the caves named start and end can only be visited exactly once each: once you leave the start cave, you may not return to it, and once you reach the end cave, the path must end immediately.
#
# Now, the 36 possible paths through the first example above are:
#
# start,A,b,A,b,A,c,A,end
# start,A,b,A,b,A,end
# start,A,b,A,b,end
# start,A,b,A,c,A,b,A,end
# start,A,b,A,c,A,b,end
# start,A,b,A,c,A,c,A,end
# start,A,b,A,c,A,end
# start,A,b,A,end
# start,A,b,d,b,A,c,A,end
# start,A,b,d,b,A,end
# start,A,b,d,b,end
# start,A,b,end
# start,A,c,A,b,A,b,A,end
# start,A,c,A,b,A,b,end
# start,A,c,A,b,A,c,A,end
# start,A,c,A,b,A,end
# start,A,c,A,b,d,b,A,end
# start,A,c,A,b,d,b,end
# start,A,c,A,b,end
# start,A,c,A,c,A,b,A,end
# start,A,c,A,c,A,b,end
# start,A,c,A,c,A,end
# start,A,c,A,end
# start,A,end
# start,b,A,b,A,c,A,end
# start,b,A,b,A,end
# start,b,A,b,end
# start,b,A,c,A,b,A,end
# start,b,A,c,A,b,end
# start,b,A,c,A,c,A,end
# start,b,A,c,A,end
# start,b,A,end
# start,b,d,b,A,c,A,end
# start,b,d,b,A,end
# start,b,d,b,end
# start,b,end
# The slightly larger example above now has 103 paths through it, and the even larger example now has 3509 paths through it.
#
# Given these new rules, how many paths through this cave system are there?
#
# Your puzzle answer was 128506.
#
# Both parts of this puzzle are complete! They provide two gold stars: **

def load_input(file_name):
    a_file = open(file_name, "r")
    input = []
    for line in a_file:
        route = line.strip().split('-')
        input.append(Path(route[0], route[1]))
    return input


class Path:
    start: str
    end: str

    def __init__(self, start, end):
        self.start = start
        self.end = end


class Route:
    nodes: []
    allow_one_double_visit: bool

    def __init__(self, nodes, allow_one_double_visit=False):
        self.nodes = nodes
        self.allow_one_double_visit = allow_one_double_visit

    def end(self):
        return self.nodes[-1]

    def can_pass_by(self, node):
        if node == 'start' and 'start' in self.nodes:
            return False
        if node.islower() and node in self.nodes:
            if not self.allow_one_double_visit:
                return False
            elif not self.has_double():
                return True
            else:
                return False
        else:
            return True

    def has_double(self):
        lower_nodes = []
        for node in self.nodes:
            if not node.islower():
                continue
            elif node in lower_nodes:
                return True
            else:
                lower_nodes.append(node)
        return False

    def finished(self):
        if self.nodes[-1] == 'end':
            return True
        else:
            return False

    def __str__(self):
        to_string = ''
        for node in self.nodes:
            to_string += node + ','
        return to_string[:-1]


def problem_a():
    # paths = load_input("day_12_sample.txt")
    paths = load_input("day_12.txt")

    new_routes = [Route(['start'])]
    completed_routes = []
    while len(new_routes) > 0:
        new_routes, completed = routes_step(new_routes, paths, False)
        completed_routes += completed

    print_routes(completed_routes)
    print("Result: ", len(completed_routes))


def problem_b():
    # paths = load_input("day_12_sample.txt")
    paths = load_input("day_12.txt")

    new_routes = [Route(['start'])]
    completed_routes = []
    while len(new_routes) > 0:
        new_routes, completed = routes_step(new_routes, paths, True)
        completed_routes += completed

    print_routes(completed_routes)
    print("Result: ", len(completed_routes))


def routes_step(routes, paths, allow_double):
    new_routes = []
    completed_routes = []
    for route in routes:

        if route.finished():
            completed_routes.append(route)
            continue

        for path in paths:
            if route.end() == path.start:
                if route.can_pass_by(path.end):
                    new_nodes = route.nodes.copy() + [path.end]
                    new_routes.append(Route(new_nodes, allow_double))
            elif route.end() == path.end:
                if route.can_pass_by(path.start):
                    new_nodes = route.nodes.copy() + [path.start]
                    new_routes.append(Route(new_nodes, allow_double))

    return new_routes, completed_routes


def print_routes(routes):
    for route in routes:
        print(route)


if __name__ == '__main__':
    problem_b()
