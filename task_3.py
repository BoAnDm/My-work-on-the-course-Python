# TODO  Напишите функцию count_letters

def text_only_letters(str_):
    small_register = str_.lower()
    spisok_letters = []
    for i1 in small_register:  # текст без специальных символов
        if i1.isalpha():
            spisok_letters += list(i1)
    return spisok_letters

def count_letters(str_):
    str_.lower()
    dict_letters = {}
    for i2 in text_only_letters(str_):  # подсчет количества каждой буквы в тексте
        if i2 not in dict_letters:
            dict_letters[i2] = 1
        else: dict_letters[i2] += 1
    return dict_letters


# TODO Напишите функцию calculate_frequency

def calculate_frequency(str_):
    total_letters = len(text_only_letters(str_))  # подсчет общего количества букв
    dict_letters = count_letters(str_)  # создаем словарь
    for i3 in dict_letters:  # замена в словаре количества каждой буквы на ее частоту
        value = dict_letters[i3]
        letter_frecuency = round(value / total_letters, 2)
        dict_letters[i3] = letter_frecuency
    return dict_letters


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте

for i in calculate_frequency(main_str):
    print(f'{i}: {calculate_frequency(main_str)[i]:.2f}')