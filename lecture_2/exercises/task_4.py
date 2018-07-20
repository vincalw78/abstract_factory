# Створити лямбда функцію, що множить число на рандом від 1 до 10.
#  Згенерувати список від 1 до 10. Застосувити лямда функцію до цього списку,
#  відфільтрувати цей список ( позбутись непарних чисел) і знайти суму списку.
#  ( Використати map, reduce, filter )
import random
from functools import reduce

# list
li = list(range(1, 11))

# lambda multiplier
multiplier = lambda x: x*random.randint(1, 11)

# multiplied list
li_mapped = list(map(multiplier, li))

# filtered list
li_filtered = list(filter(lambda x: True if x % 2 == 0 else False, li_mapped))

# summed up list
li_summed_up = reduce(lambda x, y: x + y, li_filtered)

print(li_mapped, li_filtered, li_summed_up, sep='\n')
