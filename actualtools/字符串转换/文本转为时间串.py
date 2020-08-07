a = "44042"
import pandas as pd
def date(stamp):
    delta = pd.Timedelta(str(stamp)+'D')
    real_time = pd.to_datetime('1899-12-30') + delta
    return real_time

print(str(date(a)).split(" ")[0])