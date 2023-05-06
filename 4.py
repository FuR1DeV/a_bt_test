import json


def count_questions(data: dict):
    # вывести количество вопросов (questions)
    questions = 0
    for question in data.get("game").get("rounds"):
        questions += len(question.get("questions"))
    return print(questions)


def print_right_answers(data: dict):
    # вывести все правильные ответы (correct_answer)
    correct_answers = []
    for answer in data.get("game").get("rounds"):
        for correct_answer in answer.get("questions"):
            correct_answers.append(correct_answer.get("correct_answer"))
    return print(correct_answers)


def print_max_answer_time(data: dict):
    # вывести максимальное время ответа (time_to_answer)
    max_time = 0

    def find(collection, key):
        if isinstance(collection, dict):
            if key in collection:
                yield collection[key]
            for val in collection.values():
                yield from find(val, key)
        elif isinstance(collection, list):
            for val in collection:
                yield from find(val, key)

    for val in find(data, 'time_to_answer'):
        max_time = val if val > max_time else max_time
    return print(max_time)


def main(args):
    with open('test.json') as f:
        data = json.load(f)  # загрузить данные из test.json файла
    count_questions(data)
    print_right_answers(data)
    print_max_answer_time(data)


if __name__ == '__main__':
    # передать имя файла из аргументов командной строки
    main("test.json")
