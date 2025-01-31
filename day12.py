import random
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose difficulty. Type 'easy' or 'hard': ").strip().lower()
num = random.randint(1, 100)
if difficulty == 'hard':
    attempt = 5
elif difficulty == 'easy':
    attempt = 10
else:
    difficulty = input("Choose difficulty. Type 'easy' or 'hard': ").strip().lower()
while True:
    if attempt == 0:
        print("You run out of attempts.\nYou Lose!")
        print(f"The number was: {num}")
        break
    print(f"You have {attempt} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess > 101 or guess <=0:
        guess = int(input("Make a guess: "))
    if guess == num:
        print(f"You got it. The number is {num}")
        break
    elif guess > num:
        print("Too high.")
    else:
        print("Too low.")
    attempt -=1
    print("Guess agian.\n")