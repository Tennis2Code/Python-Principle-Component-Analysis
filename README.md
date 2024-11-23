# Housing Market PCA (2020-2024)

This project performs Principal Component Analysis (PCA) on housing market data from the years 2020 through 2024. The dataset includes various housing metrics, such as prices, market trends, and regional data, and the goal is to reduce the dimensionality of the data to gain insights into the underlying structure and variations in the housing market.

## Project Overview

The dataset used in this project contains housing data from the United States, focusing on market trends over a 5-year period. PCA is applied to this data to reduce its complexity and identify the most significant factors driving the housing market's evolution during this period.

### Steps:
1. **Data Loading and Preprocessing**:
   - The data is loaded from a CSV file containing monthly housing prices and market data.
   - Missing values are removed, and only relevant numeric columns are retained for PCA.

2. **Standardization**:
   - The data is standardized using `StandardScaler` to ensure each feature has a mean of 0 and a standard deviation of 1. This step is crucial before performing PCA.

3. **PCA Transformation**:
   - PCA is applied to reduce the data to 2 principal components, simplifying the dataset while retaining as much variability as possible.

4. **Data Visualization**:
   - A scatter plot is generated to visualize the first two principal components, with points colored to indicate the magnitude of each component.

## Visualizations

The scatter plot represents the housing market data, with each point corresponding to a year between 2020 and 2024. The first and second principal components are plotted to show how the data varies over time and identify key trends in the housing market.

## PCA Scatterplot

Below is the PCA scatterplot showing the first two principal components of the housing market data:

![PCA Scatterplot](scatterplot.png)
### Key Insights:
- The PCA transformation helps in identifying patterns and trends in the data that might not be apparent in the raw dataset.
- By focusing on the first two principal components, we can observe the most significant variations in the housing market during the 2020-2024 period.

## Requirements

- Python 3.x
- pandas
- numpy
- matplotlib
- scikit-learn

