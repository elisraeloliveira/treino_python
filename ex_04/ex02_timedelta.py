# manipulando data e horas com timedelta

from datetime import datetime, timedelta

new_year = datetime(2024, 12, 31, 23, 59)

new_year = new_year + timedelta(minutes=1)

print(new_year)