# Climate Data Visualizer 

A Python-based climate analytics application that analyzes environmental data, creates visualizations, calculates climate statistics, and predicts future temperature trends using machine learning.

This project demonstrates data processing, object-oriented programming, data visualization, and machine learning techniques to explore climate change patterns.



## Project Overview

Climate change is one of the most important environmental challenges today. This project provides a simple analytics dashboard that allows users to explore historical climate data and understand trends in temperature, carbon dioxide levels, and sea level rise.

The application loads climate datasets, performs statistical analysis, generates graphs, and uses a machine learning model to predict future temperature changes.



# Features

## Data Visualization

- Generate graphs showing climate trends over time
- Visualize temperature changes
- Visualize CO₂ concentration trends
- Visualize sea level rise
- Compare different climate variables



## Climate Statistics

The application calculates:

- Average values
- Maximum values
- Minimum values

for different climate datasets.



## Machine Learning Prediction

The project uses **Linear Regression** to predict future temperature values based on historical climate data.

Example:


Enter future year: 2050

Predicted Temperature: 16.8°C



## Report Generation

The application can generate a climate analysis report containing:

- Dataset information
- Average climate values
- Summary statistics



# Technologies Used

## Programming Language

- Python 3

## Libraries

### Pandas
Used for:
- Reading datasets
- Processing climate information
- Performing calculations

### Matplotlib
Used for:
- Creating climate graphs
- Data visualization

### Scikit-learn
Used for:
- Machine learning prediction
- Linear Regression model



# 📂 Project Structure


Climate-Data-Visualizer/

│
├── main.py
│ └── Main program menu and user interaction
│
├── climate_dataset.py
│ └── ClimateDataset class for managing datasets
│
├── visualizer.py
│ └── Graph creation and climate comparisons
│
├── predictor.py
│ └── Machine learning temperature prediction
│
├── report.py
│ └── Generates climate analysis reports
│
├── temperature.csv
│ └── Historical temperature data
│
├── co2.csv
│ └── Carbon dioxide concentration data
│
├── sea_level.csv
│ └── Sea level rise data
│
└── climate_data.csv
└── General climate dataset


---

# ▶️ How to Run the Project

## 1. Clone the Repository

```bash
git clone https://github.com/DOVEdotENTER/Climate-Data-Visualizer.git
2. Navigate to the Project Folder
cd Climate-Data-Visualizer
3. Install Required Libraries
pip install pandas matplotlib scikit-learn
4. Run the Application
python3 main.py
🖥 Application Menu

When the program runs, users can select:

===== Climate Dashboard =====

1. View Temperature
2. View CO2
3. View Sea Level
4. Statistics
5. Graph
6. Compare Temperature and CO2
7. Predict Future Temperature
8. Save Report
9. Exit
📊 Example Capabilities

The application can:

✅ Load climate datasets
✅ Analyze historical trends
✅ Generate climate graphs
✅ Compare environmental factors
✅ Predict future temperature changes
✅ Create reports from climate information
