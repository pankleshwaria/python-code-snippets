print('Importing module...')

test = 'Test String'


def find_index(to_search, target):
    '''Find the index of value in the sequence'''
    for index, value in enumerate(to_search):
        if target == value:
            return index

    return -1

