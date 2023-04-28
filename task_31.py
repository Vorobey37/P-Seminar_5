"""
Последовательностью Фибоначчи называется
последовательность чисел a0
, a1
, ..., an
, ..., где
a0
 = 0, a1
 = 1, ak
 = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи
Input: 7
Output: 21
Задание необходимо решать через рекурсию
"""


N = int(input("Введите число: "))
def Fibonachi(k):
    if k == 0:
        return 0
    if k == 1:
        return 1 
    return Fibonachi(k-1) + Fibonachi(k-2)


print(Fibonachi(N))
