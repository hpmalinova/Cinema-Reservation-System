FIRST_ROW = 1
LAST_ROW = 10
FIRST_COL = 1
LAST_COL = 10


def validate_row(row):
    if row < FIRST_ROW or row > LAST_ROW:
        raise ValueError(f'Row should be between {FIRST_ROW} and {LAST_ROW}')


def validate_col(col):
    if col < FIRST_COL or col > LAST_COL:
        raise ValueError(f'Col should be between {FIRST_COL} and {LAST_COL}')
