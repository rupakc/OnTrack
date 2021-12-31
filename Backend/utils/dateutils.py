import datetime


def get_python_date_from_tweet(tweet_date_string,format='%a %b %d %H:%M:%S +0000 %Y'):
    tweet_date = datetime.datetime.strptime(tweet_date_string,format)
    return tweet_date


def get_datestring_from_python_date(python_datetime):
    return python_datetime.__str__()


def parse_datetime_finance_string(datetime_string_list):
    datetime_object_values = []
    for datetime_string in datetime_string_list:
        datetime_split_list = datetime_string.strip().split(' ')
        date_part,time_part = datetime_split_list[0],datetime_split_list[1]
        total_time_components = date_part.split('-')
        total_time_components.extend(time_part.split(':'))
        d = datetime.datetime(*(int(c) for c in total_time_components))
        datetime_object_values.append(d)
    return datetime_object_values


def get_increased_date_values(date_string_list,num_increase,increment_unit):
    date_object_values = []
    for date_string in date_string_list:
        if increment_unit == 'intraday':
            date_object_values = parse_datetime_finance_string(date_string_list)
        else:
            d = datetime.date(*(int(s) for s in date_string.strip().split('-')))
            date_object_values.append(d)
    for i in range(num_increase):
        if increment_unit == 'daily':
            increased_date = date_object_values[-1] + datetime.timedelta(days=1)
        elif increment_unit == 'monthly':
            increased_date = date_object_values[-1] + datetime.timedelta(days=30)
        elif increment_unit == 'weekly':
            increased_date = date_object_values[-1] + datetime.timedelta(weeks=1)
        else:
            increased_date = date_object_values[-1] + datetime.timedelta(minutes=15)
        date_object_values.append(increased_date)
    date_object_values = map(str,date_object_values)
    return date_object_values
