
lista_compras = []

while True:
    
    print("\nMenú de opciones:")
    print("1. Agregar artículo")
    print("2. Eliminar artículo")
    print("3. Mostrar lista")
    print("4. Salir")

    
    opcion = input("Selecciona una opción (1/2/3/4): ")

   
    if opcion == "1":
        articulo = input("Introduce el nombre del artículo: ")
        lista_compras.append(articulo)
        print(f"Artículo '{articulo}' agregado a la lista.")
    
    elif opcion == "2":
        if not lista_compras:
            print("La lista está vacía. No hay artículos para eliminar.")
        else:
            print("Lista de compras actual:")
            for idx, item in enumerate(lista_compras):
                print(f"{idx}: {item}")
            indice = input("Introduce el índice del artículo a eliminar: ")
            try:
                indice = int(indice)
                if 0 <= indice < len(lista_compras):
                    eliminado = lista_compras.pop(indice)
                    print(f"Artículo '{eliminado}' eliminado de la lista.")
                else:
                    print("Índice fuera de rango.")
            except ValueError:
                print("Por favor, introduce un número entero válido.")
    
    elif opcion == "3":
        if not lista_compras:
            print("La lista está vacía.")
        else:
            print("Lista de compras:")
            for idx, item in enumerate(lista_compras):
                print(f"{idx}: {item}")

    elif opcion == "4":
        print("¡Hasta luego señor profesor!")
        break

    else:
        print("Opción no válida. Por favor, selecciona una opción del menú.")
