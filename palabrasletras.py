def filtrar_palabras():
    palabras = []
    letra = input("Ingrese la letra para filtrar: ").lower()

    num_palabras = int(input("Ingrese el número de palabras: "))

    for i in range(num_palabras):
        palabra = input(f"Ingrese palabra {i+1}: ").lower()
        palabras.append(palabra)

    palabras_filtradas = [palabra for palabra in palabras if palabra.startswith(letra)]

    print(f"\nLista de palabras que comienzan con '{letra}':")
    for palabra in palabras_filtradas:
        print(palabra)

filtrar_palabras()