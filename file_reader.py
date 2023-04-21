"""
Now that we have a text file, auspiciously named TextFile1.txt, we can do some
things with that file in Python.

'And here....we.......go'

"""
with open('TextFile1.txt') as file_object:
    contents = file_object.read()

print(contents)
print("\n")
"""
This is relative file pathing.  I won't do it here but you can also use full path
such as '/root/Directory/file.txt'.  Also of note, python uses / and not \ 
since \ is an escape character in python.
"""
with open('text_files/another_text_file.txt') as file_object:
    contents = file_object.read()

print(contents)