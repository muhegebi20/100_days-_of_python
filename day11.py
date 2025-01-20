import random

logo = '''
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_|
      |  \/ K|                            _/ |                
      '------'                           |__/  

      '''
def blackJack():
    print(logo)
    wanna_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if wanna_play == 'n':
        return
    cards = [10, 4, 6, 11, 7, 8, 9, 5, 2, 3, 10, 10, 10]
    first = random.choice(cards)
    second = random.choice(cards)
    c_card = random.choice(cards)
    total = 0
    c_total = 0
    play = True
    total = first + second
    while play:
        print(f"\tYour cards: [{first},{second}]",end=", ")
        print(f"Current score: {total}")
        print(f"\tComputer's first card: {c_card} + ?")
        if total == 21:
            print("You win")
            blackJack()
        get_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if get_card == 'y':
            if total > 21:
                print("Bust!!!")
            elif total < 21:
                total +=random.choice(cards)
                if total > 21:
                    print("Bust!!!")
                    print(f"\tYour cards: [{first},{second}]",end=", ")
                    print(f"Current score: {total}")
                    blackJack()
            else:
                print("You win!!!")
        else:
            for _ in range(random.randint(1,2)):
                    c_total += random.choice(cards)
            if c_total == total:
                print("Push")
                blackJack()
            elif total < c_total < 21:
                print("Computer wins")
                print("You lose")
            elif c_total > 21:
                print("You win")
            else:
                print("You win")
            play = False
    print(f"Your score:--> {total}")
    print(f"Computer Scroe:--> {c_total}")
    blackJack()

        

blackJack()