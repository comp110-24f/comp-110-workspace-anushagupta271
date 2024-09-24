"""Exercise 2 - Chardle"""

__author__ = "730646393"


def input_word() -> str:
    """checks if inputted word has length of 5"""
    word: str = input("Enter a 5-character word: ")
    if len(word) == 5:
        return word
    else:
        print("Error: Word must contain 5 characters.")
        exit()
        # no longer return word just exit


def input_letter() -> str:
    """checks if inputted letter has length of 1"""
    letter: str = input("Enter a single character: ")
    if len(letter) == 1:
        return letter
    else:
        print("Error: Character must be a single character.")
        exit()
        # no longer return letter just exit


def contains_char(word: str, letter: str) -> None:
    """Checks if inputted word contains the inputted letter"""
    # i: int = 0
    # while i < len(word):
    #     if letter == word[i]:
    # no while loop yet, just a bunch of if statements :(
    count: int = 0
    print("Searching for " + letter + " in " + word)
    if word[0] == letter:
        count = count + 1
        print(letter + " found at index 0")
    if word[1] == letter:
        count = count + 1
        print(letter + " found at index 1")
    if word[2] == letter:
        count = count + 1
        print(letter + " found at index 2")
    if word[3] == letter:
        count = count + 1
        print(letter + " found at index 3")
    if word[4] == letter:
        count = count + 1
        print(letter + " found at index 4")
    if count == 0:  # checks if count is 0
        print("No instances of " + letter + " found in " + word)
    else:  # if count is greater than 0
        print(str(count) + " instances of " + letter + " found in " + word)


def main() -> None:
    """Entry point of the Chardle game, calling other functions to gather user inputs and perform necessary operations"""
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
# at the bottom bc it needs to call a defined fn
