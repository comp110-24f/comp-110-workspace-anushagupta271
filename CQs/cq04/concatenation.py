"""Challenge Question 4 - concatentation"""

__author__ = "730646393"


def concat(input1=str, input2=str) -> str:
    """returns the concatenation of the 2 input strings"""
    x: str = ""
    x = input1 + input2
    return x


word1: str = "happy"
word2: str = "tuesday"
print(concat(word1, word2))

if __name__ == "__main__":
    concat(word1, word2)
