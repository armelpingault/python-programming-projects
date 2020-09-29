with open('files.txt') as files:
    with open('output.txt', 'w') as output:
        i = 1
        for line in files:
            output.write('{}. {}'.format(i, line))
            i = i + 1

print('Content of output.txt')
with open('output.txt') as output:
    print(output.read())
