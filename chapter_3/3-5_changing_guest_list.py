guest_list = ['ayrton senna', 'machado de assis', 'pedro II', 'beethoven']
cannot_dinner = 'beethoven'
guest_list.remove(cannot_dinner)
new_guest = 'mozart'
guest_list.insert(0,new_guest)
print(guest_list)
print(f'Considering {cannot_dinner.title()} will not dinner with us tonight, I invited {new_guest.title()}, which is coming over already.')
