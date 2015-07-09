"""
Timer module.
"""

import enum
import time


NANO_SECONDS = 'nsec'
MILLI_SECONDS = 'msec'
SECONDS = 'sec'
MINUTES = 'min'

__all__ = ['Timer']

class TimeMetric(enum.Enum):
    sec = 1
    nsec = 1 * pow(10, 9)
    msec = 1 * pow(10, 3)
    min = 1 / 60


def get_time():
    return time.time()



class Timer(object):
    """
    Timer class.
    """
    def __init__(self, time_in='sec'):
        """
        :param time_in string: This defines the time metric min/sec/msec/nsec.
        """
        self.time_in = time_in
        self.start_time = None
        self.end_time = None
        self.time_taken = None

    def __time_in_metric(self):
        return get_time() * float(TimeMetric[self.time_in].value)

    def __enter__(self):
        self.start_time = self.__time_in_metric()

    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = self.__time_in_metric()
        self.time_taken = self.end_time - self.start_time
        print str(self.time_taken) + ' ' + self.time_in
