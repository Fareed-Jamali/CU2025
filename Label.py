import pandas as pd

# Replace with the path to your CSV file
csv_path = 'output1.csv'

# Load the CSV
df = pd.read_csv(csv_path)

# Add the new column with value 0
df['Device Type'] = 0

# Save the updated CSV (overwrite or use a new file name)
df.to_csv(csv_path, index=False)

print(f" 'Device Type' column added with value 0 to {csv_path}")
