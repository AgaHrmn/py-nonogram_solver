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
    
    def can_place(self, row, start, size):
        # returns True if a group of `size` can be placed at position `start`
        # Skip cells already set to 0, Respect cells already set to 1

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
    
    def leftmost_position(self, row, clue):
        # refactor to find the leftmost valid arrangement that is 
        # consistent with the existing row state 

        initial_row_state = [x for x in row]
        current_position = 0 
        indexes = []
        space_needed = 0
        
        print(f"initial_row_state: {initial_row_state}")

        for j in range(current_position, len(row)):
                    if initial_row_state[j] == 1:
                        if j not in indexes:
                            indexes.append(j)
        print(indexes)

        for group in clue:
            space_needed += group + 1
        space_needed -= 1

        print(space_needed)
        if len(row[indexes[0]:]) >= space_needed:
            print(f"len(row[indexes[0]:]) <= space_needed : {len(row[indexes[0]:])} < {space_needed}")
            current_position = indexes[0]
        else: 
            print(f"leftmost possible start: {indexes[-1]-space_needed + 1}")
            current_position = indexes[-1]-space_needed + 1

######################################################
        for i, group in enumerate(clue): 
            
            while not self.can_place(row, current_position, group):
                current_position += 1  
                if current_position > len(row):
                    raise ValueError("No valid placement found")
                
            for k in range(group):
                row[current_position + k] = 1
            
            current_position += group
            if i != len(clue) - 1:
                row[current_position] = 0

        for l, cell in enumerate(row):
            if cell == None:
                row[l] = 0
            
        return row

    def rightmost_position(self, row, clue):
        # reverse clue [3,2] -> [2,3] 
        # reverse the row state (preserving existing cells mirrored)
        # leftmost of reversed clue on reversed row
        # reverse result 
        reversed_clue = clue[::-1] # not altering the clue 
        reversed_row = row[::-1]
        temp_row = self.leftmost_position(reversed_row, reversed_clue)
        result = temp_row[::-1]
 
        return result

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
# print(test.has_uncovered_ones([None, None, None, None, None, None, None, 1, 1, None], 1,3))

# left = test.leftmost_position([None, None, None, 1, None, None, None, 1, None, None], [3,2]) # works
left = test.leftmost_position([None, None, None, None, None, None, None, 1, None, None], [3,2]) # doesn't work - not considering gap between group of 3 as part of group

# right = test.rightmost_position([None, None, None, 1, None, None, None, None, 1, None], [3,2])

# print(f"row: [None, None, None, 1, None, None, None, None, 1, None]")
print(left)
# print(f"left: {left}\nright: {right}")
# print(f"overlap: {test.find_overlap(left, right)}")
