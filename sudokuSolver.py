# A Backtracking program  in Pyhton to solve Sudoku problem
 
 
# A Utility Function to print the Grid
def print_grid(arr):
    for i in range(9):
        print (arr[i])
   
 
         
# Function to Find the entry in the Grid that is still  not used
# Searches the grid to find an entry that is still unassigned.
def find_empty_location(arr,j):
    for row in range(9):
        for col in range(9):
            if(arr[row][col]==0):
                j[0]=row
                j[1]=col
                return True
    return False
 
# Returns a boolean which indicates whether any assigned entry
# in the specified row matches the given number.
def used_in_row(arr,row,num):
    for i in range(9):
        if(arr[row][i] == num):
            return True
    return False
 
# Returns a boolean which indicates whether any assigned entry
# in the specified column matches the given number.
def used_in_col(arr,col,num):
    for i in range(9):
        if(arr[i][col] == num):
            return True
    return False
 
# Returns a boolean which indicates whether any assigned entry
# within the specified 3x3 box matches the given number
def used_in_box(arr,row,col,num):
    for i in range(3):
        for j in range(3):
            if(arr[i+row][j+col] == num):
                return True
    return False
 
# Checks whether it will be legal to assign num to the given row,col
#  Returns a boolean which indicates whether it will be legal to assign
#  num to the given row,col location.
def check_location_is_safe(arr,row,col,num):
     
    # Check if 'num' is not already placed in current row,
    # current column and current 3x3 box
    return not used_in_row(arr,row,num) and not used_in_col(arr,col,num) and not used_in_box(arr,row - row%3,col - col%3,num)
 
# Takes a partially filled-in grid and attempts to assign values to
# all unassigned locations in such a way to meet the requirements
# for Sudoku solution (non-duplication across rows, columns, and boxes)
def solve_sudoku(arr):
     
    # 'j' is a list variable that keeps the record of row and col in find_empty_location Function    
    j=[0,0]
     
    # If there is no unassigned location, we are done   
    if(not find_empty_location(arr,j)):
        return True
     
    # Assigning list values to row and col that we got from the above Function 
    row=j[0]
    col=j[1]
     
    # digits 1 to 9
    for num in range(1,10):
         
        if(check_location_is_safe(arr,row,col,num)):
             
            # make tentative assignment
            arr[row][col]=num
 
            # return, if sucess
            if(solve_sudoku(arr)):
                return True
 
            # failure, try again
            arr[row][col] = 0
             
    #triggers backtracking        
    return False
 
# test functions
if __name__=="__main__":
     
    # 2D array 
    grid=[[0 for x in range(9)]for y in range(9)]
     
    # assigning values 
    grid=[[0,0,4,3,0,0,2,0,9],
          [0,0,5,0,0,9,0,0,1],
          [0,7,0,0,6,0,0,4,3],
          [0,0,6,0,0,2,0,8,7],
          [1,9,0,0,0,7,4,0,0],
          [0,5,0,0,8,3,0,0,0],
          [6,0,0,0,0,0,1,0,5],
          [0,0,3,5,0,8,6,9,0],
          [0,4,2,9,1,0,3,0,0]]

    # if sucess print the grid
    if(solve_sudoku(grid)):
        print_grid(grid)
    else:
        print ("No solution exists")



        
