
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

# Create a scatter plot with custom coloring for the 1st and 2nd principal components
plt.figure(figsize=(8, 6))

# Plot first PC with blue color
plt.scatter(pca_result[:, 0], pca_result[:, 1], c='blue', label='First Principal Component', alpha=0.6)

# Plot second PC with yellow color
plt.scatter(pca_result[:, 0], pca_result[:, 1], c='yellow', label='Second Principal Component', alpha=0.6)

# Customize the plot
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')
plt.title('PCA: Housing Market Data (2020-2024)')

# Show the plot
# Save the plot as an image file
plt.savefig("/Users/lindytatum/Python/PythonPCA/pca_housing_plot.png", dpi=300, bbox_inches='tight')
plt.show()
