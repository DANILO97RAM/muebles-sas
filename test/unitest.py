import json
import boto3
import logging

logging.basicConfig(level=logging.INFO)
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.INFO)

formatter = logging.Formatter('[%(levelname)s] %(message)s')
consoleHandler.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(consoleHandler)
logger.propagate = False

def unitest():
    logger.info('#' * 50)
    logger.info(f'Inciando Archivo de pruebas...')
    
unitest()