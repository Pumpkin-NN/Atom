class Time():
    pass


def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time




if __name__ == '__main__':
    t1 = Time()
    t1.hour = 3
    t1.minute = 50
    t1.second = 55
    print('%.2d:%.2d:%.2d' % (t1.hour, t1.minute, t1.second))
    print("\n")

    seconds = time_to_int(t1)
    t2 = int_to_time(seconds)
    print('%.2d:%.2d:%.2d' % (t2.hour, t2.minute, t2.second))
