import random

compscore = 0
playscore = 0


def game():
    global compscore, playscore

    while compscore <6 and playscore <6:
        p = random.choice([0,1,2])
        n = int(input("0. for snake\n1. for water\n2. for gun\nEnter your choice:"))
        if n > 2 or n < 0:
            print("Invalid choide")
            return
        
        else:

            if p == n:
                print("It's a draw")

            else:

                if((p==0 and n==2) or (p==1 and n==0) or (p==2 and n==1)):
                    print("You win")
                    playscore += 1

                else:
                    print("You lost")
                    compscore += 1

        
        print(f"Current score is computer : {compscore} \n player: {playscore}")

    if playscore == 5:
        print("Congrats!! You won the game")
    if compscore == 5:
        print("You Lost the game\nPlease try again")
    

game()