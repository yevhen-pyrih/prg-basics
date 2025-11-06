###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides
#
import math
def triangle_area(a,b,c):
    p = (a+b+c)/2
    return math.sqrt(p*(p-a)*(p-b)*(p-c))

print('The area of ​​a triangle with sides ... is ...', triangle_area(3, 4, 5))
print('The area of ​​a triangle with sides ... is ...', triangle_area(5, 12, 13))
print('The area of ​​a triangle with sides ... is ...', triangle_area(7, 24, 25))