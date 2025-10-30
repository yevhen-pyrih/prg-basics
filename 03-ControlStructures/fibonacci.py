prev = 1
current = 0

cnt = int(input("Lenght: "))

for i in range(0, cnt):
    print(current)
    new = prev + current
    prev = current
    current = new


