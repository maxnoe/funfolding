import numpy as np

from ._solution import Solution, LLHSolutionMinimizer
from sklearn.naive_bayes import GaussianNB


class DSEAGaussianNB(Solution):
    name = 'GaussianNBDsea'

    def __init__(self):
        super(DSEAGaussianNB, self).__init__()
        self.trained_model = None

    def initialize(self, X_A, y_A, sample_weight=None, priors=None):
        super(DSEAGaussianNB, self).initialize()
        self.trained_model = GaussianNB(priors=priors)
        self.trained_model.fit(X_A,
                              y_A,
                              sample_weight=sample_weight)

    def fit(self, X_test, return_individual_confidences=False):
        confidences = self.trained_model.predict_proba(X_test)
        if return_individual_confidences:
            return confidences
        else:
            return np.sum(confidences, axis=0)
