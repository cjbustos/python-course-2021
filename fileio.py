# Steps:
# open != execute
# 1. Open the file (tell to OS who works with the file)
# Windows notation: C:\\Users\\carlos\\repos\\django-course-2022\\debug.log
# f_ref = open("/Users/carlos/repos/django-course-2022/debug.log")
# 2. Read the file
# content = f_ref.read()
# print(content)
# 3. Close the file
# f_ref.close()

# Note: 
# r - read
# w - write
# a - append

path_source = "/Users/carlos/repos/django-course-2022/debug.log"
path_to = "/Users/carlos/repos/python-course-2021/requests.log"

def read_file(path: str):
    f = open(path)
    content = f.read()
    f.close()
    return content

def write_file(path: str, content: str):
    f = open(path, "w")
    f.write(content)
    f.write("\nend of file")
    f.close()

# print(read_file(path_source))

write_file(path_to, read_file(path_source))
print(read_file(path_to))
