# 1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
exp = [23, "proto", 23.6, "ksdj", {1, 2, 3}, (5, 6, 7, "asd")]
print(type(exp))
print(type(exp[5]))
for i in exp:
    print(type(i))

#2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются
# элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний
# сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().
num = int(input("Сколько значений будет в списке? введите целое число"))
list1 = []
i = 1
while num > len(list1):
    num2 = input("введите элемент списка")
    list1.append(num2)
    i = i + 1

list1a = list1[::2]
list1b = list1[1::2]

for w in list1:
    if w % 2 == 0:
        list1 = list1.insert(w, list1[w::2])
    elif w % 2 != 0:
        list1 = list1.insert(w, list1[w::2])

print(list1)




# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

month = int(input("Введите  номер месяца от 1 до 12"))
month_list = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь",
              "Декабрь"]
month_dict = {
    "Январь": "Зима",
    "Февраль": "Зима",
    "Март": "Весна",
    "Апрель": "Весна",
    "Май": "Весна",
    "Июнь": "Лето",
    "Июль": "Лето",
    "Август": "Лето",
    "Сентябрь": "Осень",
    "Октябрь": "Осень",
    "Ноябрь": "Осень",
    "Декбрь": "Зима"
}
print(month_list[month-1], (month_dict[month_list[month-1]]))


#4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.
word1 = input("введите несколько слов, разделяйте слова пробелами")
word1 = word1.split()
i=1
for word in word1:
    if len(word) > 10:
        print(f'{i}.{word[:9]}')
    else:
        print(f'{i}.{word}')
    i= i+1


