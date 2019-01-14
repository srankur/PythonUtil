import logging
import logging.handlers


def init_log(modulename = None):
    if modulename is None:
        logger = logging.getLogger()
    else:
        logger = logging.getLogger(modulename)

    logger.setLevel(logging.DEBUG)

    logfilehandler = logging.handlers.RotatingFileHandler('Module.log', 'a', 300000, 10)
    logfilehandler.setLevel(logging.DEBUG)

    logformat = logging.Formatter('%(asctime)s %(processName)-10s %(name)s %(levelname)-8s %(message)s')
    logfilehandler.setFormatter(logformat)

    logger.addHandler(logfilehandler)

    return logger
