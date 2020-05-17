from datetime import datetime

ALL_TYPES = ['2D', '3D', '4DX']
ALL_UPDATES = ['type', 'date', 'time']


def validate_type(projection_type):
    if projection_type not in ALL_TYPES:
        raise ValueError(f'Projection type should be: {ALL_TYPES}')


def validate_date_and_time(projection_date, projection_time):
    if len(projection_date) == 10:
        p_year = int(projection_date[:4])
        p_month = int(projection_date[5:7])
        p_day = int(projection_date[8:])

        if len(projection_time) == 5:
            p_hour = int(projection_time[:2])
            p_min = int(projection_time[3:])

            p_datetime = datetime(p_year, p_month, p_day, p_hour, p_min)

            if p_datetime <= datetime.today():
                raise ValueError('New projections should be in the future.')

        else:
            raise ValueError('Correct time format: `HH-MM`')
    else:
        raise ValueError('Correct data format: `YYYY-MM-DD`')
