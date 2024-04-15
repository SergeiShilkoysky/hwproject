import random
from datetime import datetime, timedelta

min_year = 2023
max_year = datetime.now().year

start = datetime(min_year, 1, 1, 00, 00, 00)
years = max_year - min_year + 1
end = start + timedelta(days=365 * years)


# for i in range(3):
#     random_date = start + (end - start) * random.random()
#     print(random_date)


# or a function
def gen_datetime(min_year=2023, max_year=datetime.now().year):
    # generate in format yyyy-mm-dd hh:mm:ss.000000
    start = datetime(min_year, 1, 1, 00, 00, 00)
    years = max_year - min_year + 1
    end = start + timedelta(days=365 * years)
    # print(start + (end - start) * random.random())
    return start + (end - start) * random.random()

# start = datetime.strptime('01.01.2023', '%d.%m.%Y')
# end = datetime.strptime('01.01.2024', '%d.%m.%Y')
#
# def get_random_date(self, start, end):
#     delta = end - start
#     return start + timedelta(random.randint(0, delta.days))
