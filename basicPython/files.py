# Modos de Apertura
# r -> Solo lectura
# r+ -> Lectura y escritura
# w -> Solo escritura. Sobre escribe el archivo si existe. Crea el archivo si no existe
# w+ -> Escritura y lectura. Sobre escribe el archivo si existe. Crea el archivo si no existe
# a -> Añadido (agregar contenido). Crea el archivo si éste no existe
# a+ -> Añadido (agregar contenido) y lectura. Crea el archivo si éste no existe.


def read():
    numbers = []
    with open('./files/numbers.txt', 'r', encoding='utf-8') as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)


def write():
    names = ["Julian", "Erika"]
    with open('./files/names.txt', 'a', encoding='utf-8') as f:
        for name in names:
            f.write(name)
            f.write('\n')
    print('Archivo guardado')


def run():
    write()


if __name__ == '__main__':
    run()