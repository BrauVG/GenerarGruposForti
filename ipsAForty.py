import pyperclip
import ipaddress

# Verifica si una cadena es una dirección IPv4 válida
def ip_valida(ip):
    try:
        ipaddress.IPv4Address(ip)
        return True
    except ValueError:
        return False

# Genera comandos de configuración para FortiGate con direcciones IP individuales y un grupo de direcciones
def generar_comandos(nombre_grupo, ips):
    comandos = []
    # Crear una entrada de firewall address para cada IP
    for ip in ips:
        comandos.append(f"""
config firewall address
edit "{ip}/32"
set subnet {ip} 255.255.255.255
next
end
""")
    
    # Crear el grupo de direcciones con todas las IPs anteriores
    miembros = " ".join([f'"{ip}/32"' for ip in ips])
    comandos.append(f"""
config firewall addrgrp
edit "{nombre_grupo}"
append member {miembros}
next
end
""")
    
    return comandos

# Captura un único bloque de entrada del usuario: nombre del grupo seguido de una o más IPs
def entrada_grupo():
    print("Introduce un solo grupo con su nombre y las IPs (una por línea). Ejemplo:\n"
          "Grupo1\n192.168.1.1\n192.168.1.2\n\n"
          "Presiona Enter en una línea vacía para finalizar:")
    
    lineas = []
    while True:
        linea = input()
        if linea.strip() == "":
            break
        lineas.append(linea.strip())

    return "\n".join(lineas)

# Función principal del script
def main():
    entrada = entrada_grupo().strip()

    # Validar que solo se haya ingresado un grupo (no se permiten bloques múltiples)
    if "\n\n" in entrada:
        print("\nError: Solo se permite un grupo por ejecución.")
        return

    lineas = entrada.splitlines()

    # Validar que haya al menos nombre del grupo y una IP
    if len(lineas) < 2:
        print("\nError: Se requiere al menos un nombre de grupo y una IP.")
        return

    nombre_grupo = lineas[0]
    ips = lineas[1:]

    # Validar que todas las IPs sean válidas
    if not all(ip_valida(ip) for ip in ips):
        print("\nError: Una o más IPs no tienen formato válido.")
        return

    # Generar comandos y copiarlos al portapapeles
    comandos = generar_comandos(nombre_grupo, ips)
    comandos_completos = "\n".join(comandos)
    pyperclip.copy(comandos_completos)
    print("\nComandos generados y copiados al portapapeles.")

# Ejecutar el script
if __name__ == "__main__":
    main()


"""Hecho por Braulio Vargas"""