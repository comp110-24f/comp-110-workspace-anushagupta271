"""Challenge Question 4 - coordinates"""

__author__ = "730646393"


def get_coords(xs: str, ys: str) -> None:
    """print the formatted pairs of each character int he 2 input strings"""
    r: int = 0
    while r < len(xs):
        # print(r)
        c: int = 0
        # need to define c inside first loop but before second loop to make sure value of c resets after first run of 2nd while loop
        while c < len(ys):
            # print(c)
            print("(" + xs[r] + "," + ys[c] + ")")
            c += 1
            # print(c)
        r += 1
