# Exceptions - Check Python Docs
# Mejor pedir perdón que pedir permiso - Filosofía

# First: Stop execute script
# Second: Show information to the user
# Third: Execute alternative code

# Exercise 1: Write a script witch enter file name and read it.
file_name = input('Enter file name: ')

print('Reading file...')
# Always type both keyword try and except
try:
    # Try execute the line above - Careful: One line of code only! Add exception type too
    f = open(file_name, "r")
except FileNotFoundError:
    # If couldn't execute execute this block
    print('The file not exist!')
except PermissionError:
    print('Do not have permission to read the file!')
    # Option 1: With else - If doesn't throw an exception continue with else block
    # Option 2: If you put the code under into try block maybe the exceptions confused
else:
    content = f.read()
    print(content)
    f.close()


