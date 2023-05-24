import sys 
from time import sleep
DASHES = 25
def main():
    start()

#------------------------PLAY AGAIN -------------------------
def play_again():
    print("\nDo you want to play again? (y or n)")

    answer = input (">").lower()

    if "y" in answer:
        start()

    else:
        sys.exit()

#------------------------- GAME OVER ---------------------------
def game_over(reason):
    print ("\n" + reason)
    print ("Game over!")
    play_again()

#------------------------- START -----------------------
def start():
    print(DASHES * "-")
    print("Welcome to TMRs")
    print("The Maf Runs")
    print(DASHES * "-")
    print("You are regular guy with a regular life but something happen today.")
    sleep(0.5)
    print("Today you saw a crime from ome one of the mafia tha is fightinh for territory")
    sleep(0.5)
    print("one of the guys saw and asks you if you want to joing them")
    print("Do you aswer yeas or no? (y and n)")

    #Convert the asnwer to lower case 
    answer = input ("> ").lower()

    #Game structure
    if "y" in answer:
        situation1()
    elif "n" in answer:
        game_over("You receibe a bullet in betwen your eyes you are collateral damage")
    else:
        game_over("You should learn to type or read")




#----------------------- SITUATION 1 ---------------------
def situation1():
    print("One of the guys look at you in a curios way.")
    sleep(0.5)
    print("They asks you if you want to go with them right away")
    sleep(1)
    print("Are you going with them?(y or n)")

    #Convert the asnwer to lower case 
    answer = input ("> ").lower()

    #Game structure
    if "y" in answer:
        situation2()
    elif "n" in answer:
        game_over("You receibe a bullet in betwen your eyes you are collateral damage")
    else:
        game_over("You should learn to type or read")




#------------------------ SITUATION 2 -----------------------------
def situation2():
    print("They have two cars")
    print("There's a BMW M5 and one you have never seen in your life")
    print("One of those is from the hitman the other is from the mafia boss")
    sleep(1.5)
    print("Which car do you choose?")
    print("Left for BMW right for the other one. (l or r)")

    #Convert the asnwer to lower case 
    answer = input ("> ").lower()

    #Game structure
    if "l" in answer:
        situation3()
    elif "r" in answer:
        game_over("You got into the hitmas car he killed you.")
    else:
        game_over("You should learn to type or read")



#--------------------------- SITUATION 3 -------------------------------
def situation3():
    print("The mafie boss took you to a house.")
    sleep(0.5)
    print("He shows you around.")
    print("The mafia boss asks you to sell drugs for him.")
    print("Do yoy accept or not? (y or n)")

    #Convert the asnwer to lower case 
    answer = input ("> ").lower()

    #Game structure
    if "y" in answer:
        situation4b()
    elif "n" in answer:
        situation4()
    else:
        game_over("You should learn to type or read")




#------------------------------- SITUATION 4 ------------------------
def situation4():
    print("The mafia boss takes you to your house.")
    print("He explains that they are going to be watching you.")
    sleep (4)
    print("Months later a judge call you to be witness in a trial")
    sleep(2)
    print("In the trial they ask you if you could see who did it.")
    sleep(3)
    print("Are you going snitch on the boss? (y or n)")

    #Convert the asnwer to lower case 
    answer = input ("> ").lower()

    #Game structure
    if "y" in answer:
        game_over("Mafia killed you.")
    elif "n" in answer:
        jail()
    else:
        game_over("You should learn to type or read")




#------------------------------- SITUATION 4 B ----------------------
def situation4b():
    print("You take 5k worth of drugs with you")
    sleep (0.5)
    print("Next week you take 10k")
    sleep (0.5)
    print("You realize how profitable the bussniss is.")
    sleep (0.5)
    print("Do you want to get more involved? (y or n)")

    #Convert the asnwer to lower case 
    answer = input ("> ").lower()

    #Game structure
    if "y" in answer:
        bussiness()
    elif "n" in answer:
        game_over("You become a simple drug sellers you get killed in 3 months")
    else:
        game_over("You should learn to type or read")




#------------------------------ JAIL -------------------------------- 
def jail():
    print("The jury find out you knew and didn't snith on the boss")
    sleep (0.5)
    print("You go to prison")
    sleep(4)
    print("One week later you the boss goes to see you.")
    print("He gets you out of prision and give you 5k.")
    sleep(7)
    game_over("The family of the victims hire a hitman and killed you.")



#-------------------------------- BUSSINESS -----------------------
def bussiness():
    print("You go and talk with the boss that at this pooint is your friend.")
    sleep (0.5)
    print("You ask him if you can go up in the food chain")
    sleep (3)
    print("The boss agree with you")
    sleep (0.5)
    print("Do you want to go money laundry or to control the sellers in you area.(m or a)")

    #Convert the asnwer to lower case 
    answer = input ("> ").lower()

    #Game structure
    if "m" in answer:
        moneylaundry()
    elif "a" in answer:
        controlsellers()
    else:
        game_over("You should learn to type or read")


#---------------------- MONEY LAUNDRY ----------------------------
def moneylaundry():
    print("You go to the other part of the bussiness.")
    sleep (0.5)
    print("The acountant says that he needs to use your bank account")
    sleep (0.5)
    print("He asks how much money are you willing to pass through your account.")
    sleep (0.5)
    print("More than 25k monthly or less? (m or l)")

    #Convert the asnwer to lower case 
    answer = input ("> ").lower()

    #Game structure
    if "m" in answer:
        game_over("The bank realize your fraud and go to prison")
    elif "l" in answer:
        moneymaker()
    else:
        game_over("You should learn to type or read")



#----------------------- CONTROL AREA SELLERS -----------------------------
def controlsellers():
    print("You start having a lot of success")
    sleep(3)
    print("Everyone respects you")
    sleep(3)
    print("And you and your family have a good life")
    sleep(5)
    game_over("Other gang killed you in the fight for territory.")



#------------------------ MONEY MAKER --------------------------
def moneymaker():
    print("You start making approximately 280k a year")
    print("You have all you dreamedd for as a child and you don't work anymore")
    sleep(5)
    print("You have more than 20 million in investments")
    print("Do you want out or you want more? (o or m)")

    #Convert the asnwer to lower case 
    answer = input ("> ").lower()

    #Game structure
    if "m" in answer:
        game_over("You are too gredy and the FBI discover you and the whole organization")
    elif "o" in answer:
        happylife()
    else:
        game_over("You should learn to type or read")



#------------------------------ HAPPY LIFE ----------------------------
def happylife():
    print("You can live with all your investments")
    print("You have all the money you need and a mafia boos friend.")
    print("You both eat regularly")
    sleep(7)
    youwin()


#------------------------------ YOU WIN ----------------------------
def youwin():
    print("Congrats you finish life in cheat mode")
    play_again()



#-------------------------- GAME START -------------------------
    # If a standalone program, call the main function 
    # Else, use as a module
if __name__=="__main__":
    main()