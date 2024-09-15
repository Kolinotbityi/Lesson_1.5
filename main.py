from math import trunc

immutable_var = 777, 2.3, True, "Hello"
print(immutable_var)
print(immutable_var[0])
# immutable_var[0] = 111 - кортеж не поддерживает изменение элементов
# Но можно изменить элемент внутреннего списка
immutable_var_1 = [44,500], 5.5
immutable_var_1[0][1] = 1
print(immutable_var_1)
mutable_list = [934234, 55.54, False]
print(mutable_list)
mutable_list[2] = True
print(mutable_list)

