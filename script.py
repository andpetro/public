from sys import argv

script, filename = argv

print(f"""We're going to erase {filename}.
If you don't want that, hit CTRL-C (^C).
If you do want that, hit RETURN.""")

input("?")

target = open(filename, 'w')

print(f"Say goodbuy to {filename}.")

target.truncate()

print("I'm goint to ask you for three lines")

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print(f"Now I'm adding these lines to the {filename}")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)

print("And finally, we close it.")
target.close()

target = open(filename, 'r')

for line in target:
    print(line)

target.close()








