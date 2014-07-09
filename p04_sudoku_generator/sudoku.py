def gridSudoku(sudoku_values):
    sudoku_ascii = str()
    for idx_row, row in enumerate(sudoku):
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
