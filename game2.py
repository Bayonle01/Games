import mygame
print("="*50)
print("="*10,"WELCOME TO GAME","="*10)
print("="*50)
print("Choose from the available game")
while True:
    gamelist="""
                1. Guess Number game
                2. Rock-paper-scissors
                3. Quit
            """
    print(gamelist)
    print("")
    choice = int(input("Enter your choice from 1 - 3: "))
    if choice == 1:
        mygame.guessnumber()
    elif choice == 2:
        mygame.RPS()
    elif choice == 3:
        quit()
