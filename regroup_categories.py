def regroup_categories(data,feature,threshold=0.005,new_category='other'):
  
  
  print('Initial categories: ',len(data[feature].value_counts()))

  for_index=pd.DataFrame({'percent':data[feature].value_counts()/data.shape[0]})
  to_replace=for_index[for_index['percent']<=threshold].index
  

  for i in to_replace:

    data.loc[data[data[feature]==i].index,feature]=new_category

  print('Final categories: ',len(data[feature].value_counts()))
