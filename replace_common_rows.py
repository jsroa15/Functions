def replace_common_rows(col1,col2,data):
    
    '''Replace common values in rows for a pair of columns'''
    
    mask1=data[col1].isnull()
    data[col1].fillna(data.loc[mask1,[col2]].squeeze(),inplace=True)
    

    mask2=data[col2].isnull()
    data[col2].fillna(data.loc[mask2,[col1]].squeeze(),inplace=True)
