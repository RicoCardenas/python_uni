# Imprimimos el título del programa
print("REGISTRADURIA")

# Inicializamos un diccionario vacío para almacenar los datos de los ciudadanos
datos_ciudadanos = {}

# Iniciamos un bucle infinito para mostrar el menú y procesar las opciones del usuario
while True:
    # Imprimimos el menú de opciones
    print("\n1. Agregar ciudadano")
    print("2. Ver ciudadanos")
    print("3. Ver si el ciudadano es apto para votar")
    print("4. Salir")

    # Solicitamos al usuario que ingrese una opción y la convertimos a entero
    opcion = int(input("\nIngrese una opción: "))

    # Si la opción es 1, agregamos un nuevo ciudadano
    if opcion == 1:

        name = input("\nIngrese su nombre completo: ")
        edad = int(input("Ingrese su edad: "))
        datos_ciudadanos[name] = edad
        
        print(f"El ciudadano {name} ha sido agregado con exito")
        
    # Si la opción es 2, mostramos la lista de ciudadanos registrados
    elif opcion == 2:

        print("\nListado de ciudadanos registrados")
        print(f"{datos_ciudadanos}")
        
    # Si la opción es 3, verificamos si el ciudadano es apto para votar
    elif opcion == 3:

        print("\nVerificar si el ciudadano es apto para votar")
        print("\nListado de ciudadanos registrados, separados por comas")
        print(datos_ciudadanos)

        ciudadano = input("\ningrese el nombre completo del ciudadano: ")

        # Verificamos si la edad del ciudadano es mayor o igual a 18
        if datos_ciudadanos[ciudadano] >= 18: 
            print(f"El ciudadano {ciudadano} es apto para votar")
        else:
            print(f"El ciudadano {ciudadano} no es apto para votar")

    # Si la opción es 4, salimos del bucle y terminamos el programa
    elif opcion == 4:
        
        print("\nGracias por usar el programa")
        break