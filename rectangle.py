def area(a, b):
    '''
    Функция считает и возвращает площадь прямоугольника.
    Аргументы:
        a (float) или (int) - длина одной из сторон прямоугольника.
        b (float) или (int) - длина другой стороны прямоугольника.
    Возвращаемое значение:
        S (float) или (int) - значение площади прямоугольника,
            (float), если a или b (float),
            (int), если a и b (int).
    Пример вызова:
        area(1, 2)
    Вернёт:
        2
    '''
    if (type(a) != int) and (type(a) != float):
        print(f'WARNING in rectangel.area(): "a" must be int or float type but not {type(a).__name__}')
        return -1
    if (type(b) != int) and (type(b) != float):
        print(f'WARNING in rectangel.area(): "b" must be int or float type but not {type(b).__name__}')
        return -1
    if a <= 0:
        print(f'WARNING in rectangel.area(): "a" <= 0, "a" == {a}')
        return -1
    if b <= 0:
        print(f'WARNING in rectangel.area(): "b" <= 0, "b" == {b}')
        return -1

    return a * b


def perimeter(a, b):
    '''
    Функция считает и возвращает периметр прямоугольника.
    Аргументы:
        a (float) или (int) - длина одной из сторон прямоугольника.
        b (float) или (int) - длина другой стороны прямоугольника.
    Возвращаемое значение:
        P (float) или (int) - значение периметра прямоугольника,
            (float), если a или b (float),
            (int), если a и b (int).
    Пример вызова:
        perimeter(1, 2)
    Вернёт:
        6
    '''
    if (type(a) != int) and (type(a) != float):
        print(f'WARNING in rectangel.perimeter(): "a" must be int or float type but not {type(a).__name__}')
        return -1
    if (type(b) != int) and (type(b) != float):
        print(f'WARNING in rectangel.perimeter(): "b" must be int or float type but not {type(b).__name__}')
        return -1
    if a <= 0:
        print(f'WARNING in rectangel.perimeter(): "a" <= 0, "a" == {a}')
        return -1
    if b <= 0:
        print(f'WARNING in rectangel.perimeter(): "b" <= 0, "b" == {b}')
        return -1
    
    return 2 * (a + b)
