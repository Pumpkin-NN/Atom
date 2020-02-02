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
    return sum

sum = add_time(start, duration)


# Modifier
def increment(time, seconds):
    n = seconds // 60
    m = seconds % 60

    if n == 0:
        time.second = seconds
    else:
        time.second = m
        t = n // 60
        if t == 0:
            time.minute += n
        else:
            time.minute += n % 60
            time.hour += t

    d = time.hour // 24
    if d == 0:
        time.hour = time.hour % 24
    else:
        if d == 1:
            print(f'next {d} day')
        else:
            print(f'next {d} days')
        time.hour = time.hour % 24

    print('%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second))

increment(sum, 1800000)
