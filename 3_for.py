"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

school_workbook = [
    {
        'school_class': '4a',
        'score': [3, 4, 2, 5, 4]
    },
    {
        'school_class': '8a',
        'score': [4, 4, 4, 5]
    },
    {
        'school_class': '2a',
        'score': [3, 2, 5, 5, 2, 5, 2]
    }
]


def school_average(school: list):
    result = 0
    for list_of_scores in school:
        result += (sum(list_of_scores['score']) / len(list_of_scores['score']))
    result = result / len(school)
    print('Average mark of school is:', '%.2f' % result)


def class_average(school: list):
    result = 0
    for list_of_scores in school:
        result = sum(list_of_scores['score']) / len(list_of_scores['score'])
        print('Average for class ', list_of_scores['school_class'], 'is:', '%.2f' % result)


def main(school: list):
    school_average(school)
    class_average(school)


if __name__ == "__main__":
    main(school_workbook)
