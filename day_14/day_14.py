# --- Day 14: Extended Polymerization ---
# The incredible pressures at this depth are starting to put a strain on your submarine. The submarine has polymerization equipment that would produce suitable materials to reinforce the submarine, and the nearby volcanically-active caves should even have the necessary input elements in sufficient quantities.
#
# The submarine manual contains instructions for finding the optimal polymer formula; specifically, it offers a polymer template and a list of pair insertion rules (your puzzle input). You just need to work out what polymer would result after repeating the pair insertion process a few times.
#
# For example:
#
# NNCB
#
# CH -> B
# HH -> N
# CB -> H
# NH -> C
# HB -> C
# HC -> B
# HN -> C
# NN -> C
# BH -> H
# NC -> B
# NB -> B
# BN -> B
# BB -> N
# BC -> B
# CC -> N
# CN -> C
# The first line is the polymer template - this is the starting point of the process.
#
# The following section defines the pair insertion rules. A rule like AB -> C means that when elements A and B are immediately adjacent, element C should be inserted between them. These insertions all happen simultaneously.
#
# So, starting with the polymer template NNCB, the first step simultaneously considers all three pairs:
#
# The first pair (NN) matches the rule NN -> C, so element C is inserted between the first N and the second N.
# The second pair (NC) matches the rule NC -> B, so element B is inserted between the N and the C.
# The third pair (CB) matches the rule CB -> H, so element H is inserted between the C and the B.
# Note that these pairs overlap: the second element of one pair is the first element of the next pair. Also, because all pairs are considered simultaneously, inserted elements are not considered to be part of a pair until the next step.
#
# After the first step of this process, the polymer becomes NCNBCHB.
#
# Here are the results of a few steps using the above rules:
#
# Template:     NNCB
# After step 1: NCNBCHB
# After step 2: NBCCNBBBCBHCB
# After step 3: NBBBCNCCNBBNBNBBCHBHHBCHB
# After step 4: NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB
# This polymer grows quickly. After step 5, it has length 97; After step 10, it has length 3073. After step 10, B occurs 1749 times, C occurs 298 times, H occurs 161 times, and N occurs 865 times; taking the quantity of the most common element (B, 1749) and subtracting the quantity of the least common element (H, 161) produces 1749 - 161 = 1588.
#
# Apply 10 steps of pair insertion to the polymer template and find the most and least common elements in the result. What do you get if you take the quantity of the most common element and subtract the quantity of the least common element?
#
# Your puzzle answer was 3408.
#
# --- Part Two ---
# The resulting polymer isn't nearly strong enough to reinforce the submarine. You'll need to run more steps of the pair insertion process; a total of 40 steps should do it.
#
# In the above example, the most common element is B (occurring 2192039569602 times) and the least common element is H (occurring 3849876073 times); subtracting these produces 2188189693529.
#
# Apply 40 steps of pair insertion to the polymer template and find the most and least common elements in the result. What do you get if you take the quantity of the most common element and subtract the quantity of the least common element?
#
# Your puzzle answer was 3724343376942.
#
# Both parts of this puzzle are complete! They provide two gold stars: **

def load_input(file_name):
    a_file = open(file_name, "r")
    template = ''
    insertions = {}
    for line in a_file:
        if '->' in line:
            raw_insertions = line.strip().split(' -> ')
            insertions[raw_insertions[0]] = raw_insertions[1]
        elif line.strip() == '':
            continue
        else:
            template = line.strip()
    return template, insertions


def problem_a():
    template, insertions = load_input("day_14_sample.txt")
    # template, insertions = load_input("day_14.txt")

    processed = perform_insertions(template, insertions, 10)
    occurrences = get_occurrences(processed)

    print (occurrences)
    print("Result: ", max(occurrences.values()) - min(occurrences.values()))

def problem_b():
    # template, insertions = load_input("day_14_sample.txt")
    template, insertions = load_input("day_14.txt")

    times = 40
    initial = 20

    first_pass = perform_insertions(template, insertions, initial)

    # Split in smaller shards
    shards = []
    for index in range(0, len(first_pass) - 1):
        shards.append(first_pass[index] + first_pass[index + 1])

    shard_occurrences = process_shards(initial, insertions, shards, times)
    occurrences = merge_shard_occurrences(shard_occurrences)

    print("Result: ", max(occurrences.values()) - min(occurrences.values()))


def process_shards(initial, insertions, shards, times):
    cache = {}
    shard_occurrences = []
    for index, shard in enumerate(shards):
        if index == len(shards) - 1:
            processed = perform_insertions(shard, insertions, times - initial)
            shard_occurrences.append(get_occurrences(processed))
        else:
            if shard not in cache.keys():
                # Exclude last element as that's duplicate in the next shard.
                processed = perform_insertions(shard, insertions, times - initial)
                cache[shard] = get_occurrences(processed[0:len(processed) - 1])
            shard_occurrences.append(cache[shard])
        print(index,'/', len(shards))
    return shard_occurrences


def perform_insertions(shard, insertions, times):
    for step in range(0, times):
        new_shard = [shard[0]]
        for index in range(1, len(shard)):
            new_shard.append(insertions[(shard[index - 1] + shard[index])])
            new_shard.append(shard[index])
        shard = new_shard.copy()
    return shard


def get_occurrences(template):
    occurrences = {}
    for char in template:
        if char in occurrences:
            occurrences[char] = occurrences[char] + 1
        else:
            occurrences[char] = 1
    return occurrences


def merge_shard_occurrences(shard_occurrences):
    occurrences = {}
    for shard_occurrences in shard_occurrences:
        for char in shard_occurrences:
            if char in occurrences:
                occurrences[char] = occurrences[char] + shard_occurrences[char]
            else:
                occurrences[char] = shard_occurrences[char]
    return occurrences


if __name__ == '__main__':
    problem_b()
