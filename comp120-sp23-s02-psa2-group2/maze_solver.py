# Add your code after this line.

from enum import Enum 
from agenda import Agenda, StackAgenda, QueueAgenda
import sys
from sys import argv 


class SquareType(Enum):
    """
    arguments:
    enum 
    returns:
    None
    """
    WALL = '#'
    OPEN_SPACE = '.'
    START = 'o'
    FINISH = '*'

class Square:
    """
    creates a new square obj 

    class named Square that represents one location in our maze. 

    instance variables:
    type (SquareType): The type of location represented by the square. Use the enum you created earlier to store this data.
    visited (bool): Whether this square has been visited or not. This value defaults to False.
    location (tuple[int, int]): The (x,y) location of the square in the maze. We’ll use the convention that (0, 0) is the upper left corner of the maze.

    returns 
    None 
    """
    def __init__(self, rep:str, x:int, y:int) -> None:


        try: 
            self.type = SquareType(rep)
        except: 
            raise ValueError("invalid")
        self.visited = False
        self.location = x,y 

#method that converts Square to a string 
    def __str__(self) -> str:
        """
        Special method to convert your square to a string. 
        It should return only a single character string based on the type of square this is (e.g. ‘#’ for a wall)
        and, in the case of an open space, whether it it has been visited or not (‘.’ if not visited, ‘x’ if it has been visited).

        """
        """
        >>> square = Square('#', 0, 0)
        >>> str(square)
        '#'

        >>> square = Square('.', 1, 2)
        >>> str(square)
        '.'

        """
        if self.type == SquareType.WALL:
            return '#'
        if self.type == SquareType.OPEN_SPACE and self.visited:
            return 'x'
        if self.type == SquareType.OPEN_SPACE and not self.visited:
            return '.'
        if self.type == SquareType.START:
            return 'o'
        if self.type == SquareType.FINISH:
            return '*'
   

class BadMazeFileFormat(Exception):
    pass


class Maze:
    """
    instance varibales: 
    _locations (list[list[Square]]): The 2D list of squares in the maze. We don’t want users to access/use this instance variable so don’t forget to have the name start with “_” so it is clear that it is a “private” variable. 
    width (int): The width of the maze.
    height (int): The height of the maze.

    methods: 
    __init__(self, filename: str) -> None : The initializer/constructor. The filename parameter will be the name of the file that contains the maze layout. See the section below for a description of how this file will be formatted. If the given file doesn’t have the correct format, this method should raise a BadMazeFileFormat exception, with a useful error message. Note that you’ll have to create the BadMazeFileFormat exception class.
    __str__(self) -> str : Special method to convert your maze to a string. It should return a string that shows the current status of the maze. It will look similar to the input format for the maze, but with any open spaces that have been visited being marked as ‘x’ instead of ‘.’.
    
    starting_square(self) -> Square : Returns the square in the maze that is the starting point. You can assume there will only be one starting point in the maze.
    get_square(self, x: int, y: int) -> Square : Returns the Square at the given (x,y) location. The maze’s top-left corner will be the (0, 0) coordinate. The x direction will be from left-to-right, and the y direction will be from top-to-bottom."""

    def __init__(self,filename:str) -> None:

        f = open(filename, 'r')
        f = f.readline()
        f = f.split()
        try:
            self.width = int(f[0])
            self.height = int(f[1])
        except:
            raise BadMazeFileFormat("Dimensions for maze formatted incorrecty")
        
        line_list = []
        x = 0 
        y = 0 
        for line in f:
            ch_list = []
            for ch in line:
                ch_square = Square(ch, x, y)
                ch_list.append(ch_square)
                x +=1 
            
            line_list.append(ch_list)
            x = 0 
            y += 1
    
        self._locations = line_list
    
    def __str__(self) -> str:
        """
        Special method to convert your maze to a string. It should return a string that shows the current status of the maze. 
        It will look similar to the input format for the maze, 
        but with any open spaces that have been visited being marked as ‘x’ instead of ‘.’.

        """
        """ 
        >>> maze= Maze('maze1.txt')
        >>> print(maze)
        #######
        #...#o#
        #*#...#
        #######
        <BLANKLINE>
    
        """
        s = ""
        for ch_list in self._locations:
            for ch in ch_list:
                s += str(ch)
            s += "\n"

        return s
    
    def starting_square(self) -> Square : 
        """Returns the square in the maze that is the starting point.
        """
        for y, ch_list in enumerate(self._locations):
            for x, line_list in enumerate(ch_list):
                if line_list.type == SquareType.START:
                    return line_list

    def get_square(self, x: int, y: int) -> Square :
        """Returns the Square at the given (x,y) location. The maze’s top-left corner will be the (0, 0) coordinate. 
        The x direction will be from left-to-right, and the y direction will be from top-to-bottom.

        """

        return self._locations[x][y]


def maze_solver(maze: Maze, agenda: Agenda, wait_for_user = False) -> bool:
    """
    this code which will bundle up the functionality of determining whether a maze has a solution—that is, 
    whether you can get from the start to the finish (without jumping over any walls).

    args:
    Maze(maze)
    agenda(Agenda)
    wait_for_user(bool) - defaults to false 
  
    """
    size = agenda.size()
    for i in range(size):
        agenda.remove()
    agenda.add(maze.starting_square())

    while agenda.is_empty == False:
        if wait_for_user == True:
            print(maze)
            input("Enter to continue")
        else:
            print(maze)
        
        square = agenda.remove()
        x,y = square.location

        if square.type == SquareType.FINISH:
            return True 
        elif square.type == SquareType.WALL:
            square.visited = True 
            continue
        elif square.visited == True:
            continue
        elif square.visited == False:
            square.visted = True 
            
            right_square = maze.get_square(x+1, y)
            agenda.add(right_square)
            
            left_square = maze.get_square(x-1, y)
            agenda.add(left_square)
            
            north_square = maze.get_square(x,y+1)
            agenda.add(north_square)
           
            south_square = maze.get_square(x,y-1)
            agenda.add(south_square)
       
        else:
            return False 
        


   

                
def main(maze_filename: str, agenda_type: str) -> None:
    """This function will create a Maze object, create either a StackAgenda or QueueAgenda object based on the type given by agenda_type, call the maze_solver function, 
    and print out a message saying either “Maze solution found.” or “Maze solution does not exist.”, depending on whether the solver was able to find a path to an exit or not.

    Parameters:
    maze_filename(str) - name of maze file

    agenda type(str) - type of agenda (either stack or queue)
    """
    
    if agenda_type == "stack":
        path = StackAgenda()
    elif agenda_type == "queue":  
        path = QueueAgenda()
    else:
        assert agenda_type == "stack" or agenda_type == "queue"
    
    maze = Maze(maze_filename)
    x = maze_solver(maze, agenda_type)
    if x == True:
        print("solution found")
    elif x == False:
        print("no solution found")
    

# The following lines should remain at the BOTTOM of the file
if __name__ == "__main__":
    if len(sys.argv)!=3:
       sys.exit("Invalid Arguments")
    else:
        main(str(sys.argv[1]), str(sys.argv[2]))