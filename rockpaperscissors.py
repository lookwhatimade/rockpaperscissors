import time
import random
import os
import sys


class RockPaperScissors:

    def __init__(self):
        """ Intialize a tuple that defines your rock paper scissor options """

        self.rock_paper_scissors = ('rock', 'paper', 'scissors')

    def play(self):
        """
        Play Rock, Paper, Scissors.  This function loops and allows you to keep playing until CTRL-C is pressed
        """

        print('Rock, Paper, Scissors \n')

        input("Press Enter to Play! ")
        while True:
            try:
                os.system('clear')
                print('Counting down from 3 ...')
                time.sleep(1)
                self.countdown(3)
                print('SHOOT!\n')
                self.shoot()

                input("Press Enter to Play Again.  CTRL-C to Exit. ")

            except KeyboardInterrupt:
                os.system('clear')
                print('Thanks for playing! \n')
                sys.exit(0)

    def countdown(self, count_down_from):
        """
        Count down from an integer passed into the function

        Parameters:
           count_down_from (int): The number to start counting down from
        """

        while count_down_from > 0:
            print(count_down_from)
            time.sleep(1)
            count_down_from -= 1

    def shoot(self):
        """
        Get a random integer a range 0,2.
        Use that random int as an index for your tuple.
        From there, dynamically call a rock, paper, or scissor function
        """

        self.__getattribute__(self.rock_paper_scissors[random.randint(0, 2)])()

    def rock(self):
        """ Print Rock """

        print("""
        ROCK

            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        
        
        """)

    def paper(self):
        """ Print Paper """

        print("""
        PAPER
        
             ________
        ---'    _____)____
                   _______)
                  ________)
                 ________)
        ---.___________)
        
        
        """)

    def scissors(self):
        """ Print Scissor """

        print("""
        SCISSORS
        
            _______
        ---'   ____)______
                  ________)
               ____________)
              (____)
        ---.__(___)
        
        
        """)


if __name__ == '__main__':

    # clear terminal screen
    os.system('clear')

    # instatiate class and play the game
    rps = RockPaperScissors()
    rps.play()
