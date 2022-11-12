i=1
print("\nYOU HAVE TO GUESS THE NUMBER FROM 1 TO 10\n")
print("YOU HAVE 3 ATTEMPTS")
while i<=3:
    i+=1
    a = int(input("Guess the number :"))
    if a==5:
        print("Congratulations....You win !!")
        break
    elif a>=7:
        print("A little lower....")
    elif a<7 and a>5:
        print("Very close!!")
    elif a<5:
        print("A little bit bigger....")
    elif a>3 and a<5:
        print("Very close!!")

else:
    print("Better luck next time")