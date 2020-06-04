"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""


def main(first_str: str, second_str: str):
    if not isinstance(first_str, str) and not isinstance(second_str, str):
        return 0
    elif first_str is not second_str and second_str == 'learn':
        return 3
    elif first_str is not second_str and len(first_str) > len(second_str):
        return 2


if __name__ == "__main__":
    print(main(1,2))
    print(main('gun', 'gun'))
    print(main('easy', 'learn'))
