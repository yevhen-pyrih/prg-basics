row = 1

while(row <=3):
    text = ""
    column = 1
    while(column<=3):
        text += f"{(3-row)*3 + column} "
        column += 1
    row += 1
    print(text)