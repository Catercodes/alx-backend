
def access_nested_map(nested_map, path):
    """
    Accesses a nested dictionary using a list of keys.
    
    :param nested_map: The dictionary to access.
    :param path: A list of keys specifying the path to the desired value.
    :return: The value at the end of the path.
    """
    current_value = nested_map
    for key in path:
        current_value = current_value[key]
    return current_value

