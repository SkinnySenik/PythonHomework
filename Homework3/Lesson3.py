# 1.
"""
import random

length = int(input("type the length of the list: "))
number = int(input("type the numeral X: "))
NumList = [ ]
count = 0

for i in range(length):
    NumList.append(random.randint(1,100))
    min_n = max(NumList) - number

    if int(NumList[i]) == number:
        count += 1

for i in set(NumList):
    if abs(i - number) < min_n:
        min_n = abs(i - number)
        closest = i

print(NumList)
print(f"we can meet the given number {count} times in the list")

if count == 0:
    print(f"therefore the closest number to it is {closest}")
"""
# 2.
"""
English = "abcdefghijklmnopqrstuvwxyz"
Russian = "абвгдеёжзийклмнопрстуфхцчьъыэюя"

EngAlphabet = {1:"AEIOULNSTR", 2:"DG", 3:"BCMP", 4:"FHVWY", 5:"K" , 8:"JX", 10:"QZ"}
RusAlphabet = {1:"АВЕИНОРСТ", 2:"ДКЛМПУ", 3:"БГЁЬЯ", 4:"ЙЫ", 5:"ЖЗХЦЧ", 8:"ШЭЮ", 10:"ФШЪ"}

word = input("write a word on english or russian language: ")
sum = 0

if word[0].lower() in English:
    for letter in word:
        for key ,value in EngAlphabet.items():
            if letter.upper() in value:
                sum += key
    print(f"for this word you get {sum} points")

elif word[0].lower() in Russian:
    for letter in word:
        for key, value in RusAlphabet.items():
            if letter.upper() in value:
                sum += key
    print(f"for this word you get {sum} points")
"""