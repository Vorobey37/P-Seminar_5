"""
Хакер Василий получил доступ к классному журналу и
хочет заменить все свои минимальные оценки на
максимальные. Напишите программу, которая
заменяет оценки Василия, но наоборот: все
максимальные – на минимальные.
Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1

"""
import random


n = int(input("Введите количество оценок в журнале: "))

def ScoreQuality(a):
    scoreList = []
    for i in range(a):
        scoreList.append(random.randint(1, 5))
    return scoreList

def ChangeScores(list):
    ma = max(list)
    mi = min(list)
    for i in range(len(list)):
        if list[i] == ma:
            list[i] = mi
    return list


list1 = ScoreQuality(n)
print(list1)
print(ChangeScores(list1))

