import random
num=random.randint(1,100)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
choice=input("Choose a difficulty. Type 'easy' or 'hard':").lower()
def easy(num):
    attempts=10
    print("you have 10 attempts")
    while attempts!=0:
        my_choice=int(input("make a guess"))
        if my_choice ==num:
            print(f"the ans is {num} you won")
            return ""
        elif my_choice<num:
            print("too low")
            attempts-=1
        elif my_choice>num:
            print("too high")
            attempts-=1
        elif attempts==0:
            print("ran out of guesses")


def hard(num):
    attempts = 5
    print("you have  attempts")
    while attempts != 0:
        my_choice = int(input("make a guess"))
        if my_choice == num:
            print(f"the ans is {num} you won")
            return ""
        elif my_choice < num:
            print("too low")
            attempts -= 1
        elif my_choice > num:
            print("too high")
            attempts -= 1
        elif attempts == 0:
            print("ran out of guesses")


if choice=="easy":
    easy(num)
elif choice=="hard":
    hard(num)