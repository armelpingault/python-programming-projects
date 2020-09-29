def get_input(type):
    ###This function will get the input of the user###
    return input('Type a {}: '.format(type))

def fill_blanks():
    ###This function will fill the blanks###
    print('There was a {} that tends to {} a {} tree.'.format(get_input('noun'), get_input('verb'), get_input('adjective')))

help(get_input)
help(fill_blanks)
fill_blanks()
