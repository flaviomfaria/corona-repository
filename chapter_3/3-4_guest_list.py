guest_list = ['ayrton senna', 'machado de assis', 'pedro II', 'beethoven']
print(f'Hi {guest_list[0].title()}, would you like to have dinner with me tonight?')
message = f"Hello {guest_list[2].upper()}, I would like to know more about the nineteenth century's history. Can we have dinner tonight?"
print(message)

great_writer = guest_list.pop(1).title()
print(f'Hello {great_writer}, could you teach me how to write a good book tonight at dinner?')
print(guest_list)
guest_list.insert(1,'machado de assis')
print(guest_list)
