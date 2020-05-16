import sys
import pprint

def error(err):
	print(err)
	sys.exit()

def parseData(data):
    counter = 0
    tabData = []
    line = []
    for char in data:
        if (char.isdigit()):
            line.append(int(char))
            counter += 1
        if (counter == 9):
            counter = 0
            tabData.append(line)
            line =  []
    return (tabData)

def findZero(board):

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)

def checkIfSolvable(board):
    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if (board[i][j] > 9 or board[i][j] < 0):
                error('One of the number is invalid.')
            if (board[i][j] > 0 and board[i].count(board[i][j]) > 1):
                error('invalid, twice same number in row.')
            for k in range(0, len(board)):
                if (board[k][j] == board[i][j] and k != i and board[k][j] != 0 and board[i][j] != 0):
                    error('invalid, twice same number in column')

            box_x = j // 3
            box_y = i // 3

            for m in range(box_y*3, box_y*3 + 3):
                for n in range(box_x*3, box_x*3 + 3):
                    if (board[i][j] == board[m][n] and m != i and n != j and board[i][j] != 0 and board[m][n] != 0):
                        error('invalid, twice same number in box')
    return (board)

def isValid(board, pos, num):

    for i in range(0, len(board)):
            if (board[pos[0]][i] == num):
                return (False)

    for i  in range(0, len(board)):
        if (board[i][pos[1]] == num):
            return (False)

    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if board[i][j] == num:
                return (False)

    return (True)

def solve(board):

    find = findZero(board)
    if find:
        row, col = find
    else:
        return (True)

    for i in range(1,10):
        if (isValid(board, (row, col),  i)):
            board[row][col] = i

            if solve(board):
                return (True)

            board[row][col] = 0

    return (False)


if __name__ == '__main__':
    if (len(sys.argv) != 2):
        error('python main.py [file]')
    file = open(sys.argv[1])
    data = file.read()
    pp = pprint.PrettyPrinter(width=41, compact=True)
    board = parseData(data)
    Board = checkIfSolvable(board)
    solve(Board)
    pp.pprint(Board)
