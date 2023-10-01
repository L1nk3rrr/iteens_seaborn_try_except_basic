import logging

def get_sum(a, b):
    return a + b
 
assert get_sum(1, 2) == 3
assert get_sum(2, 2) == 4
# assert get_sum(3, 10) == 12 Посилка!
assert get_sum(5, 5) == 10

# try:
#     a = open('text.txt')
#     # print(a.asdasd)
# except (ZeroDivisionError, AttributeError) as error:
#     print(error)
#     print("Так не можна")
# else:
#     print("Все гуд")
# finally:
#     print('Я завжди є')
#     a.close()


def division_ten_by_user_num():
    try:
        num = int(input("Введіть число: "))
    except ValueError as error:
        print()
        print("Вводити можна лише числа")
    else:
        if num != 0:
            result = 10/num
        else:
            print("Ділення на нуль неможливе")
        return result

print(division_ten_by_user_num())