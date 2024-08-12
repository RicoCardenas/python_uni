# Solicitamos al usuario que ingrese el número para el cual se generará la tabla de multiplicar
numero = int(input("Ingresa el numero a multiplicar: "))

# Solicitamos al usuario que ingrese hasta qué número desea que se multiplique
can_mult = int(input("Hasta donde desea que se multiplique: "))

# Usamos un bucle for para iterar desde 1 hasta el número ingresado por el usuario (inclusive)
for i in range(1, can_mult + 1):

    multiplicar = numero * i

    print(f"{numero} * {i} = {multiplicar}")