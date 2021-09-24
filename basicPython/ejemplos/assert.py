def primera_letra(lista_palabras):
    primeras_letras = []

    for palabra in lista_palabras:
        assert type(palabra) == str, f'{palabra} no es str'
        assert len(palabra) > 0, f'{palabra} es vacío'

        primeras_letras.append(palabra[0])

    return primeras_letras

mi_lista = ['Julian', 'Camilo', 3, '', 'Sachez', 'Sosa']
primera_letra(mi_lista)