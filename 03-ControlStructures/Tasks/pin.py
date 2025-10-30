PIN = input("Set a pin: ")

attempts = 3

while(attempts>0):
    input_PIN = input("Enter the PIN: ")
    if input_PIN == PIN:
        print("Correct!")
        break
    else:
        print("Incorrect...")
        attempts-=1

if attempts <= 0:
    print("Sorry, your payment card has been blocked.")