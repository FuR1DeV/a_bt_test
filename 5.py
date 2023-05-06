import os


def task1():
    # в папке test найти все файлы filenames вывести количество
    res = []
    for root, dirs, files in os.walk("./test"):
        for filename in files:
            if "filenames" in str(filename):
                res.append(filename)
    return print(f"Все файлы - {res}\nКоличество - {len(res)}")


def task2():
    # в папке test найти все email адреса записанные в файлы
    emails = []
    for root, dirs, files in os.walk("./test"):
        for filename in files:
            with open(f"{root}/{filename}", "r") as file:
                for line in file.readlines():
                    if "@" in str(line):
                        emails.append(line[:-1])
    return print(f"Все email в папке test - {emails}")


def main():
    task1()
    task2()
    # дополнительно: придумать механизм оптимизации 2-й задачи

    # Нам надо проверить каждый файл, каждую строку. Скорее всего можно
    # оптимизировать с помощью регулярных выражений


if __name__ == '__main__':
    main()
