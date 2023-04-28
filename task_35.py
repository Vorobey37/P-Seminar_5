"""
Напишите функцию, которая принимает одно число и
проверяет, является ли оно простым
Напоминание: Простое число - это число, которое
имеет 2 делителя: 1 и n(само число)
Input: 5
Output: yes
"""
n = int(input("Введите число для проверки: "))
def SimpleOrNot(a):
    count = 0
    for i in range(1, a):
        if a%i == 0:
            count+=1
    if count < 2:
        print("yes")
    else: 
        print("no")
SimpleOrNot(n)
