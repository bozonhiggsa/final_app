import pandas as pd

from sklearn.preprocessing import LabelEncoder


class DataLoader(object):
    def fit(self, dataset):
        self.dataset = dataset.copy()

    def load_data(self):
        # binning with cut
        self.dataset['PhotoAmt'] = pd.cut(self.dataset['PhotoAmt'], 4)

        # binning with qcut
        self.dataset['Age'] = pd.qcut(self.dataset['Age'], 3)

        # encode labels
        le = LabelEncoder()

        le.fit(self.dataset['PhotoAmt'])
        self.dataset['PhotoAmt'] = le.transform(self.dataset['PhotoAmt'])

        le.fit(self.dataset['Age'])
        self.dataset['Age'] = le.transform(self.dataset['Age'])

        return self.dataset
