sortedList = []

with open('animals.txt') as animals:
    for animal in animals:
        sortedList.append(animal)

sortedList = sorted(sortedList)

with open('animals-sorted.txt', 'w') as animalsSorted:
    for animal in sortedList:
        animalsSorted.write(animal)

print('Content of animals-sorted.txt')
with open('animals-sorted.txt') as animalsSorted:
    print(animalsSorted.read())
