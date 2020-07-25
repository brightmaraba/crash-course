magicians = ['Alice', 'David', 'Caroline']

for magician in magicians:
    print(magician)

for magician in magicians:
    print(f"{magician.title()}, that was an awesomet trick!")


for value in range(1, 5):
    print(value)

squares = [value**2 for value in range(1, 11)]
print(squares)