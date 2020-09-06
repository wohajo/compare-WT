from constants import WORDS_TO_REMOVE

def list_to_chunks(lst, n):
    '''
    Crops list into chunks with n values and returns list of lists.
    '''
    new_list = [lst[i:i + n] for i in range(0, len(lst), n)]  

    return new_list

def crop_list(list, start, end):
    '''
    Returns list containing items cropped from starting string to ending string. 
    '''

    start = list.index(start) + 1
    end = list.index(end)

    return list[start:end]

def remove_weird_chars(lst):
    '''
    Returns list without trailing spaces and unnecessary characters.
    '''

    new_list = []

    for item in lst:
        new_list.append(item.strip().replace(u'\xa0', ' '))

    return new_list

def remove_empty_lists(lst):
    '''
    Removes empty lists from list and returns a cleaned up copy.
    '''
    
    new_list = list(filter(lambda x: x, lst))

    return new_list

def remove_unwanted_words(lst):
    '''
    Removes unwanted words from list and returns a new copy.
    '''

    new_list = [list(filter(lambda w: w not in WORDS_TO_REMOVE, sublist)) for sublist in lst]

    return new_list

def flatten_list(lst):
    '''
    Flattens 2D list to 1D and returns it.
    '''

    flattened_list = [y for x in lst for y in x]

    return flattened_list
