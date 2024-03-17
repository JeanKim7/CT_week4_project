from blackjack import BlackJack

# I didn't know it was called staying, and called it standing :(, please treat standing as staying whenever you see it

def play_blackjack():
    game = BlackJack()

    print("Welcome to Jean's Casino! Let's play some blackjack!")
    game.cash_in()

    while True:
        game.shuffle_deal()
        while True:
            # end loop if player gets 21 on initial 2 cards from shuffle_deal
            if game.player.count == 0:
                break
            options = input("What would you like to do? (1. Hit 2. Stand 3. Quit) ")
            # make sure user inputs correct option
            while options not in ['1', '2', '3']:
                print("Please enter 1, 2 or 3 only!")
                options = input("What would you like to do? (1. Hit 2. Stand 3. Quit) ")
            if options == '1':
                game.hit_player()
                # end game if game resets after winning or losing
                if game.player.count == 0:
                    break
            # end game after standing
            elif options == '2':
                game.stand()
                break
            # quit
            elif options == '3':
                break
        nextoption = input("What would you like to do next? (1. Play again 2. Quit) ")
        while nextoption not in ['1', '2']:
            print("Please enter 1 or 2 only!")
            nextoption = input("What would you like to do? (1. Play again 2. Quit) ")
        # Give option to cash in for more money
        if nextoption == '1':
            cash_in_again = input("Would you like to cash in for more money? (1. Yes 2. No)")
            while cash_in_again not in ['1', '2']:
                print("Please enter 1 or 2 only!")
                cash_in_again = input("Would you like to cash in for more money? (1. Yes 2. No) ")
            if cash_in_again == '1':
                amount = input("How much would you like to cash in? $")
                game.player.money += float(amount)
                # end game if they have no money
                if game.player.money <= 0:
                    print("You're broke! You can't play!")
                    break
            elif cash_in_again == '2':
                # end game if they don;t cash in and they have no money
                if game.player.money <= 0:
                    print("You're broke! You can't play!")
                    break
        elif nextoption == '2':
            break
                

    print("Thanks for joining us at our casino! Have a good day and hope to see you again :)")
            

play_blackjack()