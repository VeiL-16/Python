import random
rock=("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
paper=("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
scissors=("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
choice=int(input("enter 1 for rock 2 for paper and 3 for scissors"))
comp=random.randint(1,3)
if choice==1:
    print("your choice is rock")
    print(rock)
    if comp==1:
        print("comp choice is rock")
        print(rock)
        print("tie no wins")
    elif comp==2:
        print("comp choice is paper")
        print(paper)
        print("comp won")
    elif comp==3:
        print("comp choice is scissors")
        print(scissors)
        print("you won")
elif choice==2:
    print("your choice is paper")
    print(paper)
    if comp == 1:
        print("comp choice is rock")
        print(rock)
        print("you won")
    elif comp == 2:
        print("comp choice is paper")
        print(paper)
        print("tie no wins")
    elif comp == 3:
        print("comp choice is scissors")
        print(scissors)
        print("comp won")
elif choice==3:
    print("your choice is scissors")
    print(scissors)
    if comp == 1:
        print("comp choice is rock")
        print(rock)
        print("comp wins")
    elif comp == 2:
        print("comp choice is paper")
        print(paper)
        print("you won")
    elif comp == 3:
        print("comp choice is scissors")
        print(scissors)
        print("tie no wins")
