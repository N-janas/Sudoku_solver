
# Example sudoku (0 - empty space)
sudoku = [
    [9,0,0,0,6,5,0,2,0],
    [0,8,7,0,0,0,0,1,0],
    [0,0,0,0,0,0,0,8,0],
    [0,7,0,0,0,0,0,0,0],
    [0,0,2,4,3,0,5,0,0],
    [0,0,0,0,1,0,7,0,0],
    [8,9,0,0,0,4,0,0,0],
    [0,0,6,0,0,0,3,0,0],
    [0,4,0,0,2,9,0,0,0]
]

# Check if number(i) is valid in position [r][c]
def valid(i,r,c, sud): 
    # Row
    if i in sud[r]:
        return False

    # Column
    for row in sud:
        if i == row[c]:
            return False

    # Square
    k = r//3
    if k==0:
        r = 0
    elif k==1:
        r = 3
    else:
        r = 6

    k = c//3
    if k==0:
        c = 0
    elif k==1:
        c = 3
    else:
        c = 6

    for l in range(r,r+3):
        if i in sud[l][c:c+3]:
            return False

    return True
    
# Searching for empty spot
def find_empty(sud):            
    for r, row in enumerate(sud):
        for c, el in enumerate(row):
            if el == 0:
                return r,c

    return None


def fill(sud, proceed):
    result = find_empty(sud)
    #If no free spots left skip earlier recursions
    if result == None:      
        return False
    else:
        r, c = result

        for i in range(1,10):
            if valid(i,r,c, sud):
                sud[r][c] = i
                proceed = fill(sud, True)
        # Proceed if free spots are still in board
        if proceed:         
            sud[r][c] = 0
            return True

# Print sudoku before
for f in sudoku:            
    print(f)

fill(sudoku, True)
print('----------------------------')

# Print sudoku after
for f in sudoku:            
    print(f)
