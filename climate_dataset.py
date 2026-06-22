import pandas as pd


class ClimateDataset:

    def __init__(self, filename, name):
        self.name = name
        self.data = pd.read_csv(filename)


    def show_data(self):
        print("\n")
        print(self.name)
        print(self.data.to_string(index=False))


    def statistics(self):

        value_column = self.data.columns[1]

        print("\nStatistics for", self.name)

        print(
            "Average:",
            round(self.data[value_column].mean(), 2)
        )

        print(
            "Maximum:",
            round(self.data[value_column].max(), 2)
        )

        print(
            "Minimum:",
            round(self.data[value_column].min(), 2)
        )


    def get_data(self):
        return self.data


    def search_year(self, year):

        result = self.data[
            self.data["Year"] == year
        ]

        return result