# return "now time in seconds"

from time import time as oclock

def time(self, args = []):
    """show the time\n\ttime"""
    return f"{int(oclock())}"
