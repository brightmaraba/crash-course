#List
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

#Iterate List
for bicycle in bicycles:
    print(bicycle)

#Accessing List Elements
print(bicycles[0])
print(bicycles[-1])
print(bicycles[2:])
print(bicycles[:2])

#Using element
print(f"My first bicycle was: {bicycles[3].title()}")

#Changing elements
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

#Adding Elements
motorcycles.append('honda')
print(motorcycles)

#Insert Elements
motorcycles.insert(3, 'tesla')
print(motorcycles)

#Removing Elements using del
del motorcycles[3]
print(motorcycles)

#Removing Elements using pop
popped_motorcycle = motorcycles.pop()
popped_motorcycle_index = motorcycles.pop(-1)
print(motorcycles)
print(popped_motorcycle)
print(popped_motorcycle_index)

#Removing Elements by value
motorcycles.remove('ducati')
print(motorcycles)

#Organising lists
#Sort permanently
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
#Sort Temporarily
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(f"Here is the original list: {cars}")
print(f"Here is the sorted list: {sorted(cars)}")
print(f"Here is the original list again: {cars}")

#Reverse a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(f"This is a reversed list: {cars}")

#Finding the lenght of a list
print(len(cars))