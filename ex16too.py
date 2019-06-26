from sys import argv

script, filename = argv

txt = open(filename)

print(f"here's your file {filename}.")
print(txt.read())

print("type the filename :")
file = input(">>>")

txt =open(file)

print(txt.read())