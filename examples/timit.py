"""
Timer usage example.
"""

import timer


def rotate(no_of_times=1000000000):
    for i in xrange(no_of_times):
        pass


with timer.Timer(time_in='sec') as t:
    rotate()

