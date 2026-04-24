# Orquestador de Red Multimarca

## Descripción del Proyecto

Este proyecto transforma la gestión manual de dispositivos de red en un flujo de trabajo basado en Infraestructura como Código, utilizando GitHub como Fuente Única de Verdad para documentar, versionar y proteger configuraciones de red.

La solución está orientada a equipos Cisco, Huawei, Fortinet y MikroTik, permitiendo administrar configuraciones de forma organizada, segura y trazable.

## Objetivo General

Implementar un repositorio en GitHub que permita centralizar la documentación, inventario, scripts y configuraciones de una infraestructura de red multimarca.

## Tecnologías Utilizadas

- GitHub
- Git
- Python
- Netmiko
- Cisco IOS
- Huawei VRP
- Fortinet FortiOS
- MikroTik RouterOS

## Estructura del Repositorio

```text
orquestador-red-multimarca/
│
├── README.md
├── main.py
├── equipos.csv
├── requirements.txt
│
├── scripts/
│   ├── cisco/
│   ├── huawei/
│   ├── fortinet/
│   └── mikrotik/
│
├── docs/
│
└── evidencias/
    └── capturas/

## 🌐 Enlace de despliegue

El proyecto se encuentra publicado en Netlify y puede visualizarse aquí:

🔗 https://miproyectodered.netlify.app/