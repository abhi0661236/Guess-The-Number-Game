# hey it is very simple and very interesting "guessing game"

import random

sys_num = random.randint(0, 20)


def check(a, b):
    if a > b:
        print("Almost there try to decrease the value \t:o")
    elif a < b:
        print("Almost there try to increase the value \t:o")
    else:
        print("Oh yes! you got the trophy for guessing the number\t:)")


print("Hi there Lets play a game \n I am thinking about a \n number can you guess what is it?")

for number in range(21):
    user_num = int(input("What you guessed ?"))
    if number >= 10:
        print("Game Over")
        break
    elif user_num == sys_num:
        check(user_num, sys_num)
        break
    else:
        check(user_num, sys_num)