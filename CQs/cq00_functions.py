"""Challenge Question"""

__author__ = "730646393"


def mimic(message: str) -> str:
    """Takes input and repeats it back to you"""
    return message


def main() -> None:
    """Pulls together functions. Print result of calling mimic"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    """conditional statement. When runnin program in "Run" tab, the indented code will be evaluated. When loading program in REPLY of "Interact" tab, the code will not be run"""
    main()
