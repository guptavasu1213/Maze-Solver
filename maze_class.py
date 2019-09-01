class Maze:
    
    def __init__(this, maze):
        this._maze = maze 
        this.get_values()
        this.maze_formatting()
    
    #This method retrieves all the given values from the first 3 lines of the file
    # Line 1: Contains the dimensions of the maze
    # Line 2: The starting point in the maze
    # Line 3: The ending point in the maze
    # NOTE THAT THE VALUES ARE GIVEN IN TERMS OF POSITIONS, NOT INDICES
    # Hence, after retrieving theses values, they are manipulated in terms of their indices and 
    #        specified as startingPoint and endPoint 
    def get_values(this):
        #Popping out the first line in the text file
        this._dimensionOfMaze= this._maze.pop(0).strip().split(" ")    # ["5", "10"]  First line
        #print(this._dimensionOfMaze) #DEV CHECK
        
        #Popping out the second line in the text file which becomes the first after popping out previous one
        given_start = this._maze.pop(0).strip().split(" ") # ["1" , "1"]  Second line
        #print(given_start ) #DEV CHECK

        #Popping out the third line in the text file which becomes the first after popping out previous ones        
        given_end   = this._maze.pop(0).strip().split(" ") # ["5" , "10"] Third line
        #print(given_end) #DEV CHECK        
        
        # Manipulating the given values to the values in the code in terms of their indices
        #          Example:    (              (5*2)+1             -     1              - 1 ,       1              )
        #                      (                9th INDEX for the row                      , 1st INDEX for column )                             
        this._startingPoint = (int(this._dimensionOfMaze[0])*2 +1 - int(given_start[0]) -1 , int(given_start[1]))    
        #print("Start:", this._startingPoint ) #DEV CHECK --> (1,9)
        
        #          Example:    (              (5*2)+1             -     (5*2)+1        - 1 ,       10*2 +1         )
        #                      (                1st INDEX for the row                      , 19th INDEX for column )                             
        this._endPoint = (int(this._dimensionOfMaze[0])*2 - int(given_end[0])*2  +1        , int(given_end[1])*2 -1)   
        #print("End: ", this._endPoint )#DEV CHECK  --> (1,19)
                
    def maze_formatting(this):    
        index = 0
        for row in this._maze:
            row = row.strip() # Strips out the \n at the end of each row
            this._maze[index] = []
            for element in row:
                this._maze[index].append(element)
            index += 1                       
    
    #The method prints the maze out
    # The catch is that if the * is present around the "+", just print a space
    def print_maze(this):
        
        for row in range(len(this._maze)):
            for column in range(len(this._maze[row])):
                
                #If you reach the boundary of the maze, then just print the last character
                if row == len(this._maze)-1 or column == len(this._maze[row]):
                    print(this._maze[row][column], end="")                     
                else:   
                    print(this._maze[row][column], end= "")
                    
            print() # New line after every row

    # CHECKING if the the point is within the maze boundary
    def is_in_bounds(this, x, y):
        return 0 < x < len(this._maze) and 0 < y < len(this._maze[0])
    
    def find_path(this, x, y):
        # If the point specified is not present within the boundary of the maze; return False 
        if not this.is_in_bounds(x, y):
            return False

        # If the final point is reached, then mark it and return True
        if x == this._endPoint[0] and y == this._endPoint[1]:    
            this._maze[x][y]= '*'            
            return True
        
        #If the point is not an empty space, then go back
        if this._maze[x][y] != ' ':
            return False

        this._maze[x][y]= '*' #Marking the * in the maze
        
        #this.print_maze()       # To keep track of the maze
        
        if this.find_path(x + 1, y):   #Move south
            return True                        
        if this.find_path(x - 1, y): #Move north
            return True
        if this.find_path(x, y + 1): #Move east
            return True
        if this.find_path(x, y - 1): #Move west
            return True
        
        #When all the directions won't work, then point which is marked as * will be  back to " " 
        this._maze[x][y] = " "
        
        #This return statement is executed after the checking all the possible direction
        return False
