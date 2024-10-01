def ordenar_nombres():
    nombres = []

    num_nombres = int(input("Ingrese el número de nombres: "))

    for i in range(num_nombres):
        nombre = input(f"Ingrese nombre {i+1}: ")
        nombres.append(nombre)

    nombres.sort()

    print("\nLista de nombres en orden alfabético:")
    for nombre in nombres:
        print(nombre)

ordenar_nombres()

