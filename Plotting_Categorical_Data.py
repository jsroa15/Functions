def plotting_categorical(data,rows,cols,hue,x_list,size):
  '''Plot categorical data in subplots using Seaborn

  Parameters
  --------------
    data:Data frame with data
    rows:Number of rows in subplot
    cols:Number of columns in subplot
    hue:Feature to distinguish in the plot
    x_list:List with features names
    size:Tupple with size of plot
    
  '''
  pos=0
  f, axes = plt.subplots(nrows=rows, ncols=cols,figsize=size)
  for i in range(0,rows):
    for j in range(0,cols):
      
      sns.countplot(ax=axes[i,j],x=x_list[pos],hue=hue,data=data)
      pos+=1

  return(plt.show())
