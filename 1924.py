import datetime
m, d = map(int, input().split())
days= ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
b = days[datetime.date(2007, m, d).weekday()]
print(b)
