current_users = ['rio', 'tokyo', 'berlin', 'professor', 'palermo']
new_users = ['estocolmo', 'denver', 'rio','Palermo', 'nairobi']
for new_user in new_users:
    if new_user.lower() in current_users:
        print(f'\nHi there {new_user.title()}. Username not available =/ Please enter a new username.')
    else:
        print(f'\nHi there {new_user.title()}. Username is available.')