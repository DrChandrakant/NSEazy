
def _validate_vkwargs_dict(vkwargs):

    for key, value in vkwargs.items():
        
        if len(value) != 3:
            raise ValueError('Items != 3 in valid kwarg table, for kwarg "'+key+'"')
        if 'Default' not in value:
            raise ValueError('Missing "Default" value for kwarg "'+key+'"')
        if 'Description' not in value:
            raise ValueError('Missing "Description" value for kwarg "'+key+'"')
        if 'Validator' not in value:
            raise ValueError('Missing "Validator" function for kwarg "'+key+'"')
        
def _check_kwargs(kwargs, vkwargs):

    config  = {}
    for key, value in vkwargs.items():
        config[key] = value['Default']

    for key in kwargs.keys():
        if key not in vkwargs:
            raise KeyError('Unrecognized kwarg="'+str(key)+'"')
        else:
            value = kwargs[key]
            try:
                valid = vkwargs[key]['Validator'](value)
            except Exception as ex:
                ex.extra_info = 'kwarg "'+key+'" validator raised exception to value: "'+str(value)+'"'
                raise
            if not valid:
                import inspect
                v = inspect.getsource(vkwargs[key]['Validator']).strip()
                raise TypeError('kwarg "'+key+'" validator returned False for value: "'+str(value)+'"\n    '+v)


        config[key] = value

    return config