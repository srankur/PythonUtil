from __future__ import print_function

from Logger.MultiProcessLogger.logModule import init_log
from Logger.MultiProcessLogger.logModule import queue
import logging
import os

import multiprocessing as mp


logger = init_log(queue, __name__)


def calc_cube(num):
    print("Calculating Cube")
    for n in num:
        logger.log(logging.DEBUG, ("Cube value", n*n*n, "Cube PID", os.getpid()))


if __name__ == "__main__":
    calc = mp.Process(target=calc_cube, args=(range(10),))
    calc.start()
    calc.join()