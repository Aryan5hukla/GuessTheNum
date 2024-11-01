import random
n = random.randint(1,100)
guess = 1
a = -1
while(a != n) :
    a = int(input("guess the number "))

    if (a<n) :
        print("Higher Number plsss")
        guess += 1 
    elif(a>n) :
        print("Lower Number pls")
        guess += 1 

print(f"You have finally guessed the correct number which is {n} and attempt took by you to guess it are {guess}")