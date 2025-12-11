temps = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}

print("Cities with temperatures higher than 0: ", list(filter(lambda x: temps[x] > 0, temps.keys())))