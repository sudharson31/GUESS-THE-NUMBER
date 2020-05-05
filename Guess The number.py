import random

secret = random.randrange(1,50)
print(secret)

guess = 0
tries = 0
while guess != secret:
    guess = int(input("Enter the number 1 to 50: "))
    tries += 1
    if guess>secret:
        print("Too High Guess Again")
    elif guess<secret:
        print("Too Low Guess Again")
    
print("You Win correctly Guess!!!" "\n",tries,"times you trying")
