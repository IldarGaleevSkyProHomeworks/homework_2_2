# Урок 7. Вложенные структуры - домашнее задание

## Краткий алгоритм
1. Запросить у пользователя номер студента, если он существует вывести о нем информацию:

```
Студент Jane Snake
Знает Python, Go, Linux
```

2. Далее запросить название профессии, 
если профессия существует - сопоставить требуемые скиллы с имеющимися у студента.
Вывести результат вида:

```
Пригодность 50%
Jane Snake знает Python, Linux
Jane Snake не знает Docker, SQL
```

3. Если запрашиваемых данных не найдено - завершить выполнение программы

## Данные

Необходимые данные берутся из json-файлов:

- Список студентов: [students.json](data/students.json)
- Список профессий: [professions.json](data/professions.json)