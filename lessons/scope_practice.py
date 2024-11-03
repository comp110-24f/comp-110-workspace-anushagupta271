def remove_chars(msg: str, char: str) -> str:
    """return a copy of msg with all instances of char removed."""
    copy: str = ""  # Set up empty str to copy values over
    index: int = 0
    while index < len(msg):
        # if the letter is NOT char
        if not (msg[index] == char):  # if msg[index] != char
            # add it to copy
            copy += msg[index]  # copy = copy + msg[index]
        index += 1
    return copy


if __name__ == "__main__":
    print(remove_chars("football", char="o"))
    word: str = "yoyo"
    print(remove_chars(word, "y"))
    print(remove_chars(word, "o"))
