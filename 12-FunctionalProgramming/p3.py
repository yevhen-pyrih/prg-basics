arr = [4,2,17,21,3,5,1,19]

# result = []

# for item in arr:
#     if item > 4:
#         result.append(item)

# print(result)

result = list(filter(lambda x: x>4, arr))

print(result)