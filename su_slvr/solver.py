import numpy as np
import re
import datetime

sudoku = np.array([5, 3, 4, 6, 7, 2, 1, 9, 8, 6, 7, 8, 1, 9, 5, 3, 4, 2, 9, 1, 2, 3, 4, 8,
5, 6, 7, 8, 5, 9, 4, 2, 6, 7 , 1, 3, 7, 6, 1, 8, 5, 3, 9, 2, 4, 4, 2, 3, 7, 9, 1, 8, 5, 6, 9, 6, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 1 ,9, 0, 0, 0, 2, 8, 0, 0, 0, 5, 0, 7, 0])


# sudoku = np.array([0, 3, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 1, 9, 5, 0, 0, 0, 0, 0,
# 0, 0, 0, 0, 0, 6, 0, 8, 0, 0, 4, 0, 0, 0 , 0, 0, 0, 6, 0, 8, 0, 0, 0, 2, 0, 0, 0, 0,
# 0, 0, 1, 0, 0, 0, 0, 6, 0,
# 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 1 ,9, 0, 0, 0, 2, 8, 0, 0, 0, 5, 0, 7, 0])



def contains_duplicates(X):
    X = np.delete(X, np.where(X == 0))
    return len(np.unique(X)) != len(X)

def isValid(sudoku):
    columnindex = [0, 3, 6, 27, 30, 33, 54, 57, 60]
    rowindex = [0, 1, 2, 9, 10, 11, 18, 19, 20]
    for i in range(9):
        if contains_duplicates(sudoku[0+9*i:9+9*i]):
            return False

    for i in [0, 1, 2, 9, 10, 11, 18, 19, 20]:
        column = [x + i for x in columnindex]
        if contains_duplicates(sudoku[column]):
            return False

        row = [x + 3 * i for x in rowindex]
        if contains_duplicates(sudoku[row]):
            return False
    return True

def next_step_valid(arr):
    '''
    next_step([1, 0, 0]) = next_step([1, 1, 0])
    next_step([1, 1, 1]) = next_step([1, 2, 1])
    next_step([1, , 9]) = next_step([2, 1, 1])
    '''
    arr[np.where(arr == 0)[0][0]] = 1
    return arr

def next_step_not_valid(arr):
    '''
    next_step([1, 0, 0]) = next_step([2, 0, 0])
    next_step([9, 1, 1]) = next_step([1, 2, 1])
    next_step([1, 1, 9]) = next_step(1, 2, 0])
    '''
    index_where_0 = np.where(arr == 0)[0]
    if index_where_0.size > 0:
        last_index = index_where_0[0]
        test = [str(x) for x in arr[0:last_index]]
        result = [int(x) for x in list(re.sub("0", "1", str(int("".join(test)) + 1)))]
        arr[0:last_index] = result
    else:
        test = [str(x) for x in arr]
        result = [int(x) for x in list(re.sub("0", "1", str(int("".join(test)) + 1)))]
        arr = result
    return arr



indices = np.where(sudoku == 0)[0]

trying = np.array([1] + [0] * (indices.size - 1))
sudoku[indices] = trying

begin = datetime.datetime.now()

while (True):
    if isValid(sudoku):
        if np.where(trying==0)[0].size == 0:
            break
        trying = next_step_valid(trying)

    else:
        trying = next_step_not_valid(trying)
    sudoku[indices] = trying
    print(trying)


end = datetime.datetime.now()


print(end - begin)