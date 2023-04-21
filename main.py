import random


class Game:
    def __init__(self):
        # get the computers choice
        self.computer_opp = self.get_opp_choice()

        # get the user's choice
        self.user_opp = self.get_user_opp()

    def get_computer_opp(self):
        # genereate random number among 1, 2 and 3
        random_number = random.randint(1, 3)

        # choices
        option = {1: 'rock', 2: 'paper', 3: 'scissors'}

        # return the value present at radom_number
        return options[random_number]

    def get_user_pick(self):
        user_pick = input('Enter rock/paper/scissors: ')

        # Converting the user's pick to lowercase and returned it
        return user_pick.lower()
