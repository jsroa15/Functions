def performance(model_dictionary,X_for_training,y_for_training,X_for_test,y_for_test):

  null_list1=[]
  null_list2=[]

  for key,value in model_dictionary.items():
    cv_mse=-cross_val_score(key,X_for_training,y_for_training.values.ravel(),cv=10,scoring='neg_mean_squared_error')
    #Calculate root mse in CV
    rmse_cv=np.round((cv_mse.mean())**(1/2),2)

    key.fit(X_for_training,y_for_training.values.ravel())
    y_pred=key.predict(X_for_test)

    #Calculate root mse in Test
    rmse_test=np.round(MSE(y_for_test,y_pred)**(1/2),2)
    null_list1.append(rmse_cv)
    null_list2.append(rmse_test)

  index=[x for x in model_dictionary.values()]
  dff=pd.DataFrame([null_list1,null_list2],index=['Root MSE-CV','Root MSE-Test Set']).transpose()
  dff.index=index
  print(dff)
 
 
  
   
