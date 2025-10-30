instagram = True
snapchat = False
facebook = True

amount = 0

if(instagram):
    amount += 1
if(snapchat):
    amount += 1
if(facebook):
    amount += 1

if(amount >= 2):
    print("GOOD BOY")
else:
    print("bad boy")