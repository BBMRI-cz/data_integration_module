import logging
import sys

logger = logging.getLogger(__name__)
logger.level = logging.DEBUG
logFormatter = logging.Formatter(fmt=' %(asctime)s %(levelname)-8s %(message)s')
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(logFormatter)
logger.addHandler(stream_handler)
