'''
Earthquake Impact: Input some numbers, do some simple arithmetic, output results. (Python3)'''


magnitude = float(input())
distance = float(input())  
impact = 10 ** ((1.5 * magnitude) - (1.5 * distance / 100))
print(impact)