def run_cat(what = ''):
    if len(what) == 0:
        what = input('Type something to say: ')
    length = len(what)
    print('         {}'.format('_' * length))
    print('       < {} >'.format(what))
    print('         {}'.format('-' * length))
    print('        /')
    print(' /\_/\ /')
    print('( o.o )')
    print(' > ^ <')

if __name__ == '__main__':
    run_cat()
