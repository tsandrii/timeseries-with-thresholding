from abc import ABC, abstractmethod


class Method(ABC):
    """
    Predict the price at time step t using a range of values ending at t-1
    to make the prediction
    """
    @abstractmethod
    def predict(self, t, x_data, y_data, look_back=-1):
        pass

    """
    Given a current step t, data, and a length of data to "look back"
    on (memory for training), predict the next N prices at steps [t+1, t+1+N]
    """
    @abstractmethod
    def predict_next_n(self, t, n, x_data, y_data, look_back=-1):
        pass
