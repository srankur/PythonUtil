# You'll need these imports in your own code
from __future__ import print_function

import logging
import logging.handlers
import multiprocessing
import os

# Next two import lines for this demo only
from random import choice, random
import time

queue = multiprocessing.Queue(-1)

# TODO Comments
def listener_configurer():
    root = logging.getLogger()
    h = logging.handlers.RotatingFileHandler('./mptest.log', 'a', 30000000, 10)
    f = logging.Formatter('%(asctime)s %(processName)-10s %(name)s %(levelname)-8s %(message)s')
    h.setFormatter(f)
    root.addHandler(h)

# TODO Comments
def listener_process(queue, configurer):
    configurer()
    print("Listener Ready at :" , time.time())
    while True:
        try:
            record = queue.get()
            #print("Listener reading record name {} record {}:".format(record.name, record) )
            if record is None:  # We send this as a sentinel to tell the listener to quit.
                break
            logger = logging.getLogger(record.name)
            logger.handle(record)  # No level or filter logic applied - just do it!
        except Exception:
            import sys, traceback
            print('Whoops! Problem:', file=sys.stderr)
            traceback.print_exc(file=sys.stderr)



LEVELS = [logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL]

LOGGERS = ['a.b.c', 'd.e.f']

MESSAGES = [
    'Random message #1',
    'Random message #2',
    'Random message #3',
]

# TODO Comments
def worker_configurer(queue):
    h = logging.handlers.QueueHandler(queue)  # Just the one handler needed
    root = logging.getLogger()
    root.addHandler(h)
    # send all messages, for demo; no other level or filter logic applied.
    root.setLevel(logging.DEBUG)



# TODO Comments
def worker_process(queue, configurer):
    configurer(queue)
    name = multiprocessing.current_process().name
    print('Worker started: %s' % name)
    for i in range(2):
        time.sleep(random())
        logger = logging.getLogger(choice(LOGGERS))
        level = choice(LEVELS)
        message = choice(MESSAGES)
        logger.log(level, ("Worker PID : ", os.getpid()))
    print('Worker finished: %s' % name)




def init_log(queue, module_name):
    h = logging.handlers.QueueHandler(queue)  # Just the one handler needed
    logger = logging.getLogger(module_name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(h)

    return logger


# Here's where the demo gets orchestrated. Create the queue, create and start
# the listener, create ten workers and start them, wait for them to finish,
# then send a None to the queue to tell the listener to finish.
def main():
    #queue = multiprocessing.Queue(-1)
    global queue
    listener = multiprocessing.Process(target=listener_process,
                                       args=(queue, listener_configurer))
    listener.start()
    # Ankur Added
    #listener.join()
'''
    workers = []
    for i in range(2):
        worker = multiprocessing.Process(target=worker_process,
                                         args=(queue, worker_configurer))
        workers.append(worker)
        worker.start()
    for w in workers:
        w.join()
'''
    #queue.put_nowait(None)
    #listener.join()

if __name__ == '__main__':
    main()
else: main()