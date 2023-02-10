"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" и обработав исключение,
придумайте как это сделать
"""

words = ['attribute', 'класс', 'функция', 'type']


def check_byte1(word):
    fl = True
    for i in range(len(word)):
        if ord(word[i]) > 255:
            fl = False
            break
    return fl


def check_byte2(word):
    try:
        b = bytes(word, encoding='ascii')
    except UnicodeEncodeError:
        return False
    else:
        return True


print('Вариант на основе логики:')
for el in words:
    if check_byte1(el):
        print(
            f"Слово '{el}' возможно записать в байтовом типе с помощью маркировки b''"
        )
    else:
        print(
            f"Слово '{el}' невозможно записать в байтовом типе с помощью маркировки b''"
        )

print('Вариант на основе исключения:')
for el in words:
    if check_byte2(el):
        print(
            f"Слово '{el}' возможно записать в байтовом типе с помощью маркировки b''"
        )
    else:
        print(
            f"Слово '{el}' невозможно записать в байтовом типе с помощью маркировки b''"
        )
