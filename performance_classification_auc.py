def performance_classification_auc(model_dictionary,Xtrain,ytrain,Xtest,ytest,folds=5):
  '''
  The function evaluates the performance of classification models via CV. The base metric is ROC AUC score

  Parameters
  ------------
    model_dictionary: A dictionary that contains as key the instantiate model and as value the model name
    Xtrain: The X train dataset
    ytrain: The y train dataset
    Xtest: The X test dataset
    ytest: The y test dataset
    folds: Number of folds to cross-validate. Default 5

  '''
  null_list1=[]
  null_list2=[]

  for key,value in model_dictionary.items():
    metric=cross_val_score(key,Xtrain,ytrain,cv=folds,scoring='roc_auc')
    
    #Store the F1 score from CV
    metric_mean=round(metric.mean()*100,2)


    #Fit and predict
    key.fit(Xtrain,ytrain)
    y_pred=key.predict_proba(Xtest)[:,1]

    #Calculate the ROC AUC Score in Test
    metric_test=round(roc_auc_score(y_test,y_pred)*100,2)
    null_list1.append(metric_mean)
    null_list2.append(metric_test)

  index=[x for x in model_dictionary.values()]
  dff=pd.DataFrame([null_list1,null_list2],index=['ROC AUC Cross Val','ROC AUC Test set']).transpose()
  dff.index=index
  print(dff)
