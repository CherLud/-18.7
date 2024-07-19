import random

# список учеников
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
# отсортируем список учеников
students.sort()
# список предметов
classes = ['Математика', 'Русский язык', 'Информатика']
# пустой словарь с оценками по каждому ученику и предмету
students_marks = {}
# сгенерируем данные по оценкам:
# цикл по ученикам
for student in students:  # 1 итерация: student = 'Александра'
    students_marks[student] = {}  # 1 итерация: students_marks['Александра'] = {}
    # цикл по предметам
    for class_ in classes:  # 1 итерация: class_ = 'Математика'
        marks = [random.randint(1, 5) for i in range(3)]  # генерируем список из 3х случайных оценок
        students_marks[student][class_] = marks  # students_marks['Александра']['Математика'] = [5, 5, 5]
# выводим получившийся словарь с оценками:
for student in students:
    print(f'''{student}
            {students_marks[student]}''')

print('''
        Список команд:
        1. Добавить оценку ученику по определенному предмету
        2. Вывести средний балл по всем предметам по каждому ученику
        3. Вывести все оценки по всем ученикам
        4. Удалить данные ученика
        5. Редактировать оценку по предмету определенного ученика
        6. Вывести оценки по предметам определенного ученика
        7. Вывести средний балл по всем предметам определенного ученика
        8. Добавить нового ученика в журнал
        9. Добавить новый предмет
        10. Выход из программы
        ''')

while True:
    command = int(input('Введите команду: '))
    if command == 1:
        print('1. Добавить оценку ученику по определенному предмету')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # считываем название предмета
        class_ = input('Введите предмет: ')
        # считываем оценку
        mark = int(input('Введите оценку: '))
        # если данные введены верно
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            # добавляем новую оценку для ученика по предмету
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        # неверно введены название предмета или имя ученика
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 2:
        print('2. Вывести средний балл по всем предметам по каждому ученику')
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                # находим сумму оценок по предмету
                marks_sum = sum(students_marks[student][class_])
                # находим количество оценок по предмету
                marks_count = len(students_marks[student][class_])
                # выводим средний балл по предмету
                print(f'{class_} - {marks_sum // marks_count}')
            print()
    elif command == 3:
        print('3. Вывести все оценки по всем ученикам')
        # выводим словарь с оценками:
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()
    elif command == 4:
        print('4. Удалить данные ученика')
        student = input('Введите ученика, которого хотите удалить: ')
        if student in students_marks:
            del students_marks[student]
            print(students_marks)
        else:
            print('Ученик не найден')
    elif command == 5:
        print('5. Редактировать оценку по предмету определенного ученика')
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        mark = int(input('Введите оценку, которую нужно исправить: '))
        if student in students_marks.keys() and class_ in students_marks[student].keys() and mark in students_marks[student][class_]:
            students_marks[student][class_].pop(mark)
            mark = int(input('Введите новую оценку: '))
            # добавляем новую оценку для ученика по предмету
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} исправлена оценка на {mark}')
        # неверно введены название предмета или имя ученика или не найдена оценка для исправления
        else:
            print('ОШИБКА: неверное имя ученика или название предмета или оценка не найдена')
    elif command == 6:
        print('6. Вывести оценки по предметам определенного ученика')
        student = input('Введите имя ученика: ')
        if student in students_marks:
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
        else:
            print('Ученик не найден')
    elif command == 7:
        print('7. Вывести средний балл по всем предметам определенного ученика')
        student = input('Введите имя ученика: ')
        if student in students_marks:
            for class_ in classes:
                # находим сумму оценок по предмету
                marks_sum = sum(students_marks[student][class_])
                # находим количество оценок по предмету
                marks_count = len(students_marks[student][class_])
                # выводим средний балл по предмету
                print(f'{class_} - {marks_sum // marks_count}')
        else:
            print('Ученик не найден')
    elif command == 8:
        print('8. Добавить нового ученика в журнал')
        new_student = input('Введите имя ученика: ')
        if new_student not in students_marks:
            students.append(new_student)
            print(f'Новый ученик {new_student} добавлен в журнал')
            students_marks[new_student] = {
                'Математика': [random.randint(1, 5) for i in range(3)],
                'Русский язык': [random.randint(1, 5) for i in range(3)],
                'Информатика': [random.randint(1, 5) for i in range(3)],
                }
            students.sort()
            print()
            print(f'''{new_student}
                    {students_marks[new_student]}''')
        else:
            print('Ученик уже есть в журнале')
    elif command == 9:
        print('9.Добавить новый предмет')
        classes = ['Математика', 'Русский язык', 'Информатика']
        new_class_ = input('Введите новый предмет: ')
        if new_class_ not in classes:
            classes.append(new_class_)
            for student in students:
                for new_class_ in classes:
                    marks = [random.randint(1, 5) for i in range(3)]
                    students_marks[student][new_class_] = marks
            print(f'Новый предмет {new_class_} добавлен в журнал')
            for student in students:
                print(student)
                for class_ in classes:
                    print(f'\t{class_} - {students_marks[student][class_]}')
                print()
        else:
            print('Предмет уже есть в журнале')
    elif command == 10:
        print('10. Выход из программы')
        break
