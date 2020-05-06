from datetime import datetime

ALL_TYPES = ['2D', '3D', '4DX']


def validate_type(p_type):
    if p_type not in ALL_TYPES:
        raise ValueError(f'Projection type should be: {ALL_TYPES}')


def validate_date_and_time(p_date, p_time):
    if len(p_date == 10):
        p_year = int(p_date[:4])
        p_month = int(p_date[5:7])
        p_day = int(p_date[8:])

        if len(p_time == 5):
            p_hour = int(p_time[:2])
            p_min = int(p_time[3:])

            p_datetime = datetime(p_year, p_month, p_day, p_hour, p_min)

            if p_datetime <= datetime.today():
                raise ValueError('New projections should be in the future.')

        else:
            raise ValueError('Correct time format: `HH-MM`')
    else:
        raise ValueError('Correct data format: `YYYY-MM-DD`')
