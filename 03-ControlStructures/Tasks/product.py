previous_price = float( input("Previous price: ") )
price = float( input("Current price: ") )

percentage_diff =(price - previous_price)/previous_price*100

if percentage_diff <= -10:
    print(f"Buy the project! \nThe price decreased by {-int(percentage_diff)}%")
