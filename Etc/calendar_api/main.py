import requests
import json
from key import SERVICEKEY


# 공휴일 받아오기
def get_request_query(url, operation, params, serviceKey):
    import urllib.parse as urlparse
    params = urlparse.urlencode(params)
    request_query = url + '/' + operation + '?' + params + '&' + 'serviceKey' + '=' + serviceKey
    return request_query

URL = 'http://apis.data.go.kr/B090041/openapi/service/SpcdeInfoService'
OPERATION = 'getHoliDeInfo' 

solYear  = '2021' 
solMonth = '09' 
PARAMS = {'solYear':solYear, '_type':'json', 'numOfRows':'30'}
request_query = get_request_query(URL, OPERATION, PARAMS, SERVICEKEY)
response = requests.get(url=request_query)
holiday = list()

if True == response.ok:
    items = response.json().get("response").get("body").get("items").get("item")
    for item in items:
        if item["isHoliday"] == "Y":
            locdate = str(item["locdate"])
            formatLocdate = locdate[0:4] + "-" + locdate[4:6] + "-" + locdate[6:8]
            holiday.append(formatLocdate)



# 쉬는 주말 받아오기
import calendar
import numpy as np
calendar.setfirstweekday(6)
weekdays = list()
year = 2021
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
for month in months:
    fromatDate = str(year)
    for idx, week in enumerate(calendar.monthcalendar(year, month), start=1):
        s_month = str(month).zfill(2)
        s_saturday = str(week[6]).zfill(2)
        s_sunday = str(week[0]).zfill(2)
        # 둘째, 넷째 토요일은 영업일
        if (idx == 2 or idx == 4):
            if (week[0] != 0):
                weekdays.append(str(year) + "-" + s_month + "-" + s_sunday)
        else:
            if (week[0] != 0):
                weekdays.append(str(year) + "-" + s_month + "-" + s_sunday)
            if (week[6] != 0):
                weekdays.append(str(year) + "-" + s_month + "-" + s_saturday)



# 합치기
kimchi_holiday = holiday + weekdays
print(kimchi_holiday)