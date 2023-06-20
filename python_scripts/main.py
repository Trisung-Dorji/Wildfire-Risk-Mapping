# Program for data Handling/

# importing potential libraries

import os
import rasterio
import fiona
from rasterio.mask import mask
from rasterio import plot as rplot
from shapely.geometry import shape
from shapely.geometry import Point, Polygon, LineString, MultiPolygon, mapping
import matplotlib.pyplot as plt
import geopandas as gpd
import json
import math
import numpy as np
import rasterio.mask

# Importing my own functions

from Fire_season import generate_UI
from Modis_handler import Modis_nc, deleter, clipper
from WF_poly import Poly_fire
from Utilities import year_lister

# Start of the program

print("Wild fire susceptibility mapping data cleaner version 1.0")

current_directory = os.path.dirname(os.getcwd())

print("\nProject directory: "
      "\n"
      + current_directory)


# first lets get the first and last years in our MODIS file.
# Get the folder names in the MODIS directory
MODIS_directory = current_directory + "\\Data\\Initial\\MODIS\\Reprojected"

first_year, last_year = year_lister(MODIS_directory)

# open the button window and retrieve the selected month codes for the fire season months.
window, selected_month_codes = generate_UI()
# Start the main event loop
window.mainloop()

print("\nPlease look for the window to select your fire season months.")


# Step 1: Rename the MODIS files to make it easier to understand.
print("\nRenaming MODIS files\n"
      "\n")
"""
for i in range(first_year, (last_year + 1)):
    Modis_nc(i, current_directory)

# Step 2: Select raster images of the months corresponding to the fire season in your study area.

print("\nSelecting MODIS files corresponding to your fire season months.\n"
      "\n")

for i in range(first_year, (last_year + 1)):
    deleter(i, selected_month_codes, current_directory)

# Step 3: Clip the raster images by your study area.
print("\nClipping your MODIS files\n"
      "\n")
"""

for i in range(first_year, (last_year + 1)):
    clipper(i, current_directory)

# Step 4: Polygonise the raster images.
for i in range(first_year, (last_year + 1)):
    Poly_fire(i, current_directory)