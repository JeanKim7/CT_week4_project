from blackjack import BlackJack

def play_blackjack():
    game = BlackJack()

    print("Welcome to Jean's Casino! Let's play some blackjack!")
    
    while True:
        game.cash_in()
        game.shuffle_deal()

        options = input("What would you like to do? (1. Hit 2. Stand 3. Quit) ")
        while options not in ['1', '2', '3']:
            print("Please enter 1, 2 or 3 only!")
            options = input("What would you like to do? (1. Hit 2. Stand 3. Quit) ")
        if options == '1':
            game.hit_player()
        elif options == '2':
            game.stand()
        elif options == '3':
            break

    print("Thanks for joining us at our casino! Have a good day and hope to see you again :)")
            

play_blackjack()