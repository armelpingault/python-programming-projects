airports = [
    ('O’Hare', 'ORD'),
    ('Los Angeles', 'LAX'),
    ('Dallas/Fort Worth', 'DFW'),
    ('Denver', 'DEN'),
]

for airport in airports:
    (name, code) = airport
    print('The code for {} International Airport is {}.'.format(name, code))
