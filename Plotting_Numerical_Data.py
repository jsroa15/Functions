def plotting_numerical(data,rows,cols,x_list,size):
  '''Plot numerical data in subplots using Seaborn

  Parameters
  --------------
    data:Data frame with data
    rows:Number of rows in subplot
    cols:Number of columns in subplot
    x_list:List with features names
    size:Tupple with size of plot
    
  '''
  sns.set_style("whitegrid")

  pos=0
  f, axes = plt.subplots(nrows=rows, ncols=cols,figsize=size)
  for i in range(0,rows):
    for j in range(0,cols):
      
      sns.kdeplot(data=data,ax=axes[i,j],x=x_list[pos])
      pos+=1

  return(plt.show())
