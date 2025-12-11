multi = lambda n1,n2: n1*n2
sum = lambda n1, n2: n1+n2

def calc(function, n1, n2):
    return function(n1,n2)

# print(calc(multi, 3, 6))
# print(calc(sum, 3, 6))

arr = [3,4,5,6]
print(list(map(lambda x: x*2, arr)))