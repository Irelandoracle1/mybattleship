import random
class Mybattleship_Game:
    """
    This is the battleship game class
    it holds all the logic for the battleship game
    """
    player=[]
    computer=[]

    def __init__(self):
        """
        This concstructor method 
        is used for adding values to boards
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
            self.user_turn()
            m+=1

    
    
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
    def user_turn(self):
        """
        This method defines the logic for the users
        turn of play
        """
        while True:
            guess_row=int(input("Guess a Row:"))
            guess_column=int(input("Guess a Column:"))
            if guess_row==self.random_row() and guess_column==self.random_column():
                self.computer[guess_row][guess_column]="$"
                print("Yo! you made hit")
            else:
                if (guess_row<0 or guess_row>4) or (guess_column<0 or guess_column>4):
                    print("Sorry! guessed out of range. choose values from 0 to 4")
                    break



my_game=Mybattleship_Game()





