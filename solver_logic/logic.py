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
    
    def leftmost_position(self, row, clue):
        # calculate needed space for the clue - [3,2] - (3*1 + 0) + (2*1) 

        # refactor to find the leftmost valid arrangement that is 
        # consistent with the existing row state 
        # Skip cells already set to 0, Respect cells already set to 1
        
        # row = [None, None, None, None, None, None, None, None, None, None]
        # row = [None, None, 0, None, None, None, None, None, None, None]
        # row = [None, None, None, None, 1, None, None, None, None, None]        
        # clue = [3,2]

        current_position = 0 
        for i, group in enumerate(clue):
            print(f"current position: {current_position}")
            while not self.can_place(row, current_position, group):
                current_position += 1
                if current_position > len(row):
                    raise ValueError("No valid placement found")
                
            for j in range(group):
                row[current_position + j] = 1
            
            current_position += group
            if i != len(clue) - 1:
                row[current_position] = 0

        for i, cell in enumerate(row):
            if cell == None:
                row[i] = 0
            
        return row

    def rightmost_position(self, row, clue):
        # reverse clue [3,2] -> [2,3] 
        # leftmost of reversed clue 1110110000
        # reverse result 0000110111
        reversed_clue = clue[::-1] # not altering the clue 
        temp_row = self.leftmost_position(row, reversed_clue)
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
    
    def can_place(self, row, start, size):
        # returns True if a group of `size` can be placed at position `start`

        # row = [None, None, None, None, None, None, None, None, None, None]
        # row = [None, None, 0, None, None, None, None, None, None, None]
        # row = [None, None, None, 1, None, None, None, None, None, None]
        # start = 0
        # size = 3
        
        if start + size > len(row): #end of row
            # print("end of row")
            return False
        if start + size < len(row) and row[start+size] not in (None,0):  #no touching the next group
            # print("is touching the next group")
            return False
        for cell in row[start:(start + size)]:
            if cell == 0:
                # print(f"0's in the way")
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
# left = test.leftmost_position(test.grid[4], DUCK.rows[4])
# right = test.rightmost_position(test.grid[4], DUCK.rows[4])

rows = [[1],[1,1],[1]]
cols = [[1],[1,1],[1]]

test = NonoPuzzle(rows,cols)
left = test.leftmost_position(test.grid[1], rows[1])
right = test.rightmost_position(test.grid[1], rows[1])

print(f"left: {left}\nright: {right}")
print(f"overlap: {test.find_overlap(left, right)}")
# print(f"get columns result: {test.get_columns()}")
