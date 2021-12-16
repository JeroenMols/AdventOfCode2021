from dataclasses import dataclass


def load_input(file_name):
    a_file = open(file_name, "r")
    for line in a_file:
        return line


@dataclass(eq=True, frozen=True)
class Path:
    points: []
    cost: int


@dataclass(eq=True, frozen=True)
class Point:
    x: int
    y: int


def problem_a():
    # hexadecimal = load_input("day_16_sample.txt")
    hexadecimal = load_input("day_16.txt")

    binary = ''
    for string in hexadecimal:
        binary += format(int(string, 16), "b").zfill(4)

    _, versions = read_packet(binary, 0)

    print("Result:", sum(versions))


def read_packet(binary, index):
    versions = []
    if binary[index + 3:index + 6] == '100':
        index, version = read_value_packet(binary, index)
        versions.append(version)
    else:
        index, new_versions = read_operator_packet(binary, index)
        versions = versions + new_versions
    return index, versions


def read_operator_packet(binary, index):
    versions = []
    versions.append(int(binary[index:index + 3], 2))
    index += 6

    if binary[index] == '0':
        index += 1
        subpacket_length = int(binary[index: index + 15], 2)
        print("subpacket length", subpacket_length)
        index += 15
        end = index + subpacket_length
        while index < end:
            index, new_versions = read_packet(binary, index)
            versions = versions + new_versions
    else:
        index += 1
        subpackets = int(binary[index: index + 11], 2)
        print("subpackets", subpackets)
        index += 11
        packets_read = 0
        while packets_read < subpackets:
            index, new_versions = read_packet(binary, index)
            versions = versions + new_versions
            packets_read += 1
    return index, versions


def read_value_packet(binary, index):
    version = int(binary[index:index + 3], 2)
    index += 6

    length = 0
    value = ''
    last_packet = False
    while not last_packet:
        value += binary[index + 1:index + 5]
        if binary[index] == '0':
            last_packet = True
            # index+= length %4
        index += 5
        length += 5
    # index += length % 4
    print("value packet", int(value, 2), index)
    return index, version


if __name__ == '__main__':
    problem_a()
