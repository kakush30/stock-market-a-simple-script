import pandas
import numpy as np
from sklearn.ensemble import ExtraTreesClassifier
from sklearn import linear_model
from sklearn import cross_validation
from sklearn.metrics import accuracy_score, precision_score, recall_score


def validation(df):
    dataset = pandas.read_csv(df)
    columns = ["days","Change","Change_Percentage","PROC","rci"]
    labels = dataset["Close"].values
    features = dataset[list(columns)].values
    

    clf = linear_model.LinearRegression(n_jobs=2)
   
    
    features_train, features_test, labels_train, labels_test =\
            cross_validation.train_test_split(features, labels, test_size = 0.3)
   
    clf.fit(features_train, labels_train)
    predictions = clf.predict(features_test)
    print len(labels_test)
    print len(predictions)
    
    print numpy.mean((abs(predictions - labels_test))/(abs(labels_test))*100)
      

 

    
if __name__ == '__main__':
    
       
    print validation('data.csv')
   
