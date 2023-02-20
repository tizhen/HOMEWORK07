# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения.
# Ввод: Вывод:
# print_operation_table(lambda x, y: x * y) 
# 1 2 3 4 5 6
# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36


# matrix = [
#     [1,2,3,4,5,6],
#     [2,21,31,41,5,6],
#     [3,22,32,42,5,6],
#     [4,23,33,43,5,6],
#     [5,24,34,44,5,6],
#     [6,24,34,44,5,6],
# ]
# # for i in matrix:
# #     print(i)
# matr=[]
# for i in range(1,6):
#     temp=[]
#     for j in range(1,6):
#         # print(i,j)
#         temp.append(i*j)
#     matr.append(temp)
# for i in matr:
#     print(''.join(f'{n:<3}' for n in i))




def print_operation_table(operation, num_rows=6, num_columns=6):
    for x in range(1, num_rows + 1):
        nums = []
        for y in range(1, num_columns + 1):
            num = operation(x, y)
            nums.append(num)

        print(''.join(f'{x:<4}' for x in nums))


print_operation_table(lambda x, y: x * y) 

