import pandas as pd

# Replace 'your_dataset.csv' with the actual path to your dataset file.

df = pd.read_csv('your_dataset.csv')

# Identify duplicate rows

duplicate_rows = df.duplicated()

# Select and display duplicate rows

duplicate_data = df[duplicate_rows]

print(duplicate_data)

# Remove duplicate rows

df_cleaned = df.drop_duplicates()

# Save the cleaned dataset to a new CSV file

df_cleaned.to_csv('cleaned_dataset.csv', index=False)
