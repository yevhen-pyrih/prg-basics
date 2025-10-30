age = int(input("Your age: "))
age_category = "child"
if age >= 65:
    age_category = "senior"
elif age >= 20:
    age_category = "adult"
elif age >= 12:
    age_category = "teen"

print(f"Your age category is {age_category.upper()}")