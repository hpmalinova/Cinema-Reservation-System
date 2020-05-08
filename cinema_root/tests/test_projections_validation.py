import unittest
from ..projections.validation import (
    validate_type,
    validate_date_and_time,
    ALL_TYPES
)


class TestValidateType(unittest.TestCase):
    def test_validate_type_passes_with_correct_input(self):
        test_p_type = "3D"

        validate_type(test_p_type)

    def test_validate_type_raises_value_error_if_unrecognized_type(self):
        test_p_type = "Test"
        exc = None

        try:
            validate_type(test_p_type)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), f'Projection type should be: {ALL_TYPES}')


class TestValidateDateAndTime(unittest.TestCase):
    def test_validate_dat_passes_with_correct_input(self):
        test_p_date = "2030-12-01"
        test_p_time = "20:00"

        validate_date_and_time(test_p_date, test_p_time)

    def test_validate_dat_raises_value_error_if_wrong_data_format_date(self):
        test_p_date = "2020-2-2"
        test_p_time = "20:00"
        exc = None

        try:
            validate_date_and_time(test_p_date, test_p_time)
        except ValueError as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Correct data format: `YYYY-MM-DD`')

    def test_validate_dat_raises_value_error_if_wrong_data_format_time(self):
        test_p_date = "2030-12-01"
        test_p_time = "7:00"
        exc = None

        try:
            validate_date_and_time(test_p_date, test_p_time)
        except ValueError as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Correct time format: `HH-MM`')

    def test_validate_dat_raises_value_error_if_dat_before_now(self):
        test_p_date = "2020-05-07"
        test_p_time = "17:00"
        exc = None

        try:
            validate_date_and_time(test_p_date, test_p_time)
        except ValueError as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'New projections should be in the future.')


if __name__ == '__main__':
    unittest.main()
