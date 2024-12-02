
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Load the CSV data into a DataFrame
df = pd.read_csv("/Users/lindytatum/Python/PythonPCA/sortHousingResults.csv")

# Check the columns to ensure they contain the date range (2020-2024)
print(df.columns)

# Filter columns to include only those between 2020 and 2024

date_columns = [col for col in df.columns if col.startswith(('2020', '2021', '2022', '2023', '2024'))]

# Extract only the date columns
df_filtered = df[date_columns]

# Drop rows with missing values (if any)
df_cleaned = df_filtered.dropna()

# Standardize the data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df_cleaned)

# Apply PCA transformation (reduce to 2 components)
pca = PCA(n_components=2)
pca_result = pca.fit_transform(scaled_data)

# Create a 2-column, 1-row subplot grid
# fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# plot dates
years = df_cleaned.columns
plt.figure(figsize=(12, 6))
plt.scatter(pca_result[:, 0], pca_result[:, 1], c='blue', alpha=0.6)
for i, year in enumerate(years):
    plt.annotate(year, (pca_result[i, 0], pca_result[i, 1]), fontsize=9)
plt.title("PCA of Housing Market Trends (2020-2024)")
plt.xlabel("First Principal Component")
plt.ylabel("Second Principal Component")
plt.grid()
plt.show()

# Customize layout and save the plot
plt.tight_layout()
 #Save the plot as an image file
plt.savefig("/Users/lindytatum/Python/PythonPCA/pca_housing_plot.png", dpi=300, bbox_inches='tight')
#plt.show()

