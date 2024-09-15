"""Figuring out how much I need for a cozy tea party!"""

__author__ = "730489841"


# Main Function which calls all the functions
def main_planner(guests: int) -> None:
    """The function that brings together all the functions."""
    tea = tea_bags(guests)
    treat = treats(guests)
    total = cost(tea, treat)
    print("A Cozy Tea Party for " + str(guests) + " People!")
    # The first line shown when function is called

    print("Tea bags: " + str(tea))
    print("Treats: " + str(treat))
    print("Cost: $" + str(total))
    # Prints the functions to display the prices and ultimately the costs


# Defines the function for the price of tea bags based on the number of guests
def tea_bags(people: int) -> int:
    """To figure out how many tea bags to buy based on the number of guests."""
    return people * 2


# Defines the function for the price of treats based off of the number of tea bags
def treats(people: int) -> int:
    """To determine amount of treats needed based on number of guests."""
    return int(tea_bags(people=people) * 1.5)


# Defines the function for the total costs of tea bags and treats
def cost(tea_count: int, treat_count: int) -> float:
    """To determine the cost of all treats and tea bags."""
    return tea_count * 0.50 + treat_count * 0.75


# Appears on the Run tab of Trailhead that asks the user to input the amount of guests that will be attending their party
if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your party? ")))
