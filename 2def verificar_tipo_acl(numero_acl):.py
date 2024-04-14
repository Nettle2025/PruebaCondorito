def verificar_tipo_acl(numero_acl):
    # Rangos de números para ACL Estándar y Extendida
    rango_estandar = range(1, 100)
    rango_extendida = range(100, 200)

    if numero_acl in rango_estandar:
        return " corresponde a una ACL Estándar"
    elif numero_acl in rango_extendida:
        return " corresponde  a una ACL Extendida"
    else:
        return " no corresponde a una lista de acceso"
try:
    numero_ingresado = int(input("Ingresa el número de ACL IPv4: "))
    tipo_acl = verificar_tipo_acl(numero_ingresado)
    print(f"El número {numero_ingresado}{tipo_acl}.")
except ValueError:
    print("Error: Ingresa un número válido.")