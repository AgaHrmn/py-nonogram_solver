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
    
    def leftmost_position(self, clue, length):
        # calculate needed space for the clue - [3,2] - (3*1 + 0) + (2*1) 
        # fill rest of the row with 0
        
        space_needed = 0
        index = 0
        row = []

        for _ in range(length):
            row.append(None)

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

    def rightmost_position(self, clue, length):
        # reverse clue [3,2] -> [2,3] 
        # leftmost of reversed clue 1110110000
        # reverse result 0000110111
        reversed_clue = clue[::-1] # not altering the clue 
        row = self.leftmost_position(reversed_clue, length)
        reversed_row = row[::-1]
 
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
    
    def solve(self):
        return "solution"
    

# test = NonoPuzzle(DUCK.rows,DUCK.cols)
# left = test.leftmost_position(DUCK.rows[4], len(DUCK.cols))
# right = test.rightmost_position(DUCK.rows[4], len(DUCK.cols))

rows = [[3,2],[1],[2,4]]
cols = [[3,1],[4],[4,2],[7]]

test = NonoPuzzle(rows,cols)
left = test.leftmost_position(rows[0], 10)
right = test.rightmost_position(rows[0], 10)

print(f"left: {left}\nright: {right}")
print(f"overlap: {test.find_overlap(left, right)}")