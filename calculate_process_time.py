## https://stackoverflow.com/questions/766335/python-speed-testing-time-difference-milliseconds

>>> import datetime
>>> a = datetime.datetime.now()
>>> b = datetime.datetime.now()
>>> c = b - a

>>> c
datetime.timedelta(0, 4, 316543)
>>> c.days
0
>>> c.seconds
4
>>> c.microseconds
316543
