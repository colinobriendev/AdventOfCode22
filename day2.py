with open('data/day2.txt', 'r') as file:
    data = [line.strip().replace(' ', '') for line in file]

# A: Rock 1 pt, B: Paper 2 pts, C: Scissors 3 pts. X: Lose, Y: tie 3 pts, Z: Win 6 pts
first = sum({'AX': 4, 'AY': 8, 'AZ': 3, 'BX': 1, 'BY': 5, 'BZ': 9, 'CX': 7, 'CY': 2, 'CZ': 6}[round] for round in data)
second = sum({'AX': 3, 'AY': 4, 'AZ': 8, 'BX': 1, 'BY': 5, 'BZ': 9, 'CX': 2, 'CY': 6, 'CZ': 7}[round] for round in data)

print('First part: ', first)
print('Second part: ', second)
