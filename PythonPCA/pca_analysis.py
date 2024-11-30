
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

# Apply PCA transformation (reduce to 2 components)
pca = PCA(n_components=2)
pca_result = pca.fit_transform(scaled_data)

# Create a 2-column, 1-row subplot grid
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Plot the first principal component on the first subplot
axes[0].scatter(pca_result[:, 0], np.zeros_like(pca_result[:, 0]), c='blue', alpha=0.6)
axes[0].set_title('First Principal Component')
axes[0].set_xlabel('First Principal Component')
axes[0].set_ylabel('Value')

# Plot the second principal component on the second subplot
axes[1].scatter(pca_result[:, 1], np.zeros_like(pca_result[:, 1]), c='yellow', alpha=0.6)
axes[1].set_title('Second Principal Component')
axes[1].set_xlabel('Second Principal Component')
axes[1].set_ylabel('Value')

# Save the plot
plt.tight_layout()
plt.savefig("/Users/lindytatum/Python/PythonPCA/pca_housing_plot.png", dpi=300, bbox_inches='tight')
plt.show()
