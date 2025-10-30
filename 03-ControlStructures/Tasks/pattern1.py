size = int( input("Size: ") )

counter = -size

while(counter <= size):
    line = ""
    for i in range(0,size-abs(counter)):
        line += "*"
    print(line)
    counter += 1