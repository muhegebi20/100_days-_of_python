from celebrities import celebrities
import random
logo = '''
__     ______  
\ \   / / ___| 
 \ \ / /\___ \ 
  \ V /  ___) |
   \_/  |____/ 
'''

def choose_celebrity(i):
    return celebrities[i]

# 1 choose A celebrity
A = celebrities[random.randint(0, len(celebrities)-1)]

# 2 choose B celebrity
score = 0
while True:
    ind = celebrities.index(A)
    ind = (ind+1) % len(celebrities)
    B = choose_celebrity(ind)
# 3 ask who has more follower
    print(f'\n\tName: {A["name"]}\n\tFollower: {A["follower_count"]}\nA--->\tDescription: {A["description"]}\n\tCountry: {A["country"]}')
    print(f"\t{logo}")
    print(f'\n\tName: {B["name"]}\nB--->\tDescription: {B["description"]}\n\tCountry: {A["country"]}')
    userInput = input("\nWho has more followers? Type 'A' or 'B': ").lower()
    while userInput != 'a' and userInput != 'b':
          print("please type 'A' or 'B'")
          userInput = input("\nWho has more followers? Type 'A' or 'B': ").lower()
    if A["follower_count"] < B["follower_count"] and userInput == 'b':
        score+=1
        A = B
    elif A["follower_count"] > B["follower_count"] and userInput == 'a':
                score+=1
                A = B
    else:  
          print(f'Wrong Answer, your score is: {score}')
          print(f'{B["name"]} has {B["follower_count"]} follower')
          break
    print("\n"*20)
    print(f"You're right! Current score: {score}\n")