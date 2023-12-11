from __future__ import unicode_literals, absolute_import, print_function
from time import sleep

def task(env, duration=1, size=1):
    """
    sleeps `duration`  second and returns `size` times "x", used to test timeouts and large outputs.
    """
    #sleep duration seconds
    sleep(duration)

    #return size times "x"
    return "x" * size
