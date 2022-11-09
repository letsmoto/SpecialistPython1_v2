# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне - слева короткие слова дополняем символами пробела

# Исходные данные:
fruits = ["яблоко", "банан", "киви", "арбуз"]

# TODO: your code here
fruits = ["яблоко", "банан", "киви", "арбуз"]
max_len_word = 0

for fruit in fruits:
    if len(fruit) > max_len_word:
        max_len_word = len(fruit)

max_string = max_len_word + len("x. ")
for fruit in enumerate(fruits):
    probels = " " * (max_string - 2 - len(fruit[1]))
    print(str(fruit[0] + 1) + "." + probels + fruit[1])
    
# Пример вывода:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Важно! Ваше решение должно работать с любыми корректными "исходными данными"
# Проверьте это, добавив или удалив несколько элементов списка
