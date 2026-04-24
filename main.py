import csv
from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoTimeoutException, NetmikoAuthenticationException


def obtener_script(fabricante):
    rutas = {
        "cisco": "scripts/cisco/configuracion_base.txt",
        "huawei": "scripts/huawei/configuracion_base.txt",
        "fortinet": "scripts/fortinet/configuracion_base.txt",
        "mikrotik": "scripts/mikrotik/configuracion_base.txt"
    }

    ruta = rutas.get(fabricante)

    if not ruta:
        raise ValueError(f"Fabricante no soportado: {fabricante}")

    with open(ruta, "r", encoding="utf-8") as archivo:
        comandos = archivo.read().splitlines()

    return comandos


def conectar_equipo(equipo):
    dispositivo = {
        "device_type": equipo["tipo_dispositivo"],
        "host": equipo["ip"],
        "username": equipo["usuario"],
        "password": equipo["password"],
        "port": int(equipo["puerto"]),
    }

    print(f"\nConectando a {equipo['nombre']} - {equipo['ip']}")

    try:
        conexion = ConnectHandler(**dispositivo)
        comandos = obtener_script(equipo["fabricante"])

        print(f"Aplicando configuración en {equipo['nombre']}...")
        salida = conexion.send_config_set(comandos)

        print(salida)
        print(f"Configuración aplicada correctamente en {equipo['nombre']}")

        conexion.disconnect()

    except NetmikoTimeoutException:
        print(f"Error: No se pudo conectar con {equipo['nombre']}. Tiempo de espera agotado.")

    except NetmikoAuthenticationException:
        print(f"Error: Credenciales incorrectas para {equipo['nombre']}.")

    except Exception as error:
        print(f"Error inesperado en {equipo['nombre']}: {error}")


def leer_inventario():
    with open("equipos.csv", "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        for equipo in lector:
            conectar_equipo(equipo)


if __name__ == "__main__":
    print("Orquestador de Red Multimarca")
    print("Iniciando proceso de automatización...")
    leer_inventario()
    print("\nProceso finalizado.")