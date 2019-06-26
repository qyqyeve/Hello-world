from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file{filename}:")
print(txt.read())

print("type the filename again:")
filename_again = input(">")

txt_again = open(filename_again)

print(txt_again.read())
