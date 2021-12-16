age = 29
print('Is your age equal or over 27?')
print(age >= 27)

happiness = 'find someone you love'
print("\nIs happiness having lots of money?")
print(happiness == 'money')

dangerous_driver = 'max'
print('\nIs Max Verstappen a dangerous driver?')
print(dangerous_driver == 'MAX'.lower())

age = 69
print('\nIs you age greater than 30 and less than 70?')
print(age >= 30 and age <= 70)

national_champions = ['bahia', 'corinthians', 'flamengo', 'internacional']
print('\nIs Vitoria a national champion team?')
print('vitoria' in national_champions)

nice_languages = ['english', 'portuguese', 'spanish']
print('\nIs french a nice language to learn?')
print('french' in nice_languages)

nice_languages = ['english', 'portuguese', 'spanish']
boring_language = 'french'
if boring_language not in nice_languages:
    print(f'\n{boring_language.title()} is definetively not a nice language to learn!')