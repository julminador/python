def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    try:
        num = input('Ingrese un número: ')
        assert len(num) > 0, "No se ingresó ningún valor"
        num = int(num)
        if num < 0:
            raise ValueError()
        print(divisors(num))
        print('Terminó el programa')
    except ValueError:
        print('Debe ingresar un número entero')


if __name__ == '__main__':
    run()