def contar_vocales():
    palabra = input("Ingrese una palabra o frase: ").lower()
    vocales = "aeiou"
    conteo_vocales = {vocal: 0 for vocal in vocales}

    for letra in palabra:
        if letra in vocales:
            conteo_vocales[letra] += 1

    print("Conteo de vocales:")
    for vocal, conteo in conteo_vocales.items():
        print(f"{vocal}: {conteo}")

contar_vocales()