from methods import Method
from utils.general import training_data_for_t
from sklearn import svm

"""
Support Vector Machine (SVM) prediction model / method
"""


class SVM(Method):
    def predict(self, t, x_data, y_data, look_back=-1):
        # -1 means look back at as much data as possible
        # get the training data slice up to the current time step t
        x_train, y_train = training_data_for_t(data=(x_data, y_data), t=t, look_back=look_back)

        model = svm.SVR(gamma='scale', kernel='linear', degree=2, coef0=1)
        model.fit(x_train, y_train)

        return model.predict([x_data.iloc[t]])

    def predict_next_n(self, t, n, x_data, y_data, look_back=-1):
        # -1 means look back at as much data as possible
        # get the training data slice up to the current time step t
        x_train, y_train = training_data_for_t(data=(x_data, y_data), t=t, look_back=look_back)

        model = svm.SVR(gamma='scale', kernel='linear', degree=2, coef0=1)
        model.fit(x_train, y_train)
        return model.predict(x_data[t: t + n])
