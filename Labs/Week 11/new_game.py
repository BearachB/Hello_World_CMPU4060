import random

class Player(object):
    def __init__(self, name="", id=0, win_rate=(0,0), number_of_plays=0.0):
        self.name = name
        self.id = id
        self.win_rate = win_rate # first element is no. of wins, second is losses
        self.number_of_plays = number_of_plays

    def __str__(self):
        return_str = "Name: " + self.name + "\n"
        return_str = "ID: " + str(self.id) + "\n"
        return_str = "Win Rate: " + str(self.win_rate) + "\n"
        return_str = "Play Time: " + str(self.number_of_plays) + "\n"
        return return_str

class Game(object):
    def __init__(self, player, N=15, current_try=0, tries=6):
        self.N = N
        self.current_try = current_try
        self.tries = tries
        self.player = player
        self.random_number = random.randint(1, 15)

    def pick_number(self):
        while True:
            try:
                guess = int(input("Guess a number smaller than " + str(self.N) + ": "))
            except ValueError:
                print("Number is not an integer")
                continue
            if guess > self.N:
                print("Numebr is too high")
                continue

    def play(self):

        while True:
            guess = self.pick_number()
            self.current_try += 1

            if guess == self.random_number:
                print("Congratulations! You won in ", self.current_try, "tries")
                self.player.number_of_plays += 1
                self.win_rate[0] += 1
                print("You have won", self.win_rate[0], "games.")
                print("You have lost", self.win_rate[1], "games.")
                return

            else:
                if self.current_try == self.tries:
                    print("You have lost :(")
                    self.number_of_plays += 1
                    self.win_rate[1] += 1
                    print("You have won", self.win_rate[0], "games.")
                    print("You have lost", self.win_rate[1], "games.")
                    return
                else:
                    if guess > self.random_number:
                        print("Your guess is too high")
                    else:
                        print("Your guess is too low")


daragh = Player("Daragh", 1)
rebecca = Player("Rebecca", 2)


game1 = Game(daragh)
game1.play
