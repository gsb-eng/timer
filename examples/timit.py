"""
Timer usage example.
"""

import timer


def rotate(no_of_times=10000000):
    for i in xrange(no_of_times):
        pass


with timer.Timer(time_in='min') as t:
    rotate()

