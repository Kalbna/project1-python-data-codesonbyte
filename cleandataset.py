import pandas as pd
import numpy as np
import random
import string

# Read the CSV file into a DataFrame
df = pd.read_csv("dataset_netflix1.csv")

# Replace "Not Given" values with random alphabet letters
for col in df.columns:
    if df[col].dtype == object and (df[col] == 'Not Given').any():
        df[col] = df[col].replace('Not Given', ''.join(random.choice(string.ascii_letters) for _ in range(1)))




# Identify the numerical columns
num_cols = df.select_dtypes(include=np.number).columns

# Calculating the quantiles and the IQR result for each numerical column
q1 = df[num_cols].quantile(0.25)
q3 = df[num_cols].quantile(0.75)
iqr = q3 - q1

# Creating a boolean mask for values within the acceptable range for each numerical column
def is_within_range(x):
    q1_series = q1[x.name]
    q3_series = q3[x.name]
    iqr_series = iqr[x.name]
    return (x >= q1_series - 1.5 * iqr_series) & (x <= q3_series + 1.5 * iqr_series)

mask = df[num_cols].apply(is_within_range)
mask = mask.all(axis=1)

# Filtering the DataFrame based on the mask
df_filtered = df.loc[mask]

# Save the filtered DataFrame as a new CSV file
df_filtered.to_csv("filtered_datasetr.csv", sep=",", index=False)
print(df.head(10).to_string())