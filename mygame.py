import random
def guessnumber():
    r = int(input("Enter the range:"))
    #computer = random.randint(1,r)
    b = (1,r)
    computer = random.choice(b)
    me = int(input("Enter your choice:"))
    if me == computer:
        print("You won")
    else:
        print(computer)
        print("You loose, Try again")


def RPS():   
    Computer_choice = ["rock","paper","scissors"]
    import random
    X= random.randint(0,2)
    Computer = Computer_choice[X]
    Ok = input("Enter your choice = Rock,Paper & Scissors: ")
    Choice = Ok.lower()
    if Choice=="rock" and Computer=="rock":
        print("Computer Choice=",Computer)
        print("It is a Draw😉")
    elif Choice=="rock" and Computer=="paper":
        print("Computer Choice=",Computer)
        print("You lose 😔 ")
    elif Choice=="rock" and Computer=="scissors":
        print("Computer Choice=",Computer)
        print("You win 🎉")
    elif Choice=="paper" and Computer=="rock":
        print("Computer Choice=",Computer) 
        print("You win")
    elif Choice=="paper" and Computer=="paper":
        print("Computer Choice=",Computer)
        print("It is a Draw")
    elif Choice=="paper" and Computer=="scissors":
        print("Computer Choice=",Computer)
        print("You lose")
    elif Choice=="scissors" and Computer=="rock":
        print("Computer Choice=",Computer)
        print("You lose")
    elif Choice=="scissors" and Computer=="paper":
        print("Computer Choice=",Computer)
        print("You win")
    elif Choice=="scissors" and Computer=="scissors":
        print("Computer Choice=",Computer)
        print("It is a Draw")    
    else:
        print("Invalid Choice")