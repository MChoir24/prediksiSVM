import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix, precision_recall_fscore_support, accuracy_score


class Classification_svm:
    """docstring for Classification_svm."""

    def __init__(self, url):
        self.url = url
        self.data = pd.read_csv(self.url)
        self.X = self.data.drop('Class', axis=1)  # menghilangkan kelas pada data
        self.y = self.data['Class']  # menampung kolom Class ke variable y

    def classificationSVM(self, bagiUji=5, kernel='rbf'):
        # memisahkan data training dan data test yaitu data test 30% dari data asli
        self.bagi = len(self.X)//bagiUji
        bagi = self.bagi
        self.X_test = self.X[-bagi:]
        self.y_test = self.y[-bagi:]

        self.X_train = self.X[:-bagi]
        self.y_train = self.y[:-bagi]

        svclassifierRbf = SVC(kernel=kernel)
        svclassifierRbf.fit(self.X_train, self.y_train)

        self.y_pred2 = svclassifierRbf.predict(self.X_test)

        self.confusi = confusion_matrix(self.y_test, self.y_pred2)
        self.accuracy = classification_report(self.y_test, self.y_pred2)
        self.recall = precision_recall_fscore_support(self.y_test, self.y_pred2)
        self.accuracyScore = accuracy_score(self.y_test, self.y_pred2)

        # print(self.confusi)
        return self.accuracyScore*100

    def predictUji(self, urlTest, kernel='rbf'):
        self.dataTest = pd.read_csv(urlTest)

        svclassifierRbf = SVC(kernel=kernel)
        svclassifierRbf.fit(self.X, self.y)
        print(self.dataTest.values)
        self.y_pred2 = svclassifierRbf.predict(self.dataTest)
        return self.y_pred2


# svm = Classification_svm("dataSvm0.csv")
# svm.classificationSVM()
