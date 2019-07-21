
# FIRST STEP CREATE DICTIONARY WITH POSSIBLE VALUES

from operator import itemgetter



def find_cell(row, col):
    if row <= 3 and col <= 3:
        return 1
    if row <= 3 and col <= 6:
        return 2
    if row <= 3:
        return 3
    if row <= 6 and col <= 3:
        return 4
    if row <= 6 and col <= 6:
        return 5
    if row <= 6:
        return 6
    if col <= 3:
        return 7
    if col <= 6:
        return 8
    return 9



# find minimal unique possibilities
def dict_to_list(possibles):
    new_sudoku = []
    for key, val in possibles.items():
        if len(val) == 1:
            col = int(str(key)[0])
            row = int(str(key)[1])
            cell = find_cell(row, col)
            new_sudoku.append([val[0], row, col, cell])
    return new_sudoku


def find_max_fixed(sudoku):
    old_len = len(sudoku)
    possibles = calc_possibles(sudoku)
    sudoku = dict_to_list(possibles)
    while old_len < len(sudoku):
        old_len = len(sudoku)
        possibles = calc_possibles(sudoku)
        sudoku = dict_to_list(possibles)
    return sudoku

def calc_possibles(sudoku):
    mydict = {}
    for row in range(1, 10):
        for col in range(1, 10):
            loc = int(str(row) + str(col))
            cell = find_cell(row, col)
            row_values = [x[0] for x in sudoku if x[1] == row]
            col_values = [x[0] for x in sudoku if x[2] == col]
            cell_values = [x[0] for x in sudoku if x[3] == cell]
            blockedvalues = row_values + col_values + cell_values
            possibles = [x for x in range(1, 10) if x not in blockedvalues]
            prev_val = [x for x in sudoku if x[1] == row and x[2] == col]
            if prev_val:
                mydict[loc] = [prev_val[0][0]]
            else:
                mydict[loc] = possibles
    return mydict


# use recursion to go down possibility tree
# if there is a memory error then the solution has to many possibilites anyway
def reduce_possibility(sudoku):
    sudoku = find_max_fixed(sudoku)
    possibles = calc_possibles(sudoku)
    len_possibles = []
    for key in possibles:
        len_possibles.append([key, len(possibles[key])])

    if max([x[1] for x in len_possibles]) == 1:
        print(possibles)
    else:
        min_possibles = min([x[1] for x in len_possibles if x[1] > 1])
        len_poss = [x[1] for x in len_possibles]
        indices = [i for i, e in enumerate(len_poss) if e == min_possibles]
        for index in indices:
            possibles_one_element = possibles[len_possibles[index][0]]
            for possibility in possibles_one_element:
                this_possible = possibles.copy()
                this_possible[len_possibles[index][0]] = [possibility]
                reduce_possibility(dict_to_list(this_possible))





# val, row, column, cell
sudoku = [
    #[5, 1, 1, 1],
    #[3, 1, 2, 1],
    [6, 2, 1, 1],
    [9, 3, 2, 1],
    [8, 3, 3, 1],
    [1, 2, 4, 2],
    [7, 1, 5, 2],
    [9, 2, 5, 2],
    [5, 2, 6, 2],
    [6, 3, 8, 3],
    [8, 4, 1, 4],
    [4, 5, 1, 4],
    [7, 6, 1, 4],
    [6, 4, 5, 5],
    [8, 5, 4, 5],
    [3, 5, 6, 5],
    [2, 6, 5, 5],
    [3, 4, 9, 6],
    [1, 5, 9, 6],
    [6, 6, 9, 6],
    [6, 7, 2, 7],
    [4, 8, 4, 8],
    [1, 8, 5, 8],
    [9, 8, 6, 8],
    [8, 9, 5, 8],
    [2, 7, 7, 9],
    [8, 7, 8, 9],
    [5, 8, 9, 9],
    [7, 9, 8, 9],
    [9, 9, 9, 9]
]

reduce_possibility(sudoku)
