from will_hit import will_hit


assert will_hit("y = 2x - 5", (0, 0)) == False
assert will_hit("y = -4x + 6", (1, 2)) == True
assert will_hit("y = 2x + 6", (3, 2)) == False
