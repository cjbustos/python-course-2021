import os

file_name = input('Enter file name: ')

if os.path.exists(file_name):
    print('Reading file...')
    f = open(file_name)
    content = f.read()
    print(content)
    f.close()
else:
    print('The file does not exists!')