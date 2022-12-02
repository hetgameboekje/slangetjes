import random


def play_game():    
    totaalchips = 10
    winchips = 35
    inzet = 1
    print("-=-=-=-=-=-=-=-=-=-=-")
    print("je hebt", totaalchips, "chips totaal!")
    print("Je kan 35 chips winnen, Totaal is dit", totaalchips + winchips, "chips")
    print("-=-=-=-=-=-=-=-=-=-=-")

    for i in range(totaalchips):
            if totaalchips < 0:
                break
            rollguess = random.randint(1, 2)
            inzet = int(input('hoeveel chips wil je inzetten? '))
            if inzet > totaalchips or totaalchips < 0: 
                print("Je hebt niet genoeg chips!")
                break
            roll = int(input('Place your bet, 1-36: '))
            print('-=-=-=-=-=-=-=-=-=-=-')
            if roll == rollguess:
                    print("Je hebt", inzet, "chips ingezet!")
                    totaalchips = (totaalchips + (winchips*inzet))
                    print("Gefeliciteerd! je succesvol geraden, je hebt", totaalchips, "chips totaal!")
            else:
                    print("Je hebt", inzet, "chips ingezet!")
                    print("Spel rolde:", rollguess)
                    totaalchips = (totaalchips - inzet)
                    print("je hebt verloren, je hebt", totaalchips, "chips totaal! ")


              
def play_again():
    if input("Do you want to play again? (y/n)") == "y":
        play_game()
        play_again()
    else:
        print("Thanks for playing!")
        exit()
    

while True:
    play_game()
    if not play_again(): break

print ("OK Goodbye...")