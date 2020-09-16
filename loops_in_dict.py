# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]

def values_for_key(dictionary,key):
    list_items = []
    for item in dictionary:
        list_items.append(item[key])
    return list_items

students_names = values_for_key(students,'first_name')
k = 0
for name in students_names:
    k += 1
    if students_names[:k-1].count(name) == 0:
        print(f'{name}: {students_names.count(name)}')

# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]
students_names = []
for student in students:
    students_names.append(student['first_name'])

def most_frequent_name(students_names):
    """
    Returns the most frequent item in the list
    """
    counter = 0
    freqname = students_names[0] 
        
    for name in students_names: 
        curr_frequency = students_names.count(name) 
        if curr_frequency > counter: 
            counter = curr_frequency 
            freqname = name
    return freqname

print(f'Самое частое имя среди учеников: {most_frequent_name(students_names)}') 

# Пример вывода:
# Самое частое имя среди учеников: Маша

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]
k = 0
for school_class in school_students:
    k += 1
    list_school_students = values_for_key(school_class,'first_name')
    print(f'Самое частое имя в классе {k}: {most_frequent_name(list_school_students)}')


# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


# # Задание 4
# # Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# school = [
#   {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
#   {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
# ]
# is_male = {
#   'Маша': False,
#   'Оля': False,
#   'Олег': True,
#   'Миша': True,
# }
# # ???

# # Пример вывода:
# # В классе 2a 2 девочки и 0 мальчика.
# # В классе 3c 0 девочки и 2 мальчика.


# # Задание 5
# # По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
# school = [
#   {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
#   {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
# ]
# is_male = {
#   'Маша': False,
#   'Оля': False,
#   'Олег': True,
#   'Миша': True,
# }
# # ???

# # Пример вывода:
# # Больше всего мальчиков в классе 3c
# # Больше всего девочек в классе 2a