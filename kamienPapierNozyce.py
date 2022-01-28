import random, sys

loses = 0
wins = 0
ties = 0

#k=1, p=2, n=3

while True:
    print("choose k, p, n or q")
    choice = input()
    mychoice = random.randint(1, 3)
    if choice == "k":
        if mychoice == 1:
            print("tie!")
            ties=ties+1
        if mychoice ==2:
            print("you lost!")
            loses=loses+1
        if mychoice ==3:
            print("you win!")
            wins =wins+1
    elif choice == "p":
        if mychoice == 1:
            print("you win!")
            wins=wins+1
        if mychoice ==2:
            print("tie!")
            ties=ties+1
        if mychoice ==3:
            print("you lost!")
            loses = loses+1
    elif choice == "n":
        if mychoice == 1:
            print("you lost!")
            loses = loses + 1
        if mychoice == 2:
            print("you win!")
            wins = wins + 1
        if mychoice == 3:
            print("tie!")
            ties = ties+1
    elif choice== "q":
        sys.exit()
    else:
        print("wrong letter, choose again!")
    if mychoice == 1:
        mychoice="k"
    elif mychoice ==2:
        mychoice="p"
    elif mychoice==3:
        mychoice="n"
    print("my choice for this game was: ", mychoice)
    print("results: wins: ", wins, " loses: ", loses, " ties: ", ties)
    print("------------------------------------------------------")