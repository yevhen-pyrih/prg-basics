price = float( input("Price: "))

amount = int( input("Amount: "))

total_cost = 2*price + (amount-2)*price*3/4 if amount > 2 else amount*price

print(total_cost)

