import random
import pandas as pd

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

def solve_problem(sudoku, total = 0):
    global WRAPPER
    WRAPPER = []
    try:
        reduce_possibility(sudoku, total)
        return WRAPPER
    except:
        return []

def reduce_possibility(sudoku, total):
    if total > 3:
        raise ValueError("a specfic thing happend")
    sudoku = find_max_fixed(sudoku)
    possibles = calc_possibles(sudoku)
    len_possibles = []
    for key in possibles:
        len_possibles.append([key, len(possibles[key])])

    if max([x[1] for x in len_possibles]) == 1:
        WRAPPER.append(list(possibles.values()))
    else:
        min_possibles = min([x[1] for x in len_possibles if x[1] > 1])
        len_poss = [x[1] for x in len_possibles]
        indices = [i for i, e in enumerate(len_poss) if e == min_possibles]
        for index in indices:
            possibles_one_element = possibles[len_possibles[index][0]]
            for possibility in possibles_one_element:
                this_possible = possibles.copy()
                this_possible[len_possibles[index][0]] = [possibility]
                reduce_possibility(dict_to_list(this_possible), total + 1)


def drop_ele(init_sudoku):
    iterate = list(range(len(init_sudoku)))
    random.shuffle(iterate)
    for i in iterate:
        new_sudoku = init_sudoku.copy()
        del new_sudoku[i]
        result = solve_problem(new_sudoku, 0)
        if len(result) == 1:
            return new_sudoku
        if len(result) == 2 and result[0] == result[1]:
            return new_sudoku
    return init_sudoku


def find_lowest(init_sudoku):
    old_len = len(init_sudoku)

    while old_len > len(drop_ele(init_sudoku)):
        init_sudoku = drop_ele(init_sudoku)
        old_len = len(init_sudoku)

    return init_sudoku

def swap_row_and_col(sudoku):
    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    random.shuffle(a)
    random.shuffle(a[0])
    index_to_swap = a[0][:2]
    return_sud = pd.DataFrame(sudoku, columns = ["val", "row", "col", "cell"])

    for key, val in {"row":1, "col":2}.items() :

        first_vals = [x[0] for x in sudoku if x[val] == index_to_swap[0]]
        second_vals =  [x[0] for x in sudoku if x[val] == index_to_swap[1]]
        return_sud.loc[return_sud[key] == index_to_swap[0], "val"] = second_vals
        return_sud.loc[return_sud[key] == index_to_swap[1], "val"] = first_vals
    return return_sud.values.tolist()

def rename_elements(sudoku):
    a = list(range(1, 10))
    random.shuffle(a)
    rename_dict = dict(zip(list(range(1, 10)), a))
    return [[rename_dict[x[0]], x[1], x[2], x[3]] for x in sudoku]


def transform_sudoku(sudoku):
    for _i in range(100):
        sudoku = swap_row_and_col(sudoku)
        sudoku = rename_elements(sudoku)
    return sudoku

def find_sudoku():
    sudoku_full = [[5, 1, 1, 1], [6, 2, 1, 1], [1, 3, 1, 1], [8, 4, 1, 4], [4, 5, 1, 4], [7, 6, 1, 4], [9, 7, 1, 7], [2, 8, 1, 7], [3, 9, 1, 7], [3, 1, 2, 1], [7, 2, 2, 1], [9, 3, 2, 1], [5, 4, 2, 4], [2, 5, 2, 4], [1, 6, 2, 4], [6, 7, 2, 7], [8, 8, 2, 7], [4, 9, 2, 7], [4, 1, 3, 1], [2, 2, 3, 1], [8, 3, 3, 1], [9, 4, 3, 4], [6, 5, 3, 4], [3, 6, 3, 4], [1, 7, 3, 7], [7, 8, 3, 7], [5, 9, 3, 7], [6, 1, 4, 2], [1, 2, 4, 2], [3, 3, 4, 2], [7, 4, 4, 5], [8, 5, 4, 5], [9, 6, 4, 5], [5, 7, 4, 8], [4, 8, 4, 8], [2, 9, 4, 8], [7, 1, 5, 2], [9, 2, 5, 2], [4, 3,
    5, 2], [6, 4, 5, 5], [5, 5, 5, 5], [2, 6, 5, 5], [3, 7, 5, 8], [1, 8, 5, 8], [8, 9, 5, 8], [8, 1, 6, 2], [5, 2, 6, 2], [2, 3, 6, 2], [1, 4, 6, 5], [3, 5, 6, 5], [4, 6, 6, 5], [7, 7, 6, 8], [9, 8, 6, 8], [6, 9, 6, 8], [9, 1, 7, 3], [3, 2, 7, 3], [5, 3, 7, 3], [4, 4, 7, 6], [7, 5, 7, 6], [8, 6, 7, 6], [2, 7, 7, 9], [6, 8, 7, 9], [1, 9, 7, 9], [1, 1, 8, 3], [4, 2, 8, 3], [6, 3, 8, 3], [2, 4, 8, 6], [9, 5, 8, 6], [5, 6, 8, 6], [8, 7, 8, 9], [3, 8, 8, 9], [7, 9, 8, 9], [2, 1, 9, 3], [8, 2, 9, 3], [7, 3, 9, 3], [3, 4, 9, 6], [1, 5, 9, 6], [6, 6, 9, 6], [4, 7, 9, 9], [5, 8, 9, 9], [9, 9, 9, 9]]

    # sudoku_full = transform_sudoku(sudoku_full)
    sudoku_with_initial = [x + [1] for x in sudoku_full]
    sudoku = find_lowest(sudoku_full)
    df_full = pd.DataFrame(sudoku_with_initial, columns = ["val", "row", "col", "cell", "initial"])
    df_solved = pd.DataFrame(sudoku, columns = ["val", "row", "col", "cell"])
    merged = df_full.merge(df_solved, how = "left", on=["row", "col"])
    merged.loc[merged["val_y"].isna(), "initial"] = 0

    order = [11, 12, 13, 21, 22, 23, 31, 32, 33, 14, 15, 16, 24, 25, 26, 34, 35, 36, 17, 18, 19, 27, 28, 29, 37, 38, 39,
41, 42, 43, 51, 52, 53, 61, 62, 63, 44, 45, 46, 54, 55, 56, 64, 65, 66, 47, 48, 49, 57, 58, 59, 67, 68, 69,
71, 72, 73, 81, 82, 83, 91, 92, 93, 74, 75, 76, 84, 85, 86, 94, 95, 96, 77, 78, 79, 87, 88, 89, 97, 98, 99]

    result = pd.DataFrame({}, columns = ["val_x", "initial"])
    for elem in order:
        elem_char = str(elem)
        row = int(elem_char[0])
        col = int(elem_char[1])
        row_to_append = merged.loc[(merged["row"] == row) & (merged["col"] == col), ["val_x", "initial"]]
        result = result.append(row_to_append)

    result.columns = ["val", "initial"]
    result.index += 1
    return result


# sudoku = [[5, 1, 1, 1], [6, 2, 1, 1], [1, 3, 1, 1], [8, 4, 1, 4], [4, 5, 1, 4], [7, 6, 1, 4], [9, 7, 1, 7], [2, 8, 1, 7], [3, 9, 1, 7], [3, 1, 2, 1], [7, 2, 2, 1], [9, 3, 2, 1], [5, 4, 2, 4], [2, 5, 2, 4], [1, 6, 2, 4], [6, 7, 2, 7], [8, 8, 2, 7], [4, 9, 2, 7], [4, 1, 3, 1], [2, 2, 3, 1], [8, 3, 3, 1], [9, 4, 3, 4], [6, 5, 3, 4], [3, 6, 3, 4], [1, 7, 3, 7], [7, 8, 3, 7], [5, 9, 3, 7], [6, 1, 4, 2], [1, 2, 4, 2], [3, 3, 4, 2], [7, 4, 4, 5], [8, 5, 4, 5], [9, 6, 4, 5], [5, 7, 4, 8], [4, 8, 4, 8], [2, 9, 4, 8], [7, 1, 5, 2], [9, 2, 5, 2], [4, 3,
# 5, 2], [6, 4, 5, 5], [5, 5, 5, 5], [2, 6, 5, 5], [3, 7, 5, 8], [1, 8, 5, 8], [8, 9, 5, 8], [8, 1, 6, 2], [5, 2, 6, 2], [2, 3, 6, 2], [1, 4, 6, 5], [3, 5, 6, 5], [4, 6, 6, 5], [7, 7, 6, 8], [9, 8, 6, 8], [6, 9, 6, 8], [9, 1, 7, 3], [3, 2, 7, 3], [5, 3, 7, 3], [4, 4, 7, 6], [7, 5, 7, 6], [8, 6, 7, 6], [2, 7, 7, 9], [6, 8, 7, 9], [1, 9, 7, 9], [1, 1, 8, 3], [4, 2, 8, 3], [6, 3, 8, 3], [2, 4, 8, 6], [9, 5, 8, 6], [5, 6, 8, 6], [8, 7, 8, 9], [3, 8, 8, 9], [7, 9, 8, 9], [2, 1, 9, 3], [8, 2, 9, 3], [7, 3, 9, 3], [3, 4, 9, 6], [1, 5, 9, 6], [6, 6, 9, 6], [4, 7, 9, 9], [5, 8, 9, 9], [9, 9, 9, 9]]


# for _i in range(100):
#     sudoku = swap_row_and_col(sudoku)
# test = pd.DataFrame(sudoku, columns = ["val", "row", "col", "cell"])
# test.index += 1
# ids = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 19, 20, 21, 28, 31, 34, 55, 58, 61]
# test.ix[1]["val"]
# test.ix[ids]["val"]

# a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# random.shuffle(a)
# random.shuffle(a[0])
# index_to_swap = a[0][:2]
# return_sud = pd.DataFrame(sudoku, columns = ["val", "row", "col", "cell"])

# for key, val in {"row":1, "col":2}.items() :
#     first_vals = [x[0] for x in sudoku if x[val] == index_to_swap[0]]
#     second_vals =  [x[0] for x in sudoku if x[val] == index_to_swap[1]]
#     return_sud.loc[return_sud[key] == index_to_swap[0], "val"] = second_vals
#     return_sud.loc[return_sud[key] == index_to_swap[1], "val"] = first_vals