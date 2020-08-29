import pandas as pd
import csv


class Dataset:

    def __init__(self, csv_file):
        self.csv_file = csv_file

    def len(self):
        """
        Get number of examples
        @return: int
        """
        with open(self.csv_file, 'rt') as f:
            return sum(1 for row in f) - 1

    def columns(self):
        """
        Get list of columns names
        @return: list
        """
        with open(self.csv_file, 'rt') as f:
            columns = f.readline().rstrip().split(',')
        # Удаление столбца с target
        del columns[9]
        return columns

    def getitem(self, index):
        """
        Get example by index
        @param index: int
        @return: list, int
        """
        'Generates one sample of data'
        # Select sample
        # Выборка указанной строки из датасета
        # +1 т.к. нулевая строка - это шапка
        idx = index + 1
        # Load data and get label
        with open(self.csv_file, 'rt') as f:
            reader = csv.reader(f)
            count = 0
            for line in reader:
                if idx == count:
                    break
                count = count + 1

        # отделение столбца с target
        y = int(line[9])
        del line[9]
        x = line
        return x, y

    def get_items(self, items_number):
        """
        Get specific amount of examples
        @param items_number:
        @return: pd.DataFrame, pd.Series
        """
        data = pd.read_csv(self.csv_file, nrows=items_number)
        y = data['AdoptionSpeed']
        x = data.drop(['AdoptionSpeed'], axis=1)
        return x, y
