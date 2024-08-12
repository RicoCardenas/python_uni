# Inicializamos una lista vacía para almacenar los números ingresados por el usuario
lista = []

# Usamos un bucle for para iterar 10 veces, solicitando al usuario que ingrese un número en cada iteración
for i in range(1, 11):

    num = float(input("ingrese su numero: "))
    lista.append(num)

# Inicializamos contadores para números positivos, negativos y ceros
cont_pos = 0
cont_neg = 0
cont_cero = 0

# Iteramos sobre cada número en la lista
for num in lista:

    if num > 0:
        cont_pos += 1
    elif num < 0:
        cont_neg += 1
    else:
        cont_cero += 1

print(f"La cantidad de numeros positivos es: {cont_pos}")
print(f"La cantidad de numeros negativos es: {cont_neg}")
print(f"La cantidad de ceros es: {cont_cero}")