import random


class Game:
    def __init__(self):
        # get the computers choice
        self.computer_opp = self.get_computer_opp()

        # get the user's choice
        self.user_opp = self.get_user_opp()

        # get the result of the game
        self.result = self.get_result()

    def get_computer_opp(self):
        # genereate random number among 1, 2 and 3
        random_number = random.randint(1, 3)

        # choices
        options = {1: 'rock', 2: 'paper', 3: 'scissors'}

        # return the value present at radom_number
        return options[random_number]

    def get_user_opp(self):

        while True:
            user_opp = input('Enter rock/paper/scissors: ')

            # Converting the user's pick to lowercase and returned it
            user_opp = user_opp.lower()

            # if user_opp is either rock or paper or scissors end loop

            if user_opp in ('rock', 'paper', 'scissors'):
                break
            else:
                print('Wrong input!')

        return user_opp

    def get_result(self):
        # condtition for the draw
        if self.computer_opp == self.user_opp:
            return 'draw'

        # condition for the user to win
        elif self.user_opp == 'paper' and self.computer_opp == 'rock':
            return 'Win!!!'
        elif self.user_opp == 'rock' and self.computer_opp == 'scissors':
            return 'Win!!!'
        elif self.user_opp == 'scissors' and self.computer_opp == 'paper':
            return 'Win!!!'

        # In all other condition user lose
        else:
            return 'lose'

    def print_result(self):
        print(f"Computer's Choice: {self.computer_opp}")
        print(f"Your Choice: {self.user_opp}")
        print(f"You {self.result}")


#  created an object of the game class
while True:

    game = Game()
    game.print_result()

    play_again = input('Would you like to play again? (y/n): ')

    if play_again != 'y':
        print('See you soon!')
        break
