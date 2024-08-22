import pytest
from agenda import Agenda, StackAgenda, QueueAgenda
from maze_solver import Maze, maze_solver 

def valid_maze_stack():
    maze = Maze('maze1.txt')
    agenda = StackAgenda()

    assert maze_solver(maze, agenda, False) == True

def invalid_maze_stack():
    maze = Maze('maze1.txt')
    agenda = StackAgenda()

    assert maze_solver(maze, agenda, False) == False

def valid_maze_queue():
    maze = Maze('maze1.txt')
    agenda = QueueAgenda()

    assert maze_solver(maze, agenda, False) == True

def invalid_maze_queue():
    maze = Maze('maze1.txt')
    agenda = QueueAgenda()

    assert maze_solver(maze, agenda, False) == False        