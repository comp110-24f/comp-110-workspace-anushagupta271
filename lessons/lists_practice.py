"""Basic syntax of lists"""

my_numbers: list[float] = []  # literal
my_numbers: list[float] = list()  # constructor

my_numbers.append(1.5)

print(my_numbers)

game_points: list[int] = [102, 86, 94]
print(game_points)

# subscription notation/indexing
print(game_points[2])
last_game: int = game_points[2]
print(last_game)

# Modifying by index
game_points[1] = 72
print(game_points)

# getting the length
len(game_points)

# removing
game_points.pop(1)


# string analogy
# my_name: str = "" #literal
# my_name: str = str() #constructor
