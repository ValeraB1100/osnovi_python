from functools import reduce


def my_func(prev_el, el):
    return prev_el * el


list0 = [el for el in range(100, 1001) if el % 2 == 0]
print(reduce(my_func, list0))
# а тут должно было получиться такое огромное значение?) я позаимствовал из вебинара ваши названия переменных,
# надеюсь, что это не противозаконно...
# что-то я до сих пор сомневаюсь в своих способностях к обучению(
