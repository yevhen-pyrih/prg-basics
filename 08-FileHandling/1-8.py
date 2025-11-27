def read_from_file(file_name):
    with open(file_name) as f:
        content = f.read()
    return content


pets = read_from_file("pets.txt")

number = len(pets.split())

print(pets, "")

print("Word count: ", number)