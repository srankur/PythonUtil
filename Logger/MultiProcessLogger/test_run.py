from __future__ import print_function

import Logger.MultiProcessLogger.M1 as m1
import Logger.MultiProcessLogger.M2 as m2
import multiprocessing as mp
from Logger.MultiProcessLogger.logModule import queue



if __name__ == "__main__":
    calc_cube = mp.Process(target=m2.calc_cube, args=(range(10),))
    calc_square = mp.Process(target=m1.calc_square, args=(range(10),))

    calc_cube.start()
    calc_square.start()

    calc_cube.join()
    calc_square.join()

    queue.put_nowait(None)
