import random

def gridSudoku(sudoku_values):
    sudoku_ascii = str()
    for idx_row, row in enumerate(sudoku_values):
        row_ascii = ' '
        for idx_number, number in enumerate(row):
            if number == 0:
                row_ascii += '.'
            else:
                row_ascii += str(number)
            if idx_number == 2 or idx_number == 5:
                row_ascii += ' | '
            else:
                row_ascii += ' '
        row_ascii += '\n'
        sudoku_ascii += row_ascii
        if idx_row == 2 or idx_row == 5:
            sudoku_ascii += ' ------+-------+-------\n'
    return sudoku_ascii

def genEmptySudoku():
    empty_sudoku = list()
    empty_sudoku = [[0]*9]*9
    return empty_sudoku

def randomSudoku():
    sudoku = list()
    for row in xrange(9):
        row_list = list()
        for number in xrange(9):
            row_list.append(random.randint(1,9))
        sudoku.append(row_list)
    return sudoku
            
    return [[random.randint(0,9)]*9]*9

def checkRow(number, row, sudoku):
    return sudoku[row].count(number) == 0

def checkColumn(number, column, sudoku):
    column_list = list()
    for row in sudoku:
        column_list.append(row[column])
    return column_list.count(number) == 0

def checkBlock(number, block, sudoku):
    block_list = list()
    block_starters = [(0,0),(0,3),(0,6),(3,0),(3,3),(3,6),(6,0),(6,3),(6,6)]
    row_start, column_start  = block_starters[block]
    for row in xrange(row_start, row_start+3):
        for column in xrange(column_start, column_start+3):
            block_list.append(sudoku[row][column])
    return block_list.count(number) == 0

def findBlock(coordinates_number):
    row, column = coordinates_number
    if row < 3:
        if column < 3:
            return 0
        elif column < 6:
            return 1
        else:
            return 2
    elif row < 6:
        if column < 3:
            return 3
        elif column < 6:
            return 4
        else:
            return 5
    else:
        if column < 3:
            return 6
        elif column < 6:
            return 7
        else:
            return 8
    
def checkRules(number, coordinates_number, sudoku):
    row, column = coordinates_number
    block = findBlock(coordinates_number)
    return checkRow(number, row, sudoku) #and checkColumn(number, column, sudoku) and checkBlock(number, block, sudoku)

def genNumber(coordinates_number, sudoku):
    row_number, column_number = coordinates_number
    possibilities = list()
    for number in xrange(1,10):
        if checkRules(number, coordinates_number, sudoku):
            possibilities.append(number)
    number = random.choice(possibilities)
    return number
    
def genSudoku():
    sudoku_values = genEmptySudoku()
    for row in xrange(9):
        for column in xrange(9):
            sudoku_values[row][column] = genNumber((row,column),sudoku_values)
    return sudoku_values

if __name__ == '__main__':
    sudoku = genSudoku()
    print gridSudoku(sudoku)
