def checking_2cols(col1,col2,data):
    '''Check the % of records that 2 columns has in common without missing values'''
    
    op1=data[[col1]].notnull().squeeze()
    op2=data[[col2]].notnull().squeeze()
    total=(op1==op2)
    result=round(total.sum()/data[[col1]].shape[0]*100)
    return print('Total % with common rows: ',result,'%')
