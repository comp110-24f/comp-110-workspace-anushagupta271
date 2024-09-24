"""Tea Party Exercise 1!"""

__author__ = "730646393"


def main_planner(guests: int) -> None:
    """ "calls each function and prints output to the screen"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))


# I had no trouble with this, very simple!


def tea_bags(people: int) -> int:
    """Everyone at the tea party will drink 2 cups of tea"""
    return people * 2


def treats(people: int) -> int:
    """Number of treats needed based on number of teas guests are expecting to drink"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """cost of tea bags and treats combined"""
    return tea_count * 0.50 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
# at the bottom bc it needs to call a defined fn
