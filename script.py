from sys import argv

script, filename = argv

print(f"""We're going to erase {filename}.
If you don't want that, hit CTRL-C (^C).
If you do want that, hit RETURN.""")

input("?")

target = open(filename, 'w')

print(f"Say goodbuy to {filename}.")

target.truncate()

