
class Puzzle: 
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
        clues = [3, 2]
        row = []
        space_needed = 0
        index = 0
        for _ in range(10):
            row.append(None)

        for i, c in enumerate(clues): 
            space_needed += c

            while index <= space_needed:
                if index == space_needed:
                    if i != len(clues) - 1: #skipping last 0 - in case clue fills whole row 
                        print(f"inserting 0 at index {index}")
                        row[index] = 0
                else: 
                    row[index] = 1
                index += 1
            space_needed += 1
        
        for i, c in enumerate(row): #filling tailing cells with 0
            if c == None:
                row[i] = 0    

        return row

    def solve(self):
        return "solution"
    
rows = [[1,2,1],[1],[2,4]]
cols = [[3,1],[4],[4,2],[7]]

test = Puzzle(rows,cols)
print(test.leftmost_position())