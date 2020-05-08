import unittest
from ..reservations.validation import (
    validate_row, validate_col,
    FIRST_ROW, FIRST_COL,
    LAST_ROW, LAST_COL
)


class TestValidateRow(unittest.TestCase):
    def test_validate_row_passes_with_correct_input(self):
        test_row = 5

        validate_row(test_row)

    def test_validate_row_raises_value_error_if_row_greater_than_allowed(self):
        test_row = 14
        exc = None

        try:
            validate_row(test_row)
        except ValueError as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), f'Row should be between {FIRST_ROW} and {LAST_ROW}')

    def test_validate_row_raises_value_error_if_row_less_than_allowed(self):
        test_row = 0
        exc = None

        try:
            validate_row(test_row)
        except ValueError as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), f'Row should be between {FIRST_ROW} and {LAST_ROW}')


class TestValidateCol(unittest.TestCase):
    def test_validate_col_passes_with_correct_input(self):
        test_col = 5

        validate_col(test_col)

    def test_validate_col_raises_value_error_if_col_greater_than_allowed(self):
        test_col = 14
        exc = None

        try:
            validate_col(test_col)
        except ValueError as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), f'Col should be between {FIRST_COL} and {LAST_COL}')

    def test_validate_col_raises_value_error_if_col_less_than_allowed(self):
        test_col = 0
        exc = None

        try:
            validate_col(test_col)
        except ValueError as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), f'Col should be between {FIRST_COL} and {LAST_COL}')


if __name__ == '__main__':
    unittest.main()
