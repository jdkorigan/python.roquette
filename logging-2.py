import logging

logger = logging.getLogger('akshay')
logger.setLevel(logging.DEBUG)
sh = logging.StreamHandler()
sh.setLevel(logging.DEBUG)
logger.addHandler(sh)
logger.debug('Hello')