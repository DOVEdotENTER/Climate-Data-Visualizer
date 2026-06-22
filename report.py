def save_report(dataset):

    data = dataset.get_data()

    column = data.columns[1]


    with open(
        "climate_report.txt",
        "w"
    ) as file:


        file.write(
            dataset.name + "\n"
        )

        file.write("================\n")

        file.write(
            "Average: "
            +
            str(round(data[column].mean(),2))
        )


    print(
        "Report saved!"
    )