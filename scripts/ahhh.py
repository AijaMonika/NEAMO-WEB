import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd
from pykrige.ok import OrdinaryKriging
from scipy.interpolate import griddata
 
# Sample Data (Replace with actual latitude, longitude, and pH values)
# Latitude, Longitude, and pH levels at each point
data = np.array([
    [56.9496, 24.1052, 7.2],  # Riga
    [57.0000, 24.2000, 6.5],
    [56.8500, 24.0000, 7.8],
    [56.9500, 23.9000, 6.9],
    [57.1000, 24.1500, 7.1],
    [56.8000, 24.3000, 6.7]
])
 
lats, longs, ph_values = data[:, 0], data[:, 1], data[:, 2]
 
# Define grid (higher resolution for a smoother image)
grid_x, grid_y = np.meshgrid(
    np.linspace(min(longs), max(longs), 200),  # Longitude range
    np.linspace(min(lats), max(lats), 200)    # Latitude range
)
 
# ---- Kriging Interpolation ----
krig = OrdinaryKriging(longs, lats, ph_values, variogram_model='linear', verbose=False)
grid_z, _ = krig.execute('grid', grid_x[0], grid_y[:, 0])
 
# ---- Plot the Interpolated Map ----
fig, ax = plt.subplots(figsize=(10, 6))
 
# Plot interpolated data
c = ax.contourf(grid_x, grid_y, grid_z, levels=100, cmap='viridis')  # Change cmap for different colors
 
# Scatter original points
ax.scatter(longs, lats, c=ph_values, cmap='viridis', edgecolors='k', s=100, label="Sample Points")
 
# Add colorbar
cbar = plt.colorbar(c, ax=ax)
cbar.set_label("pH Level")
 
# Labels and title
ax.set_title("Interpolated pH Levels (Kriging)")
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
 
plt.legend()
plt.show()