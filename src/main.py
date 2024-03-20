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

def invoacion_lambda(nombre_lambda, payload):
    '''
    Parametros
    ----------
        nombre_lambda (str): Nombre de lambda a invocar
        payload (json): Payload a enviar a la lambda
    
    Retorno
    -----------
       lambda_payload (json): Payload de respuesta
    '''

    lambda_client = boto3.client('lambda')
    logger.info(f"Invocando Lambda: {nombre_lambda}")
    invoke_response = lambda_client.invoke(FunctionName=nombre_lambda,
                                           InvocationType='RequestResponse',
                                           Payload=json.dumps(payload))
    logger.info(f"Invocación Completada: {nombre_lambda}")
    lambda_payload = invoke_response['Payload'].read()
    lambda_payload = lambda_payload.decode('utf8')
    lambda_payload = json.loads(lambda_payload)
    return lambda_payload

def download_s3(bucket, file, destiny):
    
    s3 = boto3.resource('s3')
    file_s3 = s3.download_file(bucket, file, destiny)
    return file_s3
