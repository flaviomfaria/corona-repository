age = 66
if age < 4:
    price = 0
elif age <18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
print(f'Your admission cost is ${price}. Thank you.')

age = 59
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20
print(f'\nYour admission cost is ${price}. Thank you.')