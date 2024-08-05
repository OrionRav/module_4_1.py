from math import inf
# функция, отвечающая за деление - возвращает бесконечность
def divide(first, second):
    if second == 0:
        return inf

    return first / second
