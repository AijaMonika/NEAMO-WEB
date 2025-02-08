import xarray as xr
import pandas as pd
import os

# Get the base directory (script location)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define the raw data folder path
RAW_DATA_DIR = os.path.join(BASE_DIR, '..', 'raw_data')

# Define the output folder (optional, if you want to store results separately)
OUTPUT_DIR = os.path.join(BASE_DIR, '..', 'output')

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load NetCDF file dynamically
nc_file = os.path.join(RAW_DATA_DIR, 'NEMO_ERSEM_biogeochemical-monthly-all-rcp45-ph-2025-02-v1.1.nc')

if not os.path.exists(nc_file):
    raise FileNotFoundError(f"NetCDF file not found: {nc_file}")

dataset = xr.open_dataset(nc_file)

# Extract latitude, longitude, and pH data
df = dataset.to_dataframe().reset_index()

# Save to CSV in the output folder
csv_output_path = os.path.join(OUTPUT_DIR, 'ph_data_by_coordinates1.csv')
df.to_csv(csv_output_path, index=False)

print(f"CSV file created: {csv_output_path}")
