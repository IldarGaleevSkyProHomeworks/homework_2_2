from utils import *


def student_info_to_str(student: dict) -> str:
    """
    Преобразует данные о студенте в строку для вывода
    :param student: Словарь с данными о студенте
    :return: Строка
    """

    return f"Студент {student['full_name']}\n" \
           f"Знает {', '.join(student['skills'])}"


def fit_result_to_str(student: dict, fit_result: dict) -> str:
    """
    Преобразует результат сопоставления в строку для вывода
    :param student: Словарь с данными о студенте
    :param fit_result: Словарь с результатом сопоставления
    :return: Строка
    """

    return f"Пригодность: {fit_result['fit_percent']}%\n" \
           f"{student['full_name']} знает {', '.join(fit_result['has'])}\n" \
           f"{student['full_name']} не знает {', '.join(fit_result['lacks'])}"


def main():
    student_id_str = input('Введите номер студента: ').strip()

    if not student_id_str.isdigit():
        print('Неверный формат ввода! Введите число!')
        return

    student_id = int(student_id_str)
    student_info = get_student_by_pk(student_id)
    if not student_info:
        print('Студента с таким номером не найдено')
        return

    print(student_info_to_str(student_info))
    print('-' * 5)

    print(f"Выберите специальность для оценки студента {student_info['full_name']}")
    profession_title = input().strip()

    profession_info = get_profession_by_title(profession_title)
    if not profession_info:
        print(f"Профессии с названием \"{profession_title}\" не найдено!")
        return

    fit_result = check_fitness(student_info, profession_info)
    print(fit_result_to_str(student_info, fit_result))


if __name__ == '__main__':
    main()
