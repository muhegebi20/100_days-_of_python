# rock wins sci
# sci wins paper
# pap wins rock
import random
print("what do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")


rock = '''
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
scissor = '''
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
paper = '''
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
game = [paper, scissor, rock]
while True:
    user_input = int(input(": "))
    comp_play = random.randint(0,2)
    print(f"computer: {game[comp_play]}")
    print(f"you: {game[user_input]}")
    if user_input == comp_play:
        continue;
    elif (user_input==1 and comp_play==2) or (user_input==0 and comp_play == 1) or (comp_play==0 and user_input==2):
        print("computer wins!")
        break;
    elif (user_input==0 and comp_play==2) or (user_input==1 and comp_play==0) or (user_input==2 and comp_play==1):
        print("you win")
        break;