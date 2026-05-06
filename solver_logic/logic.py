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
    
    def get_columns(self):
        columns = []
        
        for i in range(len(self.grid[0])): # len(grid[0]) - row length
            temp = []
            for row in self.grid:
                temp.append(row[i])
            columns.append(temp)

        return columns
    
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
        # consistent with the existing row state 
        current_position = 0 
        indexes = []
        result = row[:] #copy initial row state
        
        for j in range(current_position, len(result)):
            if result[j] == 1:
                if j not in indexes:
                    indexes.append(j)

        for i, group in enumerate(clue): 
            gap = 0
            
            while not self.can_place(result, current_position, group):
                if len(indexes) > 1:
                # find gap between indexes and chceck if its bigger than the group, if so shift current position 
                    for a, cell in enumerate(result):
                        if cell in [1,0]:
                            # print(f"found 1 at index {a}")
                            continue
                        if a <= indexes[-1]:
                            # print(f"adding 1 to gap, current index = {a}")
                            gap +=1

                if i == len(clue) - 1 and gap >= group:
                    current_position = indexes[-1] - group

                current_position += 1  
                if current_position > len(result):
                    raise ValueError("No valid placement found")

            for k in range(group):
                result[current_position + k] = 1
            
            current_position += group
            if i != len(clue) - 1:
                result[current_position] = 0

        for l, cell in enumerate(result):
            if cell == None:
                result[l] = 0
            
        return result

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

    def solve(self):
        return "solution"

#####################################################################################################################    

# rows = [["row_1"],
#         ["row_2"],
#         ["row_3"],
#         ["row_4"],
#         ["row_5"],
#         ["row_6"]
#         ]
# cols = [["col_0"],
#         ["col_1"],
#         ["col_2"],
#         ["col_3"],
#         ["col_4"],
#         ["col_5"]
#         ]
# test = NonoPuzzle(rows,cols)
# print(test.grid)

# left = test.leftmost_position(test.grid[1], [1,3])
# right = test.rightmost_position(test.grid[1], [1,3])

test = NonoPuzzle(DUCK.rows,DUCK.cols)
for i, row in enumerate(test.grid):
    print(i, row)
left = test.leftmost_position(test.grid[5], DUCK.rows[5])
right = test.rightmost_position(test.grid[5], DUCK.rows[5])

# left = test.leftmost_position([None, 1, None, None, None, None, None, None, None, 1], [2,2]) # works
# left = test.leftmost_position([1, 1, None, None, 1, None, None, 1, None, 1], [3,1,3]) # works

# left = test.leftmost_position([None, 1, None, None, None, None, None, None, 1, None], [3,2,2]) # works
# right = test.rightmost_position([None, 1, None, None, None, None, None, None, 1, None], [3,2,2]) # works

print(f"left: {left}\nright: {right}")
print(f"overlap: {test.find_overlap(left, right)}")
