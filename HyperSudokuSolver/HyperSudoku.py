#################################################################
#                                                               #
#    Define any helper functions you need in this file only.    #
#    You will be handing in HyperSudoku.py, nothing else.       #
#                                                               #
#    A few test cases are provided in Test.py. You can test     #
#    Your code by running: (See the file for more details)      #
#               python Test.py                                  #
#    in the directory where the files are located.              #
#                                                               #
#    We're using Python 3.X this time.                          #
#                                                               #
#################################################################


class HyperSudoku:

    class SudokuNode:

        def __init__(self, x,y):
            self.x = x
            self.y = y
            self.affectededges = []
            self.possibleValues = pow(2,9);
            self.visited = 0;
            self.value = None
            
        def __eq__(self, other):

            return self.x == other.x and self.y == other.y

        def connect(self, node: HyperSudoku.SudokuNode):
            # # check for the edge in O(1)
            # if self.edgeCoords[node.x] & (1 << (node.y - 1)) == 0:
            #     self.affectededges.append(node)
            #     self.edgeCoords[node.x] |= (1 << (node.y - 1))
            #     node.connect(self)
        
        # def connectUnAffected(self, node: HyperSudoku.SudokuNode):
        #     self.unaffectededges.append(node)

        def setPossibleValues(self, possibleValues):
            pass

        def removeValueFromAffectedEdges(self, val:int):
            pass

        def removeValue(self, val: int):
            # run in O(1)
            # self.possibleValues = self.possibleValues & ~(1 << (val - 1))
            pass
        def addValue(self, val: int):
            
            # self.possibleValues = self.possibleValues | (1 << (val - 1))
            pass
        def getPossibleValues(self, val: int): # O(n) :(
            # L = []
            # for i in range(9):
            #     if self.possibleValues & (1 << i) > 0:
            #         L.append(i+1) 
            # return L
            pass

    @staticmethod
    def solve(grid):
        """
        Input: An 9x9 hyper-sudoku grid with numbers [0-9].
                0 means the spot has no number assigned.
                grid is a 2-Dimensional array. Look at
                Test.py to see how it's initialized.

        Output: A solution to the game (if one exists),
                in the same format. None of the initial
                numbers in the grid can be changed.
                'None' otherwise.
        """

        
        return None     # Update this to return correctly

    def _isAffected(self, x1,y1,x2,y2):
        
        # check if same column or same row
        if x1 == x2:
            return True
        
        if y1 == y2:
            return True

        # check for normal squares
        for k in range(0,3,3):

            if 0 + k <= x1 <= 2 + k and 0 + k <= x2 <= 2 + k:
                
                for j in range(0,3,3):
                    if 0 + j <= y1 <= 2 + j and 0 + j <= y2 <= 2 + j:
                        return True
        
        # check for hyper squares
        for k in range(0,2,5):

            if 1 + k <= x1 <= 3 + k and 1 + k <= x2 <= 3 + k:
                    
                for j in range(0,3,3):
                    if 1 + j <= y1 <= 3 + j and 1 + j <= y2 <= 3 + j:
                        return True
        return False


    def getPossibleValuesSquare(self, grid, x,y):

        x_sq = int(x/3)
        y_sq = int(y/3)
        possibleValues = pow(2,9)
        for i in range(0,3):
            for j in range(0,3):
                possibleValues = possibleValues & ~(1 << (grid[i + y_sq * 3][j + x_sq * 3] - 1)) 

        return possibleValues


    def getPossibleValuesRowsCols(self, grid, x,y):
        possibleValues = pow(2,9)
        for i in range(9):

            if grid[i][x] != 0:
                possibleValues = possibleValues & ~(1 << (grid[i][x] - 1)) 
            
            if grid[y][i] != 0:
                possibleValues = possibleValues & ~(1 << (grid[y][i] - 1)) 

        return possibleValues
    
    

    def _buildGraph(self, grid):
        graphs = []

        for i in range(9):
            for j in range(9):
                
                if grid[i][j] == 0:
                    
                    node = HyperSudoku.SudokuNode(j,i)
                    
                    # calculate intersect of two bitmaps
                    node.setPossibleValues(self.getPossibleValuesRowsCols(grid, j, i) & self.getPossibleValuesSquare(grid, j, i))
                    
                    graphs.append(node)


    def _solveGraph(self, start: SudokuNode):

        for i in range(len(start.edges)):
            possible_values = start.getPossibleValues()

            if len(possible_values) != 0:
                for v in possible_values:
                    
                    # set first possible value 
                    start.value = v
                    
                    # remove the value from its list
                    start.removeValue(v)

                    # remove the value from all affected nodes
                    start.removeValueFromAffectedEdges(v)

                    # mark itself as visited
                    start.visited = 1

                    if not self._solveGraph(start.edges[i]):
                        start.visited = 0
                        start.addValue(v)
                        self.edges[i].addValue(v)
                    else:
                        return True
            else:
                return False
        return False


    @staticmethod
    def printGrid(grid):
        """
        Prints out the grid in a nice format. Feel free
        to change this if you need to, it will NOT be 
        used in marking. It is just to help you debug.

        Use as:     HyperSudoku.printGrid(grid)
        """
        print("-"*25)
        for i in range(9):
            print("|", end=" ")
            for j in range(9):
                print(grid[i][j], end=" ")
                if (j % 3 == 2):
                    print("|", end=" ")
            print()
            if (i % 3 == 2):
                print("-"*25)
