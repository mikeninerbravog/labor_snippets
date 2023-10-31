import csv
import json
import pandas as pd

# Convert CSV to JSON

data = pd.read_csv("driver_data.csv")
print(data)

print("Converted JSON fiel below :")
print(json.dumps(list(csv.reader(open('driver_data.csv')))))