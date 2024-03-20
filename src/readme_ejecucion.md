# Configuracion previa:

Dependencias:

- Python 3.9
- Boto3 1.34.66

## Ejecucion del Programa

Nos ubicamos en la ruta del proyecto, en la rutaL `.../src/`:

Se configura la variable de entorno:
```
AWS_LAMBDA=ai-technical-test-danilo
```

Para ejecutar la actualizacion de la instancia de la lambda, y cargar el archivo a s3:

```
zip -r lambda_ai.zip app.py && aws lambda update-function-code --function-name $AWS_LAMBDA --zip-file fileb:///home/vboxuser/Documents/muebles-sas/src/lambda_ai.zip && aws s3 cp /home/vboxuser/Documents/muebles-sas/recursos/ s3://$AWS_LAMBDA/  --recursive
```