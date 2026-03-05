
class Puzzle: 
    """Class to solve nonograms"""
    def __init__(self, row_clues, col_clues):
        self.row_clues = row_clues
        self.col_clues = col_clues
        self.grid = self.get_grid()

    def get_grid(self):
        grid = []
        for _ in range(len(self.col_clues)):
            row = []
            for _ in range(len(self.row_clues)):
                row.append(None)
            grid.append(row)     
        return grid

    def solve(self):
        return "solution"
    
rows = [[1,2,1],[1],[2,4]]
cols = [[3,1],[4],[4,2]]


test = Puzzle(rows,cols)
print(test.get_grid())