guests = ['Einstein', 'Tesla', 'Obama', 'Martin']
print('*****************************')
for guest in guests:
    print(f"Good Morning {guest}, kindly join us for dinner at 7 PM")


print('*****************************')
print(f"Sorry, {guests[-1]} will not make it to dinner")
guests.remove('Martin')
new_guest = 'Clinton'
guests.append(new_guest)

print('*****************************')
print(guests)

print('*****************************')
for guest in guests:
    print(f"Good Morning {guest}, kindly join us for dinner at 7 PM")

guests.insert(3, 'Fauchi')
guests.insert(4, 'Malala')
guests.append('Abey')

print('*****************************')
print(guests)

print('*****************************')
for guest in guests:
    print(f"Good Morning {guest}, kindly join us for dinner at 7 PM")

print('*****************************')
print("We can only invite two people to dinner")

print('*****************************')
count = len(guests) - 1
print(count)

print('*****************************')
while count > 1:
    uninvited_guest = guests.pop(count)
    print(f"We are sorry {uninvited_guest}, we have limited space due to Covid Restrictions")
    count = count - 1

print('*****************************')
for guest in guests:
    print(f"Good Morning {guest}, kindly join us for dinner at 7 PM")

print('*****************************')

count = len(guests) - 1

while count != -1:
    del guests[count]
    count = count - 1

print('*****************************')
print(f"The list should now be empty {guests}")

