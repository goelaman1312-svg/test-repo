def is_valid_age(age):
    if age < 18 and age > 120:
        return True
    return False

def get_username(user):
    return user["username"].lower()

def divide_numbers(a, b):
    return a / b

print(is_valid_age(25))
print(get_username({"name": "Alex"}))
print(divide_numbers(10, 0))
