# Creacion de lambda

## Definir variales de entorno
```
AWS_ACCOUNT_ID=:223690032992 && AWS_REGION=us-east-1 && AWS_LAMBDA=ai-technical-test-danilo && AWS_S3_BUCKET=ai-technical-test-danilo && AWS_ROLE=ai-technical-test-danilo-LambdaExecutionRole-khK1o3cxeFiX
```

## Actualizar LAMBDA

Desde el terminal y ubicado en src/:

Para el caso de subir una libreria:

pip install -r requirements.txt -t . 

```
zip -r lambda_ai.zip app.py && aws lambda update-function-code --function-name $AWS_LAMBDA --zip-file fileb:///home/vboxuser/Documents/muebles-sas/src/lambda_ai.zip && aws s3 cp /home/vboxuser/Documents/muebles-sas/recursos/ s3://  / --recursive
```

```
zip -r lambda_ai.zip app.py asn1crypto/ asn1crypto-1.5.1.dist.info/ cffi/ cffi-1.16.0.dist-info/ cryptography/ cryptography-2.6.1.dist-info/ six-1.16.0.dist-info/ pycparser/ pycparser-2.21.dist-info/ _cffi_backend.cpython-39-x86_64-linux-gnu.so six.py __pycache__/ requirements.txt && aws lambda update-function-code --function-name $AWS_LAMBDA --zip-file fileb:///home/vboxuser/Documents/muebles-sas/src/lambda_ai.zip && aws s3 cp /home/vboxuser/Documents/muebles-sas/recursos/ s3://ai-technical-test-danilo/ --recursive
```

dobles
```
zip -r lambda_ai.zip app.py asn1crypto/ asn1crypto-1.5.1.dist.info/ cffi/ cffi-1.16.0.dist-info/ cryptography/ cryptography-2.6.1.dist-info/ six-1.16.0.dist-info/ pycparser/ pycparser-2.21.dist-info/ _cffi_backend.cpython-39-x86_64-linux-gnu.so six.py __pycache__/
```

```
zip -r lambda_ai.zip app.py asn1crypto/ asn1crypto-1.5.1.dist.info/ cffi/ cffi-1.16.0.dist-info/ cryptography/ cryptography-2.6.1.dist-info/ six-1.16.0.dist-info/ pycparser/ pycparser-2.21.dist-info/ _cffi_backend.cpython-39-x86_64-linux-gnu.so six.py __pycache__/
```

```
aws lambda update-function-code --function-name $AWS_LAMBDA --zip-file fileb:///home/vboxuser/Documents/muebles-sas/src/lambda_ai.zip && aws s3 cp /home/vboxuser/Documents/muebles-sas/recursos/ s3://ai-technical-test-danilo/ --recursive
```


Actualizar la tabla de DyndamoDB
```
aws dynamodb update-table \
    --table-name ai-technical-test-danilo \
    --attribute-definitions AttributeName=Data,AttributeType=S \
    --global-secondary-index-updates \
        "Create={IndexName=DataIndex,KeySchema=[{AttributeName=Data,KeyType=HASH}],Projection={ProjectionType=ALL},ProvisionedThroughput={ReadCapacityUnits=5,WriteCapacityUnits=5}}" \
    --region us-east-1
```