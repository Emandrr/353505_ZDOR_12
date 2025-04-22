import pandas as pd
from IPython.display import display


class MedicineAnalyzer:

    def __init__(self, data_path):
        self.df = pd.read_csv(data_path)

    def create_series_example(self):
        """
            Developer Pavel Zdor
            date: 20.04.2025
            print dataframes
            """
        print("\nПример работы с Series:")
        manufacturers = pd.Series(self.df['Manufacturer'], name='Manufacturers')
        display(manufacturers)

        print("\nПервые 5 производителей:")
        display(manufacturers.head())

        print("\nДоступ к элементам по индексу (iloc):")
        display(manufacturers.iloc[10:15])

        print("\nДоступ к элементам по метке (loc):")
        display(manufacturers.loc[10:15])


class MedicineStats(MedicineAnalyzer):

    def __init__(self, data_path):
        super().__init__(data_path)

    def get_manufacturer_stats(self):
        """
            Developer Pavel Zdor
            date: 20.04.2025
            get stats of manufacture
            """
        return self.df['Manufacturer'].value_counts()

    def get_review_stats(self):
        """
            Developer Pavel Zdor
            date: 20.04.2025
            get stats of review
            """
        self.df['Total_Review_%'] = (self.df['Excellent Review %'] +
                                     self.df['Average Review %'] -
                                     self.df['Poor Review %'])
        best_review = self.df.loc[self.df['Total_Review_%'].idxmax()]
        worst_review = self.df.loc[self.df['Total_Review_%'].idxmin()]

        return {
            'best': best_review[['Medicine Name', 'Total_Review_%']],
            'worst': worst_review[['Medicine Name', 'Total_Review_%']],
            'ratio': (-1)*best_review['Total_Review_%'] / worst_review['Total_Review_%']
        }

    def compare_side_effects(self):
        """
            Developer Pavel Zdor
            date: 20.04.2025
            compare side effects
            """
        self.df['Side_Effects_Count'] = self.df['Side_effects'].str.split().apply(len)

        max_side = self.df.loc[self.df['Side_Effects_Count'].idxmax()]
        min_side = self.df.loc[self.df['Side_Effects_Count'].idxmin()]

        ratio = max_side['Side_Effects_Count'] / min_side['Side_Effects_Count']

        return {
            'max_side': max_side[['Medicine Name', 'Side_Effects_Count']],
            'min_side': min_side[['Medicine Name', 'Side_Effects_Count']],
            'ratio': ratio
        }
