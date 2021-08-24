# Beispiel Sudoku (kann geaendert werden)
sudoku = [
			[0, 0, 6, 0, 0, 0, 9, 4, 0],
			[0, 9, 0, 0, 2, 0, 7, 0, 6],
			[0, 5, 8, 0, 0, 7, 3, 0, 0],
			[6, 0, 0, 1, 8, 3, 0, 0, 7],
			[0, 0, 0, 5, 0, 0, 4, 0, 3],
			[0, 0, 9, 0, 0, 0, 8, 0, 2],
			[0, 1, 0, 6, 0, 4, 0, 8, 0],
			[2, 0, 7, 0, 0, 9, 0, 0, 0],
			[0, 0, 0, 0, 3, 0, 6, 0, 0]
		]


def printSudoku():
	for i in range(9):
		for j in range(9):
			print(str(sudoku[i][j]), end="  ")
		print()


def solveSudoku():
	pos = nextEmpty()

	if pos is None:
		return True

	for n in range(1,10):
		if isValid(pos,n):
			sudoku[pos[0]][pos[1]] = n
			if solveSudoku():
				return True
			else:
				sudoku[pos[0]][pos[1]] = 0

	return False


def nextEmpty():
	for i in range(9):
		for j in range(9):
			if sudoku[i][j]==0:
				pos = [i,j]
				return pos
	return None


def isValid(pos,n):
	for i in range(9):
		if (n == sudoku[pos[0]][i] or n == sudoku[i][pos[1]]):
			return False

	l = (pos[0] // 3) * 3
	c = (pos[1] // 3) * 3

	for i in range(l,l+3):
		for j in range(c,c+3):
			if(sudoku[i][j] == n):
				return False
	return True


if __name__ == '__main__':
	solveSudoku()
	printSudoku()

