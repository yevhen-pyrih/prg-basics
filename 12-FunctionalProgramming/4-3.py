grades = [3.0,5.0,2.0,3.5,4.0,4.0,3.5,2.0,4.0,2,0]      

without2 = list(filter(lambda x: x>2, grades))

result = sum(without2)/len(without2)

print(result)