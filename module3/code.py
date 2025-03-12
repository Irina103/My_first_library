def calculate_product_sum(lst):
    # Подготавливаем словарь для хранения произведений
    dic_01 = dict()

    # Итерируем по парам элементов списка в двух циклах
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            num1 = lst[i]
            num2 = lst[j]

            # Считаем произведение
            product = num1 * num2

            # Если произведение еще не в словаре, добавляем его
            if product not in dic_01:
                dic_01[product] = 1
            else:
                # Если произведение уже есть, увеличиваем его счетчик
                dic_01[product] += 1

    # Подготавливаем переменную для суммы
    sm = 0

    # Итерируем все значения словаря
    for count in dic_01.values():
        # Если значение больше 1 (т.е. произведение встречается несколько раз)
        if count > 1:
            # Применяем формулу для добавления к общей сумме
            sm += count * (count - 1) * 4

    return sm

# Пример использования
# lst = [2, 3, 4, 6]
# result = calculate_product_sum(lst)
# print(result)  # Вывод: результат суммы


def find_elements_with_frequency(nums):
    # Подготавливаем словарь с помощью dict comprehension
    n = len(nums)
    dict_01 = {key: 0 for key in range(1, n+1)}  # Создаем словарь с ключами от 1 до n, значениями 0

    # Итерируем все элементы входного списка
    for el in nums:
        # Добавляем в словарь частоту встречаемости текущего элемента
        freq = nums.count(el)
        dict_01[el] = freq  # Обновляем значение частоты для текущего числа

    # Создаем список с результатом: элементы, которые встретились 2 раза или 0 раз
    result = [key for key, value in dict_01.items() if value == 2 or value == 0]

    return result

# Пример использования
# nums = [1, 2, 2, 4]
# result = find_elements_with_frequency(nums)
# print(*result)  # Выводит элементы, встретившиеся 2 раза или 0 раз


