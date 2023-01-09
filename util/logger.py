import logging
import sys


def getCustomLogger(name):
    log = logging.getLogger(name)
    log.level = logging.DEBUG
    logFormatter = logging.Formatter(fmt=' %(asctime)s %(levelname)-8s %(message)s')
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(logFormatter)
    log.addHandler(stream_handler)
    return log
