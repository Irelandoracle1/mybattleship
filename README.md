# Sumo Battleship Game

Sumo Battleship Game is a Command Line Interface Game based on the popular battleship game played with pen and paper.
This game is currently hosted online on Heroku.
Unlike the physical version that is played between to people, Sumo Battleship Game is played between  a person 
and the computer. Where the player and the computer fires at each others battleship through a grid or coordinate 
guess system.Any game lover will definitely find Sumo Battleship interesting and entertaining. That is whether he/she had played the physical 
version or not

### Here Is The Live Version
![Responsice Mockup](https://github.com/lucyrush/readme-template/blob/master/media/love_running_mockup.png)

## How To Play Sumo Battleship Game

To start playing Sumo Battleship, as you navigate to the game interface, you receive a prompt to click the enter button 
to start playing as you click on the enter button two game boards are presnted to you. One for you, the player and the 
other for the computer. The ships locations are randomly positioned on the two boards and hidden. Then the player
is presented prompts to fire at the computer's ships through grid guessing by choosing a row and a column from 0 to 4
at a time. As the user chooses his coordinates and clicks enter, he fires at the computer's ship. While the computer in return 
also fires at the player's ship at the same time. The game presents the player and the computer 10 maximum play rounds.
 A hit is indicated on both boards with an '$'character while a miss is indicate with an 'X'character.
 The scores for each rounds are displayed to the user at each round. Then finally, after the 10th round, the winner between the 
player and the computer is displayed and the game automatically exits the interface. And to replay the game, you have to re-run 
the game application again. 

##Features

### Existing Features

- __Automatic Game Boards__

  - Two game boards are automatically generated. One for the player and one for the computer
  - The ship positions are hidden in both the player and computer's game boards
  ![Nav Bar](https://github.com/lucyrush/readme-template/blob/master/media/love_running_nav.png)
  - Player and computer play turn are executed simultaneously
  - The Game Prompts And Recieves User's Input
  - Manages Scores For Every Game Round

   ![Nav Bar](https://github.com/lucyrush/readme-template/blob/master/media/love_running_nav.png)

- __Error Handling And Input Validation__

  - The player or computer are not allowed to guess a grid (row and column) 
  - The player cannot enter any other value apart from numbers within the specified range
  - The player is not allowed to guess numbers out of the specified range
  ![Landing Page](https://github.com/lucyrush/readme-template/blob/master/media/love_running_landing.png)
  - The Game Data is managed in a single class instance or object

### Future Features

- Display Ships on the player board
- Prompt the player to manually exit game or play another game after the end of a particular game session

## Data Model
-I store the game's board data in two lists using loops. The player and computer boards are initialized with empty lists.
Which are populated at run time, with values at run time in the game's class constructor method. The data stored in the 
board lists include, the board display characters and board size. Then the board lists data are updated as the player and 
the computer make guesses.

## Testing 
 I have manually tested this application through this process
-I inputed wrong values. Such as adding empty values, string values and adding the same coordinates twice
-I passed the code through the PEP8online.com test and confirmed there is no error on my code
-Tested the App in my local terminal and also my Heroku hosted terminal
 
### Validator Testing 
-PEP8
 - Errors originally returnd from PEP8online.com were all fixed
 - Final code testing returned with a message: ALL RIGHT
 
### Bugs
   -As at the point of development, I encountered errors in game scoring as I tried to count the scores with just for loop.
     I finally fixed the error using the sum() function

### Unfixed Bugs

No Bug is left unfixed

## Deployment

This are the steps I followed in deploying the application to Heroku are as follows

- Steps For Deployment 
  - Fork or Clone this repository
  - Create a new Hroku App
  - Set the builbacks for Python and Nodejs 
  - Link the Heroku App to the repository 
  - Click on 'Deploy'

The live link can be found here - https://code-institute-org.github.io/love-running-2.0/index.html 


## Credits 
- Code Institute for the sample development template and the battleship game development guide and sample
- Wikipedia for information about the Battleship game and History





