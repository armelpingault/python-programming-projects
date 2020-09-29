dict = [
    { 'Name': 'Jeff', 'Fact': 'Is afraid of clowns.' },
    { 'Name': 'David', 'Fact': 'Plays the piano.' },
    { 'Name': 'Jason', 'Fact': 'Can fly an airplane.' },
]


def display():
    for element in dict:
        print('{}: {}'.format(element['Name'], element['Fact']))


print()
print('Display each person and their interesting fact:')
print()

display()

print()
print('Change a fact about one of the people:')
print()

dict[0]['Fact'] = 'Is afraid of heights.'
display()

print()
print('Add an additional person and corresponding fact:')
print()

dict.append({ 'Name': 'Jill', 'Fact': 'Can hula dance.' })
display()

    
