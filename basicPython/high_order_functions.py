from functools import reduce

def my_reduce():
    """reduce los valores de una lista a un unico valor """
    my_list = [2, 2, 2, 2, 2]
    all_multiplied = reduce( lambda a, b: a * b, my_list )
    print(all_multiplied)


def my_filter():
    """recorre una lista, busca por la condición y la guarda en una nueva lista"""
    my_list = [1, 4, 5, 6, 9, 13, 19, 21]
    odd = list( filter( lambda x: x % 2 != 0, my_list ) )
    print(odd)


def my_map():
    """recorre una lista y la guarda en una nueva lista"""
    my_list = [1, 2, 3, 4, 5]
    squares = list( map( lambda x: x**2, my_list ) )
    print(squares)


def run():
    # my_filter()
    # my_map()
    my_reduce()


if __name__ == '__main__':
    run()