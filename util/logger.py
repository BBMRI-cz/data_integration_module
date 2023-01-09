import logging
import sys


class CustomLogger(logging.Logger):
    def __init__(self, name: str):
        super().__init__(name)
        self.level = logging.DEBUG
        logFormatter = logging.Formatter(fmt=' %(asctime)s %(levelname)-8s %(message)s')
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setFormatter(logFormatter)
        self.addHandler(stream_handler)
