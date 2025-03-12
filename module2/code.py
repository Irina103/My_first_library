def get_previous_word_indices(input_line):
    # Разделяем строку на отдельные слова
    text_split = input_line.split()

    # Подготавливаем словарь для хранения слова и его первого индекса
    dict_01 = dict()

    # Создаём список для хранения индексов (по умолчанию все элементы -1)
    lst = [-1 for _ in range(len(text_split))]

    # Итерируем по индексам списка слов
    for idx in range(len(text_split)):
        # Если слово уже встречалось
        if text_split[idx] in dict_01:
            # Заменяем в списке индексов соответствующий элемент на предыдущий индекс
            lst[idx] = dict_01[text_split[idx]]

        # Присваиваем ключу слова текущий индекс
        dict_01[text_split[idx]] = idx

    return lst

# Пример использования
# input_line = "one two one one three three"
# result = get_previous_word_indices(input_line)
# print(result)  # Вывод: [-1, -1, 0, 2, 3]

