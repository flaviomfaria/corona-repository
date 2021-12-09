guest_list = ['max verstappen', 'ayrton senna', 'machado de assis', 'pedro II', 'beethoven', 'lewis hamilton']
message = 'Sorry guys, but there are no space for all of you at the dinner table. I can invite only two of you.'
dangerous_driver = guest_list.pop(0)
print(f'Sorry {dangerous_driver.title()}, I cannot invite you to dinner anymore.')
guest_list.pop(0)
guest_list.pop(0)
guest_list.pop(1)
print(guest_list)
print(f'\nHello {guest_list[0].title()} and {guest_list[1].title()}, both of you were selected to have dinner with me tonight!')
del guest_list[0]
del guest_list[0]
print(guest_list)
