import random

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

word_list = ["cat", "rat", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)
live = 0
game_over = False
correct_letters = []
while not game_over:
    display = ""
    guess = input("\nguess the letter: ").lower()
    if guess not in chosen_word:
        live+=1
    for letter in chosen_word:
        if guess == letter:
           display+= guess
           correct_letters.append(letter)
        elif letter in correct_letters:
            display+=letter
        else:
            display+="_"
    print(display)
    print(HANGMANPICS[live])
    if "_" not in display:
        if live != 6:
            game_over = True
        print("YOu win")
    if live == 6:
        print("You lose!")
