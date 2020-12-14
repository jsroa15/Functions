def plotting_numericalVsTarget(data,rows,cols,x_list,size,target):
  '''Plot numerical data with categorical variables in subplots using Seaborn

  Parameters
  --------------
    data:Data frame with data
    rows:Number of rows in subplot
    cols:Number of columns in subplot
    x_list:List with numerical features names
    size:Tupple with size of plot
    target: Categorical feature 
    
  '''
  plt.rcParams["axes.labelsize"] = 1
  sns.set(font_scale=1)
  pos=0
  f, axes = plt.subplots(nrows=rows, ncols=cols,figsize=size)
  for i in range(0,rows):
    for j in range(0,cols):
      
      sns.boxplot(data=data,ax=axes[i,j],y=x_list[pos],x=target)
      pos+=1

  return(plt.show())
