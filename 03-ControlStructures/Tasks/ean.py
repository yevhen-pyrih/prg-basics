ean = input("TYPE EAN-13: ")

if(len(ean)< 13):
    print("error")
else:
    ean = int(ean)
    code = f"{ean[0]}{ean[1]}{ean[2]}"
    if(code == "590"):
        print("POLAND!!!!!!")