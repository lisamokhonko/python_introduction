#Task #23*
#

import random
from enum import Enum
from enum import IntEnum

Game = IntEnum('Game', 'ROCK PAPPER SCISSORS LIZARD SPOCK')

GREETING_BODY = '\n    '.join(['%d - %s' % (elem.value, elem.name) for elem in Game])
GREETING = '''
Enter data
    %s
    \'q\' for exit: ''' % GREETING_BODY
# ROCK = 0
# PAPPER = 1
# SCISSORS = 2

#print(Game.ROCK.value)

# def code2text(code):
#     if code == Game.ROCK.value:
#         return 'ROCK'
#     elif code == Game.PAPPER.value:
#         return 'PAPPER'
#     elif code == Game.SCISSORS.value:
#         return 'SCISSORS'


def who_is_winner(pc_choice, user_choice):
    if pc_choice == Game.ROCK and user_choice == Game.SCISSORS:
        return False
    if pc_choice == Game.PAPPER and user_choice == Game.ROCK:
        return False
    if pc_choice == Game.SCISSORS and user_choice == Game.PAPPER:
        return False
    if pc_choice == Game.ROCK and user_choice == Game.LIZARD:
        return False
    if pc_choice == Game.LIZARD and user_choice == Game.SPOCK:
        return False
    if pc_choice == Game.SPOCK and user_choice == Game.SCISSORS:
        return False
    if pc_choice == Game.SCISSORS and user_choice == Game.LIZARD:
        return False
    if pc_choice == Game.LIZARD and user_choice == Game.PAPPER:
        return False
    if pc_choice == Game.PAPPER and user_choice == Game.SPOCK:
        return False
    if pc_choice == Game.SPOCK and user_choice == Game.ROCK:
        return False
    return True

#print(who_is_winner(0,2))

def game():

    while True:
        input_data = input(GREETING)
        if input_data == 'q':
            break

        if int(input_data) not in [elem.value for elem in Game]:
            print('Invalid data')
            continue

        # if not Game.ROCK.value <= int(input_data) <= Game.SCISSORS.value:
        #     print('Invalid data')
        #     continue
        pc_choice = random.choice(list(Game))
        user_choice = Game(int(input_data))

        #pc_choice = random.randint(Game.ROCK.value, Game.SCISSORS.value)
        #user_choice = int(input_data)

        print('PC choice: %s' % pc_choice.name)
        if pc_choice == user_choice:
            print('Tie')
        else:
            if who_is_winner(pc_choice, user_choice):
                print('User is winner: %s vs %s' %
                      (pc_choice.name,
                       user_choice.name))
            else:
                print('PC is winner: %s vs %s' %
                      (pc_choice.name,
                       user_choice.name))
game()