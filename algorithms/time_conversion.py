#!/bin/python3


def timeConversion(s):
    """
    Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
    Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock. 
    """
    s_ = s.split(':')
    hr = s_[0]
    mn = s_[1]
    sc = ''.join([x for x in s_[-1]][:2])
    form = ''.join([x for x in s_[-1]][2:])
    if form == 'PM'and not int(hr) == 12:
        hr = str(int(hr) + 12)
    if form == 'AM' and int(hr) == 12:
        hr = '00'

    return ':'.join([hr, mn, sc])


if __name__ == '__main__':
    input1 = '12:40:22PM'
    input2 = '12:40:22AM'
    print(timeConversion(input1))
    print(timeConversion(input2))
