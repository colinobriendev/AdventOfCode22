def find_highest_calories():
    file_input = open("data/day1.txt")
    highest_calories = 0
    count = 0
    for line in file_input:
        if line == '\n':
            if count > highest_calories:
                highest_calories = count
            count = 0
        else:
            calories = int(line)
            count += calories

    print(highest_calories)


def top_three_highest():
    file_input = open("data/day1.txt")
    calorie_list = []
    count = 0
    for line in file_input:
        if line == '\n':
            calorie_list.append(count)
            count = 0
        else:
            calories = int(line)
            count += calories
    calorie_list.sort()
    print(int(calorie_list[-1] + calorie_list[-2] + calorie_list[-3]))


find_highest_calories()
top_three_highest()
