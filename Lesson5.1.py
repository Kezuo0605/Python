#Создать программно файл в текстовом формате, записать
#в него построчно данные, вводимые пользователем.
#Об окончании ввода данных свидетельствует пустая строка.


text = open('text01.txt', 'w', encoding="utf-8")
line = input('Введите текст \n')
while line:
    text.writelines(line)
    line = input('Введите текст \n')
    if not line:
        break
text.close()


#Создать текстовый файл (не программно), сохранить
#в нем несколько строк, выполнить подсчет количества строк,
#количества слов в каждой строке.

text = open('text_01.txt', 'r')
content = text.read()
print(f'Текст: \n {content}')
content = text.readlines()
print(f'Количество строк в файле - {len(content)}')
for i in range(len(content)):
    print(f' {i + 1} - символов в строке {len(content[i])}')
content = text.read()
content = content.split()
print(f'Количество Слов - {len(content)}')
text.close()

#Создать текстовый файл (не программно), построчно записать
#фамилии сотрудников и величину их окладов.
#Определить, кто из сотрудников имеет оклад менее 20 тыс.,
#вывести фамилии этих сотрудников. Выполнить подсчет средней
#величины дохода сотрудников.

with open('text_03', 'r',encoding="utf-8") as pers:
    pers = []
    les = []
    my_list = pers.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
            les.append(i[0])
        pers.append(i[1])
print(f'Оклад меньше 20.000 {les}, средний оклад {sum(map(int, pers)) / len(pers)}')


##Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение
# и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new = []
with open('file_4.txt', 'r', encoding="utf-8") as obj:
        for i in obj:
        i = i.split(' ', 1)
        new.append(rus[i[0]] + '  ' + i[1])
    print(new)

with open('file_4_new.txt', 'w') as obj_2:
    obj_2.writelines(new)

    #
    # Создать вручную и заполнить несколькими строками текстовый файл,
    # в котором каждая строка должна содержать данные о фирме:
    # название, форма собственности, выручка, издержки.
    # Пример строки файла: firm_1   ООО   10000   5000.
    # Необходимо построчно прочитать файл, вычислить прибыль каждой
    # компании, а также среднюю прибыль. Если фирма получила убытки,
    # в расчет средней прибыли ее не включать.
    # Далее реализовать список. Он должен содержать словарь
    # с фирмами и их прибылями, а также словарь со средней прибылью.
    # Если фирма получила убытки, также добавить ее в словарь
    # (со значением убытков).
    # Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000},
    # {“average_profit”: 2000}].
    # Итоговый список сохранить в виде json-объекта в соответствующий
    # файл.
    # Пример json-объекта:
    # [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000},
    # {"average_profit": 2000}]
    # Подсказка: использовать менеджер контекста.


import json

profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('file_7.txt', 'r') as file:
    for line in file:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Прибыль средняя - {prof_aver:.2f}')
    else:
        print(f'Прибыль средняя - отсутсвует. Все работают в убыток')
    pr = {'средняя прибыль': round(prof_aver)}
    profit.update(pr)
    print(f'Прибыль каждой компании - {profit}')

with open('file_7.json', 'w') as write_js:
    json.dump(profit, write_js)

    js_str = json.dumps(profit)
    print(f'Создан файл с расширением json со следующим содержимым: \n '
          f' {js_str}')