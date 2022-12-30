print('#####################################class-2#####################################')

# Example1: while loop

# month = int(input('Enter month:'))

# while month > 12 or month < 1:
#     print('Incorrect format!')
#     month = int(input('Enter month:'))
# print('The format is correct!', month)

# Python style 1
# while month not in range(1,13):
#     print('Incorrect format!')
#     month = int(input('Enter month:'))
# print('The format is correct!', month)

# Python style 2 - shorter
# while (month := int(input('Enter month:'))) not in range(1,13):
#     print('Incorrect format!')

# print('The format is correct!', month)

# Example2: for loop
week = ('Monday', 'Tuesday', 'Wednesday', 'Thrusday', 'Friday', 'Saturday', 'Sunday')

for day in week:
    if day != 'Monday':
        print(day)

dictionary_of_contacts = {'1150607080':'Tom Harris', '1140506070':'Joe Smith'}

for phone in dictionary_of_contacts:
    print(dictionary_of_contacts[phone])

for phone, name in dictionary_of_contacts.items():
    print(name, 'has this phone:', phone)