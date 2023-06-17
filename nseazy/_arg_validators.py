
def _validate_vkwargs_dict(vkwargs):
    """
    Check that we didn't make a typo in any of the things
    that should be the same for all vkwargs dict items:

    {kwarg : {'Default': ... , 'Description': ... , 'Validator': ...} }
    """
    for key, value in vkwargs.items():
        # has been changed to 3 to support descriptions
        if len(value) != 3:
            raise ValueError('Items != 3 in valid kwarg table, for kwarg "'+key+'"')
        if 'Default' not in value:
            raise ValueError('Missing "Default" value for kwarg "'+key+'"')
        if 'Description' not in value:
            raise ValueError('Missing "Description" value for kwarg "'+key+'"')
        if 'Validator' not in value:
            raise ValueError('Missing "Validator" function for kwarg "'+key+'"')