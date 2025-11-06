###
# Calculates the sum of the digits in a number
#
def sum_digits(number):
    result = 0
    for i in str(number):
        result += int(i)
    return result

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print('The sum of the digits in the number ... is ...', result)