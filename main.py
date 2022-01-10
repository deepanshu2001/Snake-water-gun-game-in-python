import random

def gameWin(comp,you):
    if comp==you:
        return None
    elif comp=="s":
        if you=='w':
            return False
        if you=='g':
            return True
    elif comp=='w':
        if you=='s':
            return True
        if you=='g':
            return False

    elif comp=='g':
        if you=='s':
            return False
        if you=='w':
            return True

print("Computers Turn :Snake(s) Water(w) Gun(g) ?")
randno=random.randint(1,3)
if randno==1:
    comp='s'
if randno==2:
    comp='w'
if randno==3:
    comp='g'

you=input("Your Turn :Snake(s) Water(w) Gun(g) ?")

a=gameWin(comp,you)

print(f"computer chose {comp}")
print(f"You choose {you}")

if a==None:
    print("The game is tied")
elif a:
    print("You Win !")
else:
    print("You Lose !")
