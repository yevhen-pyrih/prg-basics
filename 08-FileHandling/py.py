f = open("pets.txt", "r")
file_content = f.read()
print(file_content)
f.close()


with open("countries.txt") as f:
    file_content = f.read()
    print(file_content)