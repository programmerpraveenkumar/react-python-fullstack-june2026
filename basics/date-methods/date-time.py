#import the date and time
# from moudule_name import classname
from datetime import datetime 

from zoneinfo import ZoneInfo

dt_ny = datetime.now(ZoneInfo("Asia/Dubai"))
d=datetime.now()
print(f"{dt_ny.year} {dt_ny.hour}:{dt_ny.minute}")
