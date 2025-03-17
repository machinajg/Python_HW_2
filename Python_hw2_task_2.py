# Напишите программу, которая принимает две строки вида “a/b” -
# дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions

import math
import fractions
from math import gcd
from fractions import Fraction

num_1 = int(input('Enter numerator 1: '))
den_1 = int(input('Enter denominator 1: '))
num_2 = int(input('Enter numerator 2: '))
den_2 = int(input('Enter denominator 2: '))

low_com_den = int(den_1 * den_2 / gcd(den_1, den_2))
com_num = int((low_com_den / den_1 * num_1) + (low_com_den / den_2 * num_2))
gcd_1 = (gcd(com_num, low_com_den))
num_3 = int(com_num / gcd_1)
den_3 = int(low_com_den / gcd_1)
print('{}/{}'.format(num_3, den_3) if num_3 != den_3 else num_3)

num_product = int(num_1 * num_2)
den_product = int(den_1 * den_2)
gcd_2 = gcd(num_product, den_product)
num_4 = int(num_product / gcd_2)
den_4 = int(den_product / gcd_2)
print('{}/{}'.format(num_4, den_4) if num_4 != den_4 else num_4)

print(Fraction(num_1, den_1) + Fraction(num_2, den_2))
print(Fraction(num_1, den_1) * Fraction(num_2, den_2))