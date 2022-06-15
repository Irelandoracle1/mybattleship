import random
import sys


class Mybattleship_Game:
    """
    This is the battleship game class
    it holds all the logic for the battleship game
    """
    player = []
    computer = []

    def __init__(self):
        """
        This concstructor method is used for adding values to boards
        """
        for p in range(5):
            self.player.append(["~"]*5)
        for c in range(5):
            self.computer.append(["-"]*5)
        print("My Game Board")
        self.player_board()
        print("\n")
        print("Computer Game Board")
        self.computer_board()
        for m in range(10):
            self.player_turn()
            m += 1

    def player_board(self):
        """
        This method creates the player board
        from the player list already populated in 
        init method
        """ 
        for play in self.player:
            print(" ".join(play))
    def computer_board(self):
        """
        This method creates the computer board
        from the computer list already populated in 
        init method
        """ 
        for comp in self.computer:
            print(" ".join(comp))
    def random_row(self):
        """
        this returns random values between 0 and 4
        for the row
        """
        return random.randint(0, 5-1)
    def random_column(self):
        """
        this returns random values between 0 and 4
        for the column
        """
        return random.randint(0, 5-1)
    def player_turn(self):
        """
        This method defines the logic for the users
        turn of play
        """
        v=1
        while True:
            try:
              guess_row=int(input("Guess a Row:"))
            except ValueError:
                  print("You entered an invalid row value. You should choose integer values only")
                  break
            try:
              guess_column=int(input("Guess a Column:"))
            except ValueError:
                  print("You entered an invalid row value. You should choose integer values only")
                  break
            if guess_row==self.random_row() and guess_column==self.random_column():
                self.computer[guess_row][guess_column]="$"
                print("Yeh! you made hit")
            else:
                if (guess_row<0 or guess_row>4) or (guess_column<0 or guess_column>4):
                    print("Sorry! guessed out of range. choose values from 0 to 4")
                    break
                else:
                    self.computer[guess_row][guess_column]="X"
                    print(" Sorry! you missed the hit")
            self.computer_turn()
            print(f'SCORES For this Round: You:{self.player_score()} | Computer: {self.computer_score()}')
            print("My Game Board")
            self.player_board()
            print("\n")
            print("Computer Game Board")
            self.computer_board()
            quit_game=input("Click any button and enter to continue or click X and enter to exit the game")
            if quit_game=="x":
                sys.exit()
            if v>10:
                print("GAME OVER!!!")
                self.game_winner()
                sys.exit()

            v+=1

    def computer_turn(self):
        """
        This method defines the logic for the computer
        turn of play
        """
        guess_row=self.random_row()
        guess_column=self.random_column()
        game_alive=True
        while game_alive:
            if guess_row==self.random_row() and guess_column==self.random_column():
                self.player[guess_row][guess_column]="$"
                print("Hey! you were hit by the computer")
            else:
                self.player[guess_row][guess_column]="X"
                print(" the computer missed the hit")
            game_alive=False
    
    def player_score(self):
        """
        this method helps count and sum up
        the player scores from the computers board
        """
        scores=0
        for score in self.computer:
            scores +=score.count("$")
            return scores

    def computer_score(self):
        """
        this method helps count and sum up
        the computer scores from the players board
        """
        scores=0
        for score in self.player:
            scores +=score.count("$")
            return scores
    def game_winner(self):
        """
        This method is used for determining the game winner
        """
        if self.player_score()>self.computer_score():
            print("Hurray! You are the winner of the game")
        elif self.computer_score()>self.player_score():
            print("Sorry! the computer won")
        else:
            print("There is no winner. It is a draw")
            
        



print("Welcome to The Battleship Game")
input("click enter to start playing!")
my_game=Mybattleship_Game()





