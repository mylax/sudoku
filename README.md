# Sudoku App

- [Sudoku App](#sudoku-app)
  - [Structure](#structure)
  - [Input/Output Formats](#inputoutput-formats)

## Structure

Four Services are provided in Docker:

- DB (PostgreSQL)
- Server to connect to DB (Flask, SQLAlchemy)
- Server to provide new Sudoku games (Flask)
- FLASK Server providing Frontend (written in JS/HTML/CSS)

## Input/Output Formats

Newly created Sudoku game is provided as JSON:
{
  "initial": [
    1, 0, .., 0, 1
  ],
  "val": [
    4, 5, 1, 7, 9
    ]
}

initial dummy {0, 1} to provide information if game at start includes number or not
val takes values 1,..,9 and provides value at each cell
order of number represents the following structure:

1,2,3,10,11,12,19,20,21,28,29,30
4,5,6,13,14,15,22,23,24,31,32,33
7,8,9,16,17,18,25,26,27,34,35,36
37,38,39
40,41,42,
43,44,45
'''

up to numbers 81 for the 81 cells in a 3x3 standard sudoku format
