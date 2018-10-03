no_holes = ['C', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
            'M', 'N', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
one_hole = ['A', 'D', 'O', 'P', 'Q', 'R']
two_holes = ['B']

input_string = input()
holes = 0

for character in input_string:
    if character in one_hole:
        holes += 1
    elif character in two_holes:
        holes += 2

print(holes)
