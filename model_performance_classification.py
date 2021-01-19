def model_performance_classification(model,Xtrain,Ytrain,Xtest,Ytest):

  '''
  The function calculates metrics as Confusion matrix, AUC, Accuracy, Precision, Recall, F1 Score

  **Note**: Before running the function it's necessary to intantiate a classification model

  Parameters
  ------------------------------

  model: Classification model created prior to apply function.
  Xtrain: Your X train dataset
  Ytrain: Your Y train dataset
  Xtest: Your X test dataset
  Ytest: Your Y test dataset

  '''

  #Fit the model

  model.fit(Xtrain,Ytrain)

  #Make predictions

  y_pred=model.predict(Xtest)
  y_pred_proba=model.predict_proba(Xtest)[:,1]

  #Printing Metrics

  print('\nConfusion Matrix')
  print(confusion_matrix(Ytest, y_pred))


  print('\nScores')
  print('------------------------')
  print('AUC:',np.round(roc_auc_score(Ytest,y_pred_proba)*100,2),'%')
  print('Accuracy:',np.round(accuracy_score(Ytest,y_pred)*100,2),'%')
  print('Precision:',np.round(precision_score(Ytest,y_pred)*100,2),'%')
  print('Recall:',np.round(recall_score(Ytest,y_pred)*100,2),'%')
  print('F1 score:',np.round(f1_score(Ytest,y_pred)*100,2))
