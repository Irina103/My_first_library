def count_word_occurrences(input_line):
    # Подготавливаем словарь для сбора отдельных слов и их подсчёта
    dict_01 = dict()

    # Подготавливаем список для сбора результатов подсчёта
    lst = []

    # Разделяем входное предложение на отдельные слова
    splitted_text = input_line.split()

    # Итерируем каждое слово
    for key in splitted_text:
        if key not in dict_01:
            dict_01[key] = 0  # Если слова ещё нет в словаре, присваиваем ему счётчик 0
        else:
            dict_01[key] += 1  # Если слово есть в словаре, увеличиваем его счётчик

        # Добавляем в список результат для текущего слова
        lst.append(dict_01[key])

    # Возвращаем результат, преобразованный в строку
    return ' '.join(map(str, lst))

# Пример использования
# input_line = "one two one tho three one"
# result = count_word_occurrences(input_line)
# print(result)  # Вывод: "0 0 1 0 0 2"


def most_frequent_word(input_line):
    # Подготавливаем словарь для сбора отдельных слов и их подсчёта
    dict_01 = dict()

    # Разделяем входное предложение на отдельные слова
    splitted_text = input_line.split()

    # Заполняем словарь, подсчитывая количество повторений каждого слова
    for key in splitted_text:
        if key not in dict_01:
            dict_01[key] = 0  # Если слово не встречалось, присваиваем 0
        else:
            dict_01[key] += 1  # Если слово уже есть, увеличиваем его счётчик

    # Находим максимальное количество повторений
    max_v = max(dict_01.values())

    # Ищем все слова с максимальным количеством повторений
    lst = [k for k, v in dict_01.items() if v >= max_v]

    # Возвращаем слово с максимальной частотой, отсортированное лексикографически
    return sorted(lst)[0]

# Пример использования
# input_line = "apple orange banana banana orange"
# result = most_frequent_word(input_line)
# print(result)  # Вывод: "banana"

