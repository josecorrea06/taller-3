def suma_numeros_pares():
    num_numeros = int(input("Ingrese el número de números: "))
    suma_pares = 0

    for i in range(num_numeros):
        num = int(input(f"Ingrese número {i+1}: "))
        if num % 2 == 0:
            suma_pares += num

    print(f"\nSuma de los números pares: {suma_pares}")

suma_numeros_pares()
