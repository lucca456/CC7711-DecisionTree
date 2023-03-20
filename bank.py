import pandas as pd
import numpy as np
from sklearn import tree, metrics
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from scipy.io import arff

def bank():
    data,meta = arff.loadarff('./bank.arff')

    attributes = meta.names()
    data_value = np.asarray(data)

    age = np.asarray(data['age']).reshape(-1,1)
    job = np.asarray(data['job']).reshape(-1,1)
    marital = np.asarray(data['marital']).reshape(-1,1)
    education = np.asarray(data['education']).reshape(-1,1)
    default = np.asarray(data['default']).reshape(-1,1)
    housing = np.asarray(data['housing']).reshape(-1,1)
    loan = np.asarray(data['loan']).reshape(-1,1)
    contact = np.asarray(data['contact']).reshape(-1,1)
    day = np.asarray(data['day']).reshape(-1,1)
    month = np.asarray(data['month']).reshape(-1,1)
    duration = np.asarray(data['duration']).reshape(-1,1)
    campaign = np.asarray(data['campaign']).reshape(-1,1)
    pdays = np.asarray(data['pdays']).reshape(-1,1)
    previous = np.asarray(data['previous']).reshape(-1,1)
    poutcome = np.asarray(data['poutcome']).reshape(-1,1)

    features = np.concatenate((age, loan, marital, education, default, housing, contact, day, month, duration, campaign, pdays, previous, poutcome), axis=1)
    target = data['subscribed']
    Arvore = DecisionTreeClassifier(criterion='entropy').fit(features, target)

    plt.figure(figsize=(10, 6.5))

    tree.plot_tree(Arvore,feature_names=['age','loan','marital','education','default','housing','contact', 'day', 'month', 'duration','campaign','pdays','previous', 'poutcome'],class_names=['yes', 'no'],
                   filled=True, rounded=True)
    plt.show()

    fig, ax = plt.subplots(figsize=(25, 10))
    metrics.plot_confusion_matrix(Arvore,features,target,display_labels=['yes', 'no'], values_format='d', ax=ax)
    plt.show()



bank()
