distance = int(input('How far would you like to travel in miles? '))
if distance < 3:
    how = 'walking'
elif distance < 300:
    how = 'driving'
else:
    how = 'flying'
print('I suggest {} to your destination.'.format(how))
