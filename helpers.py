def crop_list(list, start, end):
    '''
    Returns list containing items cropped from starting string to ending string. 
    '''

    start = list.index(start) + 1
    end = list.index(end)

    return list[start:end]