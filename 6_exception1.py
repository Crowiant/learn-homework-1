"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""
answer_dict = {
    'Как дела?': 'Хорошо',
    'Что делаешь?': 'Программирую',
    'А хорошо умеешь?': 'Только учусь'
}


def ask_user(answers: dict):
    console_input = ''
    while console_input != 'Пока':
        try:
            console_input = input('Введите вопрос: ')
            check_answers = answers.get(console_input)
            if check_answers:
                print(check_answers)
            elif console_input != 'Пока':
                print('Я затрудняюсь ответить на вопрос')
        except KeyboardInterrupt:
            print("Пока!")
            break


if __name__ == "__main__":
    ask_user(answer_dict)
