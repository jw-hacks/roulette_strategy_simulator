import random

bankroll = 0
all_numbers = ['00',0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
red = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35]
black = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36]
green = ['00', 0]
left_column = [3,6,9,12,15,18,21,24,27,30,33,36]
middle_column = [2,5,8,11,14,17,20,23,26,29,32,35]
right_column = [1,4,7,10,13,16,19,22,25,28,31,34]

def spin():
    result = random.choice(all_numbers)
    #print('The wheel landed on', result)
    return result

def three_two():
    spins_completed = 0
    global funds
    while spins_completed < spins:
        if funds >= (unit * 5):
            result = spin()
            if result in black and left_column:
                funds += (unit * 7)
                #print('+7 ' + 'funds is now:', funds)
            elif result in black:
                funds += (unit)
                #print('+1 ' + 'funds is now:', funds)
            elif result in left_column:
                funds += (unit)
                #print('+1 ' + 'funds is now:', funds)
            else:
                funds -= (unit * 5)
                #print('-5 ' + 'funds is now:', funds)
        else:
            #print("Sorry, not enough funds")
            pass
        spins_completed += 1

print('Welcome to Roulette Strategy Simulator!')
bankroll = int(input('What is your starting bankroll? (e.g. for $500 type 500): '))
funds = int(input('How much money per game? '))
unit = int(input('\nHow much do you want 1 unit to be: '))
while True:
    choice = input('\nSelect from the following strategies: \n 1. 3/2\n')
    if choice == '1':
        games_completed = 1
        wins = 0
        losses = 0
        games = int(input('\nHow many games do you want to simulate? \n'))
        spins = int(input('\nHow many spins per game?\n'))
        game_funds = funds
        while games_completed <= games:
            bankroll -= funds
            three_two()
            profit = funds - game_funds
            print('Game ' + str(games_completed) + ' profit is ' + str(profit))
            games_completed += 1
            if funds > game_funds:
                wins += 1
            elif funds == game_funds:
                pass
            else:
                losses += 1
            bankroll += funds
            print('Bankroll = ',bankroll)
            funds = game_funds
        win_percentage = 100 * float(wins) / float(games)
        print('Wins = ',wins)
        print('Losses = ',losses)
        print('Win percentage: ' + str(win_percentage) + '%')
        print('Bankroll total is: ',bankroll)
