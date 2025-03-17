# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex используйте для проверки своего результата.

BASE = 16
result = ' '
replacements = {"10": "A", "11": "B", "12": "C", "13": "D", "14": "E", "15": "F"}

num = int(input('Enter number: '))
print(hex(num))

while num > BASE:
    result += str(num % 16)
    num //= BASE
result += str(num)

for old, new in replacements.items():
    result = result.replace(old, new)

new_result = result[::-1]
print(new_result)



