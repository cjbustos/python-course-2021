print('#####################################class-1#####################################')
# Example 1: print a message
print('Welcome to Class 1! (without variable')

# Example 2: Declare variables
msg = 'Welcome to Class 1! (from variable)'

# Example 3: Show variable type
print(type(msg))

# Example 4: Primitive types
int_number = 1
float_number = 3.1415
is_boolean = True

# Example 5: lists (vectors), tuples (immutables) and dictionaries
# Remember -> lists and dictionaries are mutable
odd_numbers_list = [1, 3, 5, 7, 9]
odd_numbers_list.append(11)
data_of_new_therapist = ['Joseph', 42, 'Psychology', True]
tuple_of_levels = ('KINDER', 'PRIMARY', 'HIGH SCHOOL')
dictionary_of_contacts = {'1150607080':'Tom Harris', '1140506070':'Joe Smith'}
print(dictionary_of_contacts['1140506070'])

# Add new contact to the dictionary ->
dictionary_of_contacts['1130405060'] = 'John Doe'

# Example 6: Slicing apply for list, tuples and strings (ordered collections) 
# Warning: Slicing doesn't change the original string, if you'll change it use a new variable for save value
fullname = 'John Doe'
name = fullname[0:4]
surname = fullname[5:]
print('The first name is ' + name + ' and the surname is ' + surname)




