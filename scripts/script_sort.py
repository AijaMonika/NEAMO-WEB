import pandas as pd

# Load the data file
input_file = 'norway_coordinates1.csv'  # Replace with the path to your file
print("Reading data from file...")
data = pd.read_csv(input_file)
print(f"Total rows read: {len(data)}")

# Define Norway's approximate latitude and longitude range
norway_lat_range = (57, 71)
norway_lon_range = (4, 31)

# Filter data for coordinates within Norway's coastline range and with non-null pH values
norway_coordinates = data[
    (data['latitude'] >= norway_lat_range[0]) & (data['latitude'] <= norway_lat_range[1]) &
    (data['longitude'] >= norway_lon_range[0]) & (data['longitude'] <= norway_lon_range[1]) &
    (data['ph'].notnull()) & 
    (data['depth'] == 0.5)
]

# Save the filtered data to a new CSV file
output_file = 'norway_coordinates2.csv'
norway_coordinates.to_csv(output_file, index=False)

print(f"Filtered data with {len(norway_coordinates)} points saved to '{output_file}'.")
