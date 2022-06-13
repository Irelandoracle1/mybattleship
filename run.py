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
    
    def player_board(self):
        """
        This method creates the player board
        from the player list already populated in 
        init method
        """ 








