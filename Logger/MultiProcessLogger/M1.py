from __future__ import print_function

from Logger.MultiProcessLogger.logModule import init_log
from Logger.MultiProcessLogger.logModule import queue
import logging
import os

import multiprocessing as mp


logger = init_log(queue, __name__)

def calc_square(num):
    print("Calculating squares")
    for n in num:
        logger.log(logging.DEBUG, ("Square value", n*n, "Square PID", os.getpid()))


if __name__ == "__main__":
    calc = mp.Process(target=calc_square, args=(range(10),))
    calc.start()
    calc.join()