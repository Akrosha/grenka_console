# return "now time in seconds"

from time import time as oclock

def time(self, args = []):
    """show the time\n\t{name}"""
    return f"{int(oclock())}"
