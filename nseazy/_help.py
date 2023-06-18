import pandas as pd
import textwrap
import nseazy as nz

def df_wrapcols(df,wrap_columns=None):

    if wrap_columns is None: return df
    if not isinstance(wrap_columns,dict):
        raise TypeError('wrap_columns must be a dict of column_names and wrap_lengths')

    for col in wrap_columns:
        if col not in df.columns:
            raise ValueError('column "'+str(col)+'" not found in df.columns')

    index = []
    column_data = {}
    for col in df.columns:
        column_data[col] = []
  
    for ix in df.index:
        row = df.loc[ix,]
        
        row_data = {}
        for col in row.index:
            cstr = str(row[col])
            if col in wrap_columns:
                wlen = wrap_columns[col]
                tw   = textwrap.wrap(cstr,wlen) if not cstr.isspace() else [' ']
            else:
                tw = [cstr]
            row_data[col] = tw

        cmax = max(row_data,key=lambda k: len(row_data[k]))
        rlen = len(row_data[cmax])
        for r in range(rlen):
            for col in row.index:
                extension = [' ']*(rlen - len(row_data[col]))
                row_data[col].extend(extension)
                column_data[col].append(row_data[col][r])
            ixstr = str(ix)+'.'+str(r) if r > 0 else str(ix)
            index.append(ixstr)

    return pd.DataFrame(column_data,index=index)

def make_left_formatter(maxwidth):
    wm3 = maxwidth-3
    w   = maxwidth
    def left_formatter(value):
        if not isinstance(value,str):
            return f'{value:<}'
        elif value[0:maxwidth] == '-'*maxwidth:
            return f'{value:<{w}.{w}s}'
        elif len(value) > maxwidth:
            return f'{value:<{wm3}.{wm3}s}...'
        else:
            return f'{value:<{w}.{w}s}'
    return left_formatter

def help( func_name=None, kwarg_names=None, sort=False ):

    func_kwarg_map = {
        'show_data'         : nz.fetch._get_quote_parameter,
        }
    func_kwarg_aliases = {
        'addplot'           : nz.fetch._get_quote_parameter,
        }
    
    
    if func_name is None:
        print('\nUsage: `kwarg_help(func_name)` or `kwarg_help(func_name,kwarg_names)`')
        print('        kwarg_help is available for the following func_names:')
        s = str(list(func_kwarg_map.keys()))
        text = textwrap.wrap(s,68)
        for t in text:
            print('           ',t)
        print()
        return

    fkmap = {**func_kwarg_map, **func_kwarg_aliases}
           
    if func_name not in fkmap:
        raise ValueError('Function name "'+func_name+'" NOT a valid function name')

    if kwarg_names is not None and isinstance(kwarg_names,str):
        kwarg_names = [ kwarg_names, ]

    if ( kwarg_names is not None 
         and (not isinstance(kwarg_names,(list,tuple)) 
              or not all([isinstance(k,str) for k in kwarg_names])
             ) 
       ):
        raise ValueError('kwarg_names must be a sequence (list,tuple) of strings')

    vks = fkmap[func_name]()

    df = (pd.DataFrame(vks).T).drop('Validator',axis=1)
    df.index.name = 'Kwarg'
    if sort: df.sort_index(inplace=True)
    df.reset_index(inplace=True)

    if kwarg_names is not None:
        for k in kwarg_names:
            if k not in df['Kwarg'].values:
                print('   Warning: "'+k+'" is not a valid `kwarg_name` for `func_name` "'+func_name,'"')
        df = df[ df['Kwarg'].isin(kwarg_names) ]
        if len(df) < 1:
            raise ValueError(' None of specified `kwarg_names` are valid for `func_name` "'+func_name,'"')

    df['Default'] = ["'"+d+"'" if isinstance(d,str) else str(d) for d in df['Default']]
        
    klen = df['Kwarg'].str.len().max()+1
    dlen = df['Default'].str.len().max()+1

    wraplen = max( 40, 80-(klen+dlen) )
    df = df_wrapcols(df,wrap_columns={'Description':wraplen})

    dividers = []
    for col in df.columns:
        dividers.append('-'*int(df[col].str.len().max()))
    dfd = pd.DataFrame(dividers).T
    dfd.columns = df.columns
    dfd.index = pd.Index(['---'])

    df = pd.concat([dfd,df])

    formatters = { 'Kwarg'       : make_left_formatter( klen ),
                   'Default'     : make_left_formatter( dlen ),
                   'Description' : make_left_formatter( wraplen ),
                 }
    
    print('\n ','-'*78)
    print('  Following Parameter Can Be Used at "'+func_name+'":')

    s = df.to_string(formatters=formatters,index=False,justify='left')

    print('\n ',s.replace('\n','\n  '))