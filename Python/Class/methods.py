class Time():
    pass
'''
T1 = Time()
T1.hour = 1
T1.second = 10
#print(hasattr(T1, "minute"))
try:
    print(T1.minute)
except:
    T1.minute = 30

print(T1.minute)

def print_time(obj):
    print('%.2d:%.2d:%.2d' % (obj.hour, obj.minute, obj.second))

print_time(T1)
'''

start = Time()
start.hour = 10
start.minute = 50
start.second = 55

duration = Time()
duration.hour = 1
duration.minute = 50
duration.second = 55

def add_time(t1, t2):
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second

    if sum.minute >= 60:
        sum.hour += 1
        sum.minute -= 60

    if sum.second >= 60:
        sum.minute += 1
        sum.second -= 60

    if sum.hour >= 24:
        sum.hour -= 24
        print("next day, ")

    print('%.2d:%.2d:%.2d' % (sum.hour, sum.minute, sum.second))

add_time(start, duration)
