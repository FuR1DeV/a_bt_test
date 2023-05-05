import os


def black_book(page: int):
    status_code = os.system(f"./black-book -n {page}")
    return True if status_code == 0 else False


def main():
    """Скорее тут будет эффективен бинарный поиск.
    Смысл бинарного поиска состоит в том, чтобы при каждой итерации делить по полам
    значение и вычислять более приближенное число. Да, я читал Грокаем Алгоритмы"""
    #  Начинаем с максимальной страницы
    #  Главная переменная которая будет вычисляться и передаваться в функцию
    start = 10000000
    #  Заносим в переменную максимальную страницу
    max_page = 10000000
    #  Заносим в переменную минимальную страницу
    min_page = 0
    #  Считаем сколько сделали итераций
    steps = 0
    #  Запускаем бесконечный цикл
    while True:
        #  Считаем шаги
        steps += 1
        #  Запускаем черный ящик
        result = black_book(start)
        #  Если страница есть возвращается True
        if result:
            #  Записываем в переменную минимальную страницу
            min_page = start if min_page < start else min_page
            #  Здесь мы вычисляем главную переменную
            start = int(((max_page - start) / 2) + start)
            #  Тут у нас финал, если максимальную страницу отнять минимальную страницу
            #  и получить 1, то соответственно мы нашли последнюю страницу
            if max_page - min_page == 1:
                #  Возвращаем количество итераций и последнюю страницу
                return steps, min_page
        else:
            #  Записываем в переменную максимальную страницу
            max_page = start
            #  Здесь тоже происходит вычисления
            start = int(((start - min_page) / 2) + min_page)


if __name__ == '__main__':
    # тут явно нужен алгоритм. Согласен, а еще вы забыли два пробела после хэштэга.
    print(main())
