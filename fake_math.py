# функция, отвечающая за деление - возвращает строку "Ошибка"
def divide(first, second):
    if second == 0:
        return "Ошибка"

    return first / second