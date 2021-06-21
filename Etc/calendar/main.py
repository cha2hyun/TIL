#1,3,5째주 토요일 구하기
from datetime import datetime, timedelta

def get_date(y, m, d):    
    s = f'{y:04d}-{m:02d}-{d:02d}'
    return datetime.strptime(s, '%Y-%m-%d')

def get_week_no():
    target = datetime.today()
    firstday = target.replace(day=1)
    
    if firstday.weekday() == 6:
        origin = firstday
    elif firstday.weekday() < 6:
        origin = firstday - timedelta(days=firstday.weekday() + 1)
    else:
        origin = firstday + timedelta(days=6-firstday.weekday())

    print(target.weekday())

    return (target - origin).days // 7 + 1

print(get_week_no())
today_1 = datetime.today().strftime('%Y-%m-%d')
print(type(today_1))

# print(datetime.today().strptime('%Y-%m-%d'))