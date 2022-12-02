import random


chips = 10
red = (1,3,5,7,9,12,14,16,18,21,23,25,27,30,32,34,36)
black = (2,4,6,8,10,11,13,15,17,19,20,22,24,26,28,29,31,33,35)
green = 0
even = (2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36)
odd = (1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35)

totaalchips = 10
winchips = 35







def main():
    print('Red = 1')
    print('Black = 2')
    print('Green = 3')
    print('Odd = 4')
    print('Even = 5')
    print('-=-=-=-=-=-=-=-=-=-=-')
    player = int(input('Place your bet, 1-5: '))
    print('-=-=-=-=-=-=-=-=-=-=-')

    roll()
    win_loss()

def roll():
    spin = random.randint(1,36)
    print('Landed on: ',spin)
    print('-=-=-=-=-=-=-=-=-=-=-')

def win_loss():
    if (roll) == red:
        print('You won $.45')
        totaalchips = (totaalchips + winchips)
        print("je hebt", totaalchips, "chips totaal!")
    elif (roll) == black:
        print('You won $.45')
        totaalchips = (totaalchips + winchips)
        print("je hebt", totaalchips, "chips totaal!")
    elif (roll) == green:
        print('You won $5.00')
        totaalchips = (totaalchips + winchips)
        print("je hebt", totaalchips, "chips totaal!")
    elif (roll) == even:
        totaalchips = (totaalchips + winchips)
        print("je hebt", totaalchips, "chips totaal!")
        print('You won $.45')
    elif (roll) == odd:
        totaalchips = (totaalchips + winchips)
        print("je hebt", totaalchips, "chips totaal!")
        print('You won $.45')
    else:
        print('You lost')
        
main()