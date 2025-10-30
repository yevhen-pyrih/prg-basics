n = int( input("Length: ") ) - 1

list_of_primes = [2]
cnt = 0

i = 3
while(cnt < n):
    is_composed = False
    for j in list_of_primes:
        if i%j == 0:
           is_composed = True 
    if not is_composed:
        list_of_primes.append(i)
        cnt += 1
    i +=1

print(list_of_primes)