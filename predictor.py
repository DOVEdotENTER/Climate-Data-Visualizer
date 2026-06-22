from sklearn.linear_model import LinearRegression
import pandas as pd


def predict(dataset, future_year):

    data = dataset.get_data()

    X = data[["Year"]]

    y = data.iloc[:, 1]


    model = LinearRegression()

    model.fit(X, y)


    future = pd.DataFrame(
        {"Year": [future_year]}
    )


    prediction = model.predict(future)

    return prediction[0]