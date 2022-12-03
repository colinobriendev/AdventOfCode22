import string


def calculate_priority_score_1():
    score = 0
    with open('data/day3.txt', 'r') as file:
        # Separate the 2
        for line in file:
            compartment1, compartment2 = line[:len(line) // 2], line[len(line) // 2:]
            common_character = find_common_character(compartment1, compartment2)
            # Calculate priority
            score += calculate_priority(common_character)
    print('Score 1 = ' + str(score))


def calculate_priority_score_2():
    score = 0
    group_of_3 = []
    counter = 0
    with open('data/day3.txt', 'r') as file:
        for line in file:
            group_of_3.append(line.strip())
            if counter == 2:
                # because I now know I need next and can use an inter and a set, hello 1 liner
                duplicate = next(iter(set(group_of_3[0]).intersection(set(group_of_3[1]), set(group_of_3[2]))))
                score += calculate_priority(duplicate)
                counter = 0
                group_of_3 = []
            else:
                counter += 1
    print('Score 2 = ' + str(score))


def find_common_character(compartment1, compartment2):
    c_1_set = set(compartment1)
    c_2_set = set(compartment2)
    # Use set intersection to find first common between the two
    common_character = next(iter(c_1_set.intersection(c_2_set)))
    return common_character


def calculate_priority(common_character):
    lower = dict(zip(string.ascii_lowercase, range(1, 27)))
    upper = dict(zip(string.ascii_uppercase, range(27, 53)))

    if common_character in lower:
        score = int(lower[common_character])
    else:
        score = int(upper[common_character])

    return score


calculate_priority_score_1()
calculate_priority_score_2()
