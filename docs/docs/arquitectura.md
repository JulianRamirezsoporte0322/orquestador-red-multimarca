# Arquitectura de la Solución

La arquitectura del proyecto está basada en un modelo de automatización centralizada, donde GitHub funciona como la fuente única de verdad para almacenar documentación, inventario y scripts de configuración.

## Componentes

### GitHub

GitHub permite almacenar el código fuente, documentación técnica y control de versiones. Cada cambio realizado queda registrado mediante commits.

### Inventario

El archivo `equipos.csv` contiene la información básica de los dispositivos de red, incluyendo IP, fabricante, tipo de dispositivo y protocolo de conexión.

### Orquestador en Python

El archivo `main.py` lee el inventario y ejecuta los comandos definidos para cada fabricante.

### Scripts por Fabricante

Los comandos se almacenan en carpetas separadas para Cisco, Huawei, Fortinet y MikroTik.

### Dispositivos de Red

Son los equipos físicos o virtuales donde se aplican las configuraciones.