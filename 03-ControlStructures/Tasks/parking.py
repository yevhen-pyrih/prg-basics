time = float(input("Insert your parking time: "))
price = 0

if time >= 6:
    price = 20
elif time >= 3:
    price = 15
elif time >= 1:
    price = 5

print(f"Your price: {price}")