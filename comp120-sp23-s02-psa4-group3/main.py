"""
Program to try to escape from a customize labyrinth.

Author:
Maggie Cope: mcope@sandiego.edu
"""
import labyrinth
from labyrinth import MazeCell, Item

# Change the following variable (YOUR_NAME) to contain your FULL name.

"""
!!!WARNING!!!

Once you've set set this constant and started exploring your maze,
do NOT edit the value of YOUR_NAME. Changing YOUR_NAME will change which
maze you get back, which might invalidate all your hard work!
"""

YOUR_NAME = "Maggie Cope"

# Change these following two constants to contain the paths out of your mazes.
# You'll need to use the debugger to help you out!

PATH_OUT_OF_MAZE        = "SESESWWNSEEENSWNNNES"
PATH_OUT_OF_TWISTY_MAZE = "SEWNESNWENSN"

def is_path_to_freedom(start: MazeCell, moves: str) -> bool:
    """
    Given a location in a maze, returns whether the given sequence of
    steps will let you escape the maze. The steps should be given as
    a string made from N, S, E, and W for north/south/east/west without
    spaces or other punctuation symbols, such as "WESNNNS"

    To escape the maze, you need to find the Potion, the Spellbook, and
    the Wand. You can only take steps in the four cardinal directions,
    and you can't move in directions that don't exist in the maze.

    Precondition: start is not None

    Args:
        start (MazeCell): The start location in the maze.
        moves (str): The sequence of moves.

    Raises:
        ValueError: If <moves> contains any character other than N, S, E, or W

    Returns:
        (bool) Whether that sequence of moves picks up the needed items
               without making nay illegal moves.
    """
    assert start is not None 

    #new variable for the current part of the maze 
    current = start 

    #sets the magic varibles to False, will change to True if found 
    spellbook = False 
    potion = False 
    wand = False 
   
   #loops through each move in the given sequence 
    for move in moves:
        #raises value error if the move is not NESW
        if move not in 'NESW':
            raise ValueError
       
        next = None 
        #Moves the current position by the next given move 
        if move == 'N':
            next = current.north 
        elif move == 'S':
            next = current.south  
        elif move == 'E':
            next = current.east 
        elif move == 'W':
            next = current.west 
        #if the path cannot be completed returns False 
        if next == None:
            return False
        #sets the current step to the next step 
        current = next 
        #checks if the item at current is a spellbook, potion, or wand 
        if current.whats_here != Item.NOTHING:
            if current.whats_here == Item.SPELLBOOK:
                spellbook = True
            if current.whats_here == Item.POTION:
                potion = True 
            if current.whats_here == Item.WAND:
                wand = True 

    #returns if the spellbook, potion, and wand have all been collected and you can escape the maze
    return spellbook and potion and wand 




def main() -> None:
    """ Generates two types of labyrinths and checks whether the user has
    successfully found the path out of them.

    DO NOT MODIFY THIS CODE IN ANY WAY!!!
    """
    start_location = labyrinth.maze_for(YOUR_NAME)

    print("Ready to explore the labyrinth!")
    # Set a breakpoint here to explore your personal labyrinth!

    if is_path_to_freedom(start_location, PATH_OUT_OF_MAZE):
        print("Congratulations! You've found a way out of your labyrinth.")
    else:
        print("Sorry, but you're still stuck in your labyrinth.")


    twisty_start_location = labyrinth.twisty_maze_for(YOUR_NAME)

    print("Ready to explore the twisty labyrinth!")
    # Set a breakpoint here to explore your personal TWISTY labyrinth!

    if is_path_to_freedom(twisty_start_location, PATH_OUT_OF_TWISTY_MAZE):
        print("Congratulations! You've found a way out of your twisty labyrinth.")
    else:
        print("Sorry, but you're still stuck in your twisty labyrinth.")



if __name__ == "__main__":
    main()
