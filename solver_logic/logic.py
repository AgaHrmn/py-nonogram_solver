from example_nono import NonoData, DUCK 


class NonoPuzzle: 
    """Class to solve nonograms"""
    def __init__(self, row_clues, col_clues):
        self.row_clues = row_clues
        self.col_clues = col_clues
        self.grid = self.get_grid()

    def get_grid(self):
        grid = []
        for _ in range(len(self.row_clues)):
            row = []
            for _ in range(len(self.col_clues)):
                row.append(None)
            grid.append(row)         
        return grid
    
    def leftmost_position(self):
        # calculate needed space for the clue - [3,2] - (3*1 + 0) + (2*1) 
        # fill rest of the row with None

        # refactor to find the leftmost valid arrangement that is 
        # consistent with the existing row state !!! 
        # Skip cells already set to 0, Respect cells already set to 1
        
        row = [0,0,1,0,0,0,0,0,0,0]
        clue = [3,2]

        space_needed = 0
        index = 0

        # for _ in range(length):
        #     row.append(None)

        for i, c in enumerate(clue): 
            space_needed += c

            while index <= space_needed:
                if index == space_needed:
                    if i != len(clue) - 1: #skipping last 0 - in case clue fills whole row 
                        #print(f"inserting 0 at index {index}")
                        row[index] = 0
                else: 
                    row[index] = 1
                index += 1
            space_needed += 1
        
        for i, c in enumerate(row): #filling tailing cells with 0
            if c == None:
                row[i] = 0    

        return row

    def rightmost_position(self, clue, row):
        # reverse clue [3,2] -> [2,3] 
        # leftmost of reversed clue 1110110000
        # reverse result 0000110111
        reversed_clue = clue[::-1] # not altering the clue 
        temp_row = self.leftmost_position(reversed_clue, row)
        reversed_row = temp_row[::-1]
 
        return reversed_row

    def find_overlap(self, leftmost, rightmost):
        overlap = []

        if len(leftmost) != len(rightmost):
            raise ValueError("Rows must be the same length")
        
        for _ in range(len(leftmost)):
            overlap.append(None)

        for i, l in enumerate(leftmost):
                if l == 1 and rightmost[i] == 1: # definitely filled 
                    overlap[i] = 1
                else:
                    overlap[i] = None # unknown
        return overlap
    
    def can_place(row, start, size):
        # returns True if a group of `size` can be placed at position `start`
        # row = [None, None, None, None, None, None, None, None, None, None]
        # row = [None, None, 0, None, None, None, None, None, None, None]
        # row = [None, None, None, 1, None, None, None, None, None, None]

        # start = 0
        # size = 3
        
        if start + size > len(row): #end of row
            print("end of row")
            return False
        if start + size < len(row) and row[start+size] not in (None,0):  #no touching the next group
            print("is touching the next group")
            return False
        for cell in row[start:(start + size)]:
            if cell == 0:
                print(f"0's in the way")
                return False
        return True
                                
    
    def get_columns(self):
        columns = []
        
        for i in range(len(self.grid[0])): # len(grid[0]) - row length
            temp = []
            for row in self.grid:
                temp.append(row[i])
            columns.append(temp)

        return columns

    def solve(self):
        return "solution"
    

# test = NonoPuzzle(DUCK.rows,DUCK.cols)
# left = test.leftmost_position(DUCK.rows[4], len(DUCK.cols))
# right = test.rightmost_position(DUCK.rows[4], len(DUCK.cols))

rows = [[1],[1,1],[1]]
cols = [[1],[1,1],[1]]

test = NonoPuzzle(rows,cols)
print(f"grid: {test.grid}")

# left = test.leftmost_position(rows[0], 10)
# right = test.rightmost_position(rows[0], 10)

# print(f"left: {left}\nright: {right}")
# print(f"overlap: {test.find_overlap(left, right)}")
# print(f"get columns result: {test.get_columns()}")
