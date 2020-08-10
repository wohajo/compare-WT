def crop_list(list, start, end):
    '''
    Returns list containing items cropped from starting string to ending string. 
    '''

    start = list.index(start) + 1
    end = list.index(end)

    return list[start:end]

def remove_weird_chars(list):
    '''
    Returns list without trailing spaces and unnecessary characters.
    '''

    new_list = []

    for item in list:
        new_list.append(item.strip().replace(u'\xa0', ' '))

    return new_list