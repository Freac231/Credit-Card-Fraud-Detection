import logging

logging.basicConfig(filename='server.log', format='%(asctime)s %(message)s', filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.INFO)