import matplotlib.pyplot as plt


def plot_dataset(dataset):

    data = dataset.get_data()

    plt.figure(figsize=(8,5))

    plt.plot(
        data["Year"],
        data.iloc[:,1],
        marker="o"
    )

    plt.title(dataset.name)

    plt.xlabel("Year")

    plt.ylabel(data.columns[1])

    plt.grid(True)

    plt.show()



def compare(dataset1, dataset2):

    plt.figure(figsize=(8,5))

    plt.plot(
        dataset1.get_data()["Year"],
        dataset1.get_data().iloc[:,1],
        marker="o",
        label=dataset1.name
    )


    plt.plot(
        dataset2.get_data()["Year"],
        dataset2.get_data().iloc[:,1],
        marker="o",
        label=dataset2.name
    )


    plt.legend()

    plt.grid(True)

    plt.show()