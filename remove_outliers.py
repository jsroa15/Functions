def remove_outliers(data,features):

  '''
  This function removes outliers.
  The function detects and deletes outliers based on Z-score.
  
  Note: Use this function only if the amount of data is quite big.
  
  Parameters:
  -------------------
  data: dataset to be analyzed
  features: List of numerical features in the dataset
  '''
  
  to_del=[]
  for i in features:
    mean=data[i].mean()
    stand=data[i].std()
    ind_upper=[]
    ind_lower=[]
    ind=[]
    data['Z_score']=(data[i]-mean)/stand
    print(data[(data['Z_score']>3) | (data['Z_score']<-3)].shape[0],' outliers detected for ',i)
    to_del.append(data[(data['Z_score']>3) | (data['Z_score']<-3)].shape[0])
    ind_upper=data[data['Z_score']>3].index
    ind_lower=data[data['Z_score']<-3].index
    ind=ind_upper.append(ind_lower)
    
    mean_to_replace=data[(data['Z_score']<3) & (data['Z_score']>-3)][i].mean()
    
    data.drop(ind,inplace=True)
  print('total outliers removed: ',sum(to_del))
  data.drop(columns='Z_score',inplace=True)
