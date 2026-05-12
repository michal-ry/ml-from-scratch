def mode(elements):

    '''
    Calculate the mode or modes of a list.

    Args:
        elements (list): List of hashable, non-boolean values.

    Returns:
        list: List of the most frequent value or values.
    '''

    if not isinstance(elements, list):
        raise TypeError("elements must be a list.")
    
    if not elements:
        raise ValueError('elements must not be empty.')
    
    if any(isinstance(e, bool) for e in elements):
        raise TypeError("elements must not contain bool values.")
    
    counter = {}

    for e in elements:
        if e not in counter:
            counter[e] = 1
        else:
            counter[e] += 1

    modes = []
    count = 0

    for key, value in counter.items():
        if value > count:
            modes.clear()
            modes.append(key)
            count = value
        elif value == count:
            modes.append(key)

    return modes