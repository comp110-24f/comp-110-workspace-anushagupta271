"""Exercise 6 - dictionary"""

__author__ = "730646393"


def invert(dict_input: dict[str, str]) -> dict[str, str]:
    """invert the keys and values of dict"""
    inverted_dict: dict[str, str] = {}
    for key in dict_input:
        value = dict_input[key]
        if value in inverted_dict:
            raise KeyError("more than one of the same key")
        inverted_dict[value] = key
    return inverted_dict


def count(list: list[str]) -> dict[str, int]:
    new_dict: dict[str, int] = {}
    for item in list:
        if item in new_dict:
            new_dict[item] += 1
        else:
            new_dict[item] = 1
    return new_dict


def favorite_color(dict_input: dict[str, str]) -> str:
    """returns the favorite color that appears most frequently in input dict"""
    colors: list[str] = []
    for value in dict_input.values():
        colors.append(value)
    # print(colors)
    # i: int = 0
    favorite: str = ""
    frequency_of_colors: dict[str, int] = count(colors)
    # print(frequency_of_colors)
    # while i < len(colors):
    #     color = colors[i]
    #     frequency_of_colors[color] = 1
    #     if color in frequency_of_colors:
    #         frequency_of_colors[color] += 1
    max_count: int = 0
    for color in frequency_of_colors:
        if frequency_of_colors[color] >= max_count:
            favorite = color
            # print(favorite)
            # print(max_count)
            max_count = frequency_of_colors[color]
            # print(max_count)
    return favorite


def alphabetizer(list: list[str]) -> dict[str, list[str]]:
    dict: dict[str, list[str]] = {}
    for word in list:
        first_letter: str = word[0].lower()
        # letter_list: list[str] = []
        if first_letter not in dict:
            dict[first_letter] = []
        dict[first_letter].append(word)
    return dict


def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> None:
    """update the input dictionary with which students attended on which day"""
    if day not in attendance:
        attendance[day] = [student]
    if student not in attendance[day]:
        attendance[day].append(student)
    else:
        attendance[day] = [student]
