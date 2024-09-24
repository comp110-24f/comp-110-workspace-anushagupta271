"""Practice with conditionals"""


def less_than_10(num: int) -> None:
    """Tell me if num is < 10"""
    dub: int = num * 2
    dub = num - 1
    print(dub)
    if num < 10:
        print("Small number")
    else:
        print("Big number")
    print("Have a nice day!")


less_than_10(5)
# less_than_10(11)


# 9/11 practice in class
def get_weather_report() -> str:
    """takes input of weather and gives report based on whether it is rainy/cold or hot"""
    weather: str = input("What is the weather?")
    if weather == "rainy" or weather == "cold":
        print("Bring a jacket")
    elif weather == "hot":
        print("Keep cool out there!")
    else:
        print("I don't recognize the weather.")
    return weather


print(get_weather_report())

# def should_i_eat(hungry: bool) -> None:
#     """Tells me whether or not to eat based on hunger"""
#     if hungry:
#         print("Eat some food")  # then block
#     else:
#         print("Do your COMP 110 HW instead")  # else block
#     print("I'm proud of you")  # either way, be kind to yourself


# should_i_eat(hungry=True)  # if you put print, it'll print the return val which is None


# def check_first_letter(word: str, letter: str) -> str:
#     """Return match if the first chracter of word is letter. Otherwise return no match"""
#     if word[0] == letter:
#         return "match!"
#     else:
#         return "no match!"


# print(check_first_letter("happy", "h"))
# print(check_first_letter("happy", "s"))


# 9/16 while loop lesson
def characters(msg: str) -> None:
    index: int = 0
    while index < len(msg):
        print(msg[index])
        index = index + 1


characters(msg="Howdy")
