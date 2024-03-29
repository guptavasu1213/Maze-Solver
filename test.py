#importing the Maze class to test all the files
from maze_class import *

#This function tests all the given maze files and shows the solution of it, if possible.
def test():
    print("--RUNNING THE TEST FUNCTION FOR ALL THE FILES--\n")
    for file in ["test_files/maze510.txt", "test_files/maze510cycles.txt", "test_files/maze510island.txt", "test_files/maze510islandnosoln.txt", 
                 "test_files/maze510nosoln.txt","test_files/maze1020.txt", "test_files/maze50100.txt"]:
        fIn = open(file)
        contents_of_file = fIn.readlines()     
        fIn.close()     #Very Important to close
        maze= Maze(contents_of_file)    #Creating the object
        if maze.find_path(*list(maze._startingPoint)) == True:
            print("\n\nSolution of", file, "file is:")
            maze.print_maze()
        else:
            print("\n\nThere is no solution for the maze in", file, "file.")
test()
