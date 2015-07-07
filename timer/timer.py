"""
Timer module.
"""

import time


class Timer(object):
    """
    Timer class.
    """
    def __init__(self, time_in=None):
        """
        @param time_in string: This defines the time metric min/sec/msec/nsec.
        """
        self.time_in = time_in
        self.start_time = None
        self.end_time = None

    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = time.time()
        print self.end_time - self.start_time

