#importing the Maze class to test the given file
from maze_class import *

# This function prompts the user for an input for the file which contains a maze;
# If it is a valid file, the contents of the file are used to create an object of Maze class
# If the solution is possible, the .findPath method prints the solution
# If solution is possible, a statement is printed
def main():
    while True:
        fName = input("Enter the file name: ")
        try:
            fIn = open(fName)
            break # Breaks out when the program doesn't crash while opening the file
        except: #If the file is not present, the program crashes.
            print("Please enter a valid file name. Try Again\n")
  
    #After opening the file successfully, the contents of the file are supposed to be read.
    contents_of_file = fIn.readlines()     
    fIn.close()     #Very Important to close
    print("\nMaze requested to solve: ",fName)
    
    maze = Maze(contents_of_file)
    if maze.find_path(*list(maze._startingPoint)) == True:
        print("\n\nSolution of the requested", fName, "file is:")
        maze.print_maze()
    else:
        print("There is no solution for the maze in", fName, "file.")
main()
