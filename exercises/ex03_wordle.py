"""Exercise 3 - Wordle"""

__author__ = "730646393"


def input_guess(word_length: int) -> str:
    """prompt user to enter a guess and continue prompting them until they provide a guess of the correct length"""
    word: str = input(
        f"Enter a {word_length}-character word: "
    )  # f allows me not to have to concatenate strings
    while len(word) != word_length:
        word = input(
            f"That wasn't {word_length} chars! Try again: "
        )  # don't need to print, input function already prints for you
    return word


def contains_char(word: str, letter_guess: str) -> bool:
    """test the index of the word to see if it matches the guessed letter. If a match is found, the function returns True. If not, return false."""
    assert len(letter_guess) == 1
    i: int = 0
    while i < len(word):
        if word[i] == letter_guess:
            return True
        i += 1
    return False


def emojified(user_guess: str, word: str) -> str:
    """compare user_guess and word of equal length and return a string composed of emojis"""
    assert len(user_guess) == len(word)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    i: int = 0
    result: str = ""
    while i < len(word):
        if word[i] == user_guess[i]:
            result += GREEN_BOX
        elif (
            word[i] != user_guess[i] and contains_char(word, user_guess[i]) == True
        ):  # if index of guess is not equal to index of word AND the word contains index of guess
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
        i += 1
    return result


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    i: int = 0
    while i < 6:  # 6 TURNS
        print(f"=== Turn {i+1}/6 ===")
        guess: str = input_guess(
            len(secret)
        )  # don't need to rewrite the function, already have function existing, use the input_guess function
        print(emojified(guess, secret))
        if guess == secret:
            print(f"You won in {i+1}/6 turns!")
            i = 6
        elif (
            guess != secret and i < 5
        ):  # if user has not guessed the secret word and it is not the last turn yet, continue the loop
            i += 1
        elif (
            guess != secret and i == 5
        ):  # if user has not guessed the secret word and it is the last/6th turn, stop the loop
            print("X/6 - Sorry, try again tomorrow!")
            i += 1


if __name__ == "__main__":
    main("codes")
