my_pizzas = ['tuna','mozzarella','chiken with cream cheese','portuguese','four cheeses']
friend_pizzas = my_pizzas [:]
my_pizzas.append('chocolate')
friend_pizzas.append('romeo and juliet')

print('My favorite pizzas are:')
for my_pizza in my_pizzas:
    print(my_pizza)
print("\nMy friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)