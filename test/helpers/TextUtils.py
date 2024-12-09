import datetime


def compare_time(textBefore: str, textAfter: str, interval: int):
    timeBefore = datetime.datetime.strptime(
        textBefore[0:19], "%Y-%m-%d %H:%M:%S")
    timeAfter = datetime.datetime.strptime(
        textAfter[0:19].replace('T', ' '), "%Y-%m-%d %H:%M:%S")
    return compare_interval(timeBefore, timeAfter, interval)


def time_minus(textAfter: str, textBefore: str):
    timeBefore = datetime.datetime.strptime(
        textBefore, "%H%M%S")
    timeAfter = datetime.datetime.strptime(
        textAfter, "%H:%M:%S:%f")
    time_total = timeAfter - timeBefore
    while (time_total.total_seconds() < 0):
        time_del = datetime.timedelta(hours=12)
        time_total = time_total + time_del
    return str(time_total)


def time_minus_num(textAfter: str, textBefore: str):
    timeBefore = datetime.datetime.strptime(
        textBefore, "%H%M%S")
    timeAfter = datetime.datetime.strptime(
        textAfter, "%H:%M:%S:%f")
    time_total = timeAfter - timeBefore
    while (time_total.total_seconds() < 0):
        time_del = datetime.timedelta(hours=12)
        time_total = time_total + time_del
    return time_total.total_seconds()


def compare_minus(new_sample: str, new_context: str, old_sample: str, old_context: str):
    upper_limit_scale = 1.2
    lower_limit_scale = 0.8
    old_sample = (datetime.datetime.strptime(old_sample, "%H:%M:%S.%f") -
              datetime.datetime(1900, 1, 1)).total_seconds()
    old_context = (datetime.datetime.strptime(old_context, "%H:%M:%S.%f") -
               datetime.datetime(1900, 1, 1)).total_seconds()
    new_sample = (datetime.datetime.strptime(new_sample, "%H:%M:%S.%f") -
              datetime.datetime(1900, 1, 1)).total_seconds()
    new_context = (datetime.datetime.strptime(new_context, "%H:%M:%S.%f") -
               datetime.datetime(1900, 1, 1)).total_seconds()
    print(new_sample - old_sample)
    print(new_context - old_context)
    print((new_sample - old_sample) * upper_limit_scale)
    print((new_sample - old_sample) * lower_limit_scale)
    return (((new_sample - old_sample) * upper_limit_scale > (new_context - old_context) and (new_sample - old_sample) * lower_limit_scale < (new_context - old_context)) and (new_sample - old_sample) < 2)



def compare_seconds(sample: str, context: str):
    sample = (datetime.datetime.strptime(sample, "%H:%M:%S.%f") -
              datetime.datetime(1900, 1, 1)).total_seconds()
    context = (datetime.datetime.strptime(context, "%H:%M:%S.%f") -
               datetime.datetime(1900, 1, 1)).total_seconds()
    return (abs(sample - context) < 0.5)


def compare_day(textBefore: str, textAfter: str, interval: int):
    timeBefore = datetime.datetime.strptime(textBefore, "%Y%m%d")
    timeAfter = datetime.datetime.strptime(
        textAfter[0:10].replace('T', ' '), "%Y-%m-%d")
    return compare_interval(timeBefore, timeAfter, interval)


def compare_interval(timeBefore: datetime, timeAfter: datetime, interval: int):
    for i in range(-1 * interval, 1 + interval):
        timeDelta = datetime.timedelta(seconds=i)
        timeCompare = timeAfter + timeDelta
        if(timeBefore == timeCompare):
            return True
    return False


def compare_battery(textBattery: str, systemBattery: str):
    for i in range(-1, 2):
        if (textBattery.replace('%', '').replace(' ', '') == str(int(systemBattery) + i)):
            return True
    return False


def compare_driverPackage(packageText: str, expectedPackage: str):
    return packageText == expectedPackage
