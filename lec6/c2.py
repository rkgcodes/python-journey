# stores a name in a list

names = []

for _ in range(3):
    names.append(input("What's your name? "))


for name in sorted(names, key=None, reverse=False):

    print(f"hello, {name}")


