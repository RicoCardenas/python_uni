print("REGISTRADURIA")

datos_ciudadanos = {}

while True:
    print("\n1. Agregar ciudadano")
    print("2. Ver ciudadanos")
    print("3. Ver si el ciudadano es apto para votar")
    print("4. Salir")

    opcion = int(input("\nIngrese una opción: "))

    if opcion == 1:
        name = input("\nIngrese su nombre completo: ")
        edad = int(input("Ingrese su edad: "))
        datos_ciudadanos[name] = edad
        print(f"El ciudadano {name} ha sido agregado con exito")
        
    elif opcion == 2:
        print("\nListado de ciudadanos registrados")
        print(f"{datos_ciudadanos}")
        
    elif opcion == 3:
        print("\nVerificar si el ciudadano es apto para votar")
        print("\nListado de ciudadanos registrados, separados por comas")
        print(datos_ciudadanos)
        ciudadano = input("\ningrese el nombre completo del ciudadano: ")
        if datos_ciudadanos[ciudadano] >= 18:
            print(f"El ciudadano {ciudadano} es apto para votar")
        else:
            print(f"El ciudadano {ciudadano} no es apto para votar")
            
    else:
        print("Gracias por usar el sistema de la registraduria")
        break



