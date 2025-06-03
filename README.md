# Generador de Comandos para FortiGate

Este script permite generar comandos de configuración para un firewall FortiGate a partir de una lista de direcciones IP.

## Uso

1. Ejecuta el script.
2. Introduce el nombre del grupo y las IPs (una por línea).
3. Presiona Enter en una línea vacía para finalizar.
4. Los comandos se copiarán automáticamente al portapapeles.

### Ejemplo de entrada:

GrupoClientes
192.168.0.10
192.168.0.11

## Requisitos

- Python 3.x
- Librerías: `pyperclip`, `ipaddress` (incluida en la mayoría de instalaciones de Python 3)

## Propósito

Este script automatiza la creación de comandos FortiGate para configuraciones rápidas de direcciones IP y grupos.
