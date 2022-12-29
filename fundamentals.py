# Example: print a message
print('Welcome to Class 1! (without variable')

# Example: Declare different variables
msg = 'Welcome to Class 1! (from variable)'

# Types:
print(type(msg))
print(msg)

integer_number = 1
print(type(integer_number))

float_number = 3.1415
print(type(float_number))

is_ready = True
print(type(is_ready))

# lists (vectors), tuples and dictionaries
# lists and dictionaries are mutables
odd_numbers = [1, 3, 5, 7, 9]
odd_numbers.append(11)
print(type(odd_numbers))
print(odd_numbers)

therapist = ['Carlos', 42, 'Psicologo', True]
print(therapist[0])

level = ('INICIAL', 'PRIMARIO', 'SECUNDARIO')
print(type(level))

os = {'001':'OSDE', '002':'GALENO'}
therapists = {'62803':'Carlos Bustos','61809':'Jorge Sosa' }
print(type(os))
print(os['001'])
print(therapists['62803'])

# new therapist added
therapists['60100'] = 'Catalina Peréz'
print(therapists)

# Slicing apply for list, tuples and strings (ordered collections). Slicing doesn't change the string.
fullname = 'Carlos Bustos'

name = fullname[0:6]
surname = fullname[7:13]

print(name, surname)
print(odd_numbers[0:3])




