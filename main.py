from climate_dataset import ClimateDataset
from visualizer import plot_dataset, compare
from predictor import predict
from report import save_report


temperature = ClimateDataset(
    "temperature.csv",
    "Global Temperature"
)


co2 = ClimateDataset(
    "co2.csv",
    "CO2 Levels"
)


sea = ClimateDataset(
    "sea_level.csv",
    "Sea Level Rise"
)


datasets = [
    temperature,
    co2,
    sea
]


while True:

    print("\n===== Climate Dashboard =====")

    print("1. View Temperature")
    print("2. View CO2")
    print("3. View Sea Level")
    print("4. Statistics")
    print("5. Graph")
    print("6. Compare Temperature and CO2")
    print("7. Predict Future Temperature")
    print("8. Save Report")
    print("9. Exit")


    choice=input("Choice: ")


    if choice=="1":
        temperature.show_data()


    elif choice=="2":
        co2.show_data()


    elif choice=="3":
        sea.show_data()


    elif choice=="4":

        for d in datasets:
            d.statistics()



    elif choice=="5":

        plot_dataset(temperature)



    elif choice=="6":

        compare(
            temperature,
            co2
        )


    elif choice=="7":

        year=int(
            input(
            "Future year: "
            )
        )


        result=predict(
            temperature,
            year
        )


        print(
        "Prediction:",
        round(result,2)
        )


    elif choice=="8":

        save_report(
            temperature
        )


    elif choice=="9":

        break


    else:

        print(
        "Invalid option"
        )