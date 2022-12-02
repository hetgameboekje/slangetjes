import sys 

print("welkom bij de sinterklaas verlanglijst! Hier kunt u cadeau's invullen dat uw op uw verlanlijst wilt. Als u klaar bent typed u KLAAR!")

for x in range(12):
      cadeau1 = input()
if cadeau1 == "KLAAR!" :
        print(cadeau1) 
        sys.exit()
else:   print("volgende cadeau")   


