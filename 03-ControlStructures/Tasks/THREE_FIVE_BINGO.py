text = ""

for i in range(1, 31):
    divisible_by_3 = i % 3 == 0
    divisible_by_5 = i % 5 == 0
    if(divisible_by_3 and divisible_by_5):
        text += "BINGO "
        continue
    elif(divisible_by_5):
        text +="FIVE "
    elif(divisible_by_3):
        text +="THREE "
    else:
        text +=f"{i} "

print(text)