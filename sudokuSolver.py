
import random
import linecache

class Sudoku:
    
    def __init__(self):
        self.loadRandom()


    def loadRandom(self):
        r = random.randint(1, 1000001)
        line = linecache.getline('sudoku.csv', r).split(',')
        self.puzzle = line[0].strip()
        self.solution = line[1].strip()

        self.board = []

        for row in range(9):
        	tmpRow = []
        	for col in range(9):
        		tmpRow.append(int(self.puzzle[row*9+col]))
        	self.board.append(tmpRow)


    def printBoard(self):
        for row in range(9):
            for col in range(9):
                print(self.board[row][col], end=" ")
            print()

    def nextEmptyCell(self):
    	for row in range(9):
    		for col in range(9):
    			if self.board[row][col] == 0:
    				return row, col
    	return -1, -1



    def checkLocation(self, row, col, digit):
    	inRow = False
    	for c in range(9):
    		if self.board[row][c] == digit:
    			inRow = True
    			break
    	inColumn = False
    	for r in range(9):
    		if self.board[r][col] == digit:
    			inColumn = True
    			break
    	inBlock = False
    	startRow = row-row%3
    	startCol = col-col%3
    	for r in range(3):
    		for c in range(3):
    			if self.board[startRow+r][startCol+c] == digit:
    				inBlock = True
    				break

    	return not inRow and not inColumn and not inBlock

    def solve(self):
    	row = 0
    	col = 0
    	row, col = self.nextEmptyCell()
    	if(row == -1 or col == -1):
    		return True

    	for digit in range(1, 10):
    		if self.checkLocation(row, col, digit):
    			self.board[row][col] = digit

    			if(self.solve()):
    				return True

    			self.board[row][col] = 0

    	return False

    def verify(self):
    	for r in range(9):
    		for c in range(9):
    			if self.board[r][c] != int(self.solution[r*9+c]):
    				return False
    	return True


    def solvePuzzle(self):
    	if self.solve():
    		return True
    	else:
    		return False

s = 0
w = 0
u = 0
for i in range(10000):
	sudoku = Sudoku()
	if sudoku.solvePuzzle():
		if sudoku.verify():
			print(".", end="")
			s += 1
		else:
			print("x", end="", flush=True)
			w += 1
	else:
		print("o", end="", flush=True)
		u += 1

print("\nS:", s)
print("W:", w)
print("U:", u)
