guest_list = ['ayrton senna', 'machado de assis', 'pedro II', 'beethoven']
print('Hello everyone, I found a bigger table for our dinner tonight. I have invited more guests to join us!')
best_driver = ('lewis hamilton')
guest_list.append(best_driver)
dangerous_driver = 'max verstappen'
guest_list.insert(0, dangerous_driver)
print(guest_list)
print(f'Hi {best_driver.title()} and {dangerous_driver.title()}, be very welcome to our dinner table! Our guests {guest_list[1].title()}, {guest_list[2].title()}, {guest_list[3].title()} and {guest_list[4].title()} were waiting for you!')