colours = ["Spade", "Clubs", "Hearts", "Diamond"]
quadeck = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
deck = [x+ " " +y for x in colours for y in quadeck]

values = {"Ace":None, "Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10, "Jack":10, "Queen":10, "King":10}

def choose():
    a = deck.pop()
    return a

def check():
    g = 0
    if sum > 21:
        if i == 0:
            print("Player lost")
            g = 1
        elif i == 1:
            print("Player won")
            g = 1
    elif sum <= 21:
        print("Sum is {}".format(sum))
    return g


import random

random.shuffle(deck)

#print(deck)
while True:
    balance = int(input("Please enter your chip balance.\n"))
    bet = int(input("Please enter your bet.\n"))
    if bet <= balance:
        break
    else:
        print("Bet exceeds your current balance. Please re-enter your balance and bet.\n")
        continue

again = None

while True:
    deck = [x+ " " +y for x in colours for y in quadeck]
    random.shuffle(deck)
    player = []
    dealer = []
    status = 'Won'
    dealer_sum = None
    player_sum = None
    a, b = None, None
    for _ in range(2):
        a = deck.pop()
        player.append(a)
    for _ in range(2):
        b = deck.pop()
        dealer.append(b)

    if again == 'y':
        while True:
            if balance == 0:
                print("You are out of chips.")
                exit()
            print("Your balance is {}".format(balance))
            bet = int(input("Please enter your bet.\n"))
            print(f" Your balance is {balance} and you bet {bet}")
            if bet <= balance:
                break
            else:
                print("Bet exceeds your current balance. Please re-enter your balance and bet.\n")
                continue

    for _ in player:
        print( _, end = "    " )

    print("\nDealers card ",dealer[0])

    i = 0
    while i < 2:
        sum = 0
        if i == 0:
            user = player
        elif i == 1:
            user = dealer
        for _ in user:
            #if i == 1:
            #    for _ in dealer:
            #        print(_, end= "    ")
            #    print()
            if _.split()[1] != "Ace":
                sum += values[_.split()[1]]
            elif _.split()[1] == "Ace":
                print("You got an Ace.")
                while True:
                    ace = int(input("Enter 1 or 11 as value of ace.\n"))
                    if ace == 1 or ace == 11:
                        sum += ace
                        break
                    else:
                        print("Ace value incorrect. Re-enter value.\n")
        print("Sum is {}".format(sum))


        while True:
            call = input("Press h if you want to hit, else press s to stand.\n")
            if call == 'h':
                k = choose()
                print(k)
                if k.split()[1] != "Ace":
                    sum += values[k.split()[1]]
                elif k.split()[1] == "Ace":
                    print("You got an Ace.")
                    while True:
                        ace = int(input("Enter 1 or 11 as value of ace.\n"))
                        if ace == 1 or ace == 11:
                            sum += ace
                            break
                        else:
                            print("Ace value incorrect. Re-enter value.\n")
                print("Sum is {}".format(sum))

                user.append(k)
                if i == 0:
                    player.append(k)
                elif i == 1:
                    dealer.append(k)
            elif call == 's':
                if i == 1:
                    dealer_sum = sum
                    if dealer_sum > player_sum and dealer_sum <= 21:
                        status = 'Lost'
                        break
                break

            g = check()

            if sum > 21 and i == 0:
                i += 1
                status = 'Lost'
                break

            if i == 0:
                player_sum = sum

            if i == 1:
                dealer_sum = sum
                if dealer_sum > player_sum and dealer_sum <= 21:
                    status = 'Lost'
                    break

            if g == 1:
                break

        try:
            if dealer_sum > player_sum:
                status = 'Lost'
            elif dealer_sum == player_sum:
                status = 'Draw'
            else:
                status = 'Won'
        except:
            pass
        i += 1





    if status == 'Won':
        balance += bet
    elif status == 'Lost':
        balance -= bet

    again = input("Do you want to play again. Press y to play again else press any other key.\n")
    if again == "y":
        print("\n\n\n\n\n")
        continue
    else:
        break
