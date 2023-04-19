'''Factor:  Calculate temperature that a person feels because of the wind (Python3)'''
magnitude = float(input())
distance = float(input())  
impact = 10 ** ((1.5 * magnitude) - (1.5 * distance / 100))
print(impact)
