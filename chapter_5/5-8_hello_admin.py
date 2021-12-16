usernames = ['admin', 'armin', 'john', 'kiera', 'aoife']
for username in usernames:
    if username == 'admin':
        print('Hello admin, would you like to see a status report?')
    else:
        print(f'\nHello {username}, thank you for logging in again.')