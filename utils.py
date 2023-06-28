import json
from os import path

# Пути к файлам
DATA_PATH = 'data'
STUDENTS_DATA_FILENAME = path.join(DATA_PATH, 'students.json')
PROFESSIONS_DATA_FILENAME = path.join(DATA_PATH, 'professions.json')


def list_from_json(filename: str) -> list:
    """
    Получение списка из json-файла
    :param filename: Имя файла
    :return: Список
    """

    if path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    return []


def load_students():
    """
    Получение списка студентов
    :return: Список студентов
    """

    return list_from_json(STUDENTS_DATA_FILENAME)


def load_professions():
    """
    Получение списка профессий
    :return: Список профессий
    """

    return list_from_json(PROFESSIONS_DATA_FILENAME)


def get_student_by_pk(pk: int) -> dict | None:
    """
    Получение студента по его номеру
    :param pk: Номер студента
    :return: Словарь с данными о студенте либо None, если не найдено
    """

    students = load_students()
    return next(filter(lambda s: s['pk'] == pk, students), None)


def get_profession_by_title(title: str) -> dict | None:
    """
    Получить профессию по названию
    :param title: Название профессии (не чувствительно к регистру)
    :return: Словарь с данными о профессии либо None, если не найдено
    """

    professions = load_professions()
    title = title.lower()
    return next(filter(lambda p: p['title'].lower() == title, professions), None)


def check_fitness(student: dict, profession: dict) -> dict:
    """
    Сопоставление умений студента с требованиями к профессии
    :param student: Словарь с данными о студенте
    :param profession: Словарь с данными о профессии
    :return: Словарь с результатами сопоставления
    """

    student_skills = set(student['skills'])
    profession_skills = set(profession['skills'])

    has_list = student_skills.intersection(profession_skills)
    lacks_list = profession_skills.difference(student_skills)
    fit_percent = round((len(has_list) / len(profession_skills)) * 100)

    return {
        "has": has_list,
        "lacks": lacks_list,
        "fit_percent": fit_percent
    }


# if __name__ == '__main__':
#     # [print(student) for student in list_from_json('data\\students.json')]
#     # [print(student) for student in load_students()]
#     # [print(profession) for profession in load_professions()]
#     # print(get_student_by_pk(1))
#     # print(get_profession_by_title('backend'))
#     # print(check_fitness(get_student_by_pk(1), get_profession_by_title('backend')))
#     pass
