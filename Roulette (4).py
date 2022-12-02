import random

totaalchips = 10
winchips = 35
inzet = 1

print("je hebt", totaalchips, "chips totaal!")
print("Je kan 35 chips winnen, Totaal is dit", totaalchips + winchips, "chips")
print("-=-=-=-=-=-=-=-=-=-=-")

for i in range(totaalchips):
        rollguess = random.randint(1, 2)

        inzet = int(input('hoeveel chips wil je inzetten? '))
        if inzet > totaalchips:
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
                
