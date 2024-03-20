# Muebles-sas

Este proyecto se enfoca en procesar archivos de texto plano enviados por el proveedor de chat en línea de Muebles SAS para analizar las estadísticas sobre el motivo de contacto de los clientes. La información consolidada se utiliza como base para la estrategia de fidelización de clientes de Muebles SAS.

## Funcionalidades

- Genera un hash MD5 de los datos concatenados para validar la integridad de la información.
- Sube automáticamente los archivos procesados a una Lambda en AWS.
- Almacena la información procesada en una tabla de DynamoDB en formato JSON.
- Elimina los archivos planos de S3 después de procesarlos.

El archivo plano enviado por el proveedor contiene información sobre los diferentes motivos de contacto de los clientes, así como un hash MD5 para garantizar la integridad de los datos.

#### Evento de S3 para la Lambda
La Lambda se activa automáticamente cuando se carga un archivo en el bucket de S3 asociado al proyecto.

#### Estructura del Proyecto
src/: Contiene el código fuente de la Lambda desarrolado en Python.
tests/: Contiene las pruebas unitarias.

## Servicios aws usados
AWS Lambda
AWS S3
AWS DynamoDB

## Autor
Ing. Danilo Ramirez Gomez