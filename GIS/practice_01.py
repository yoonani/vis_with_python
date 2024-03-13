import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd

pth = gpd.datasets.get_path("naturalearth_lowres")
world = gpd.GeoDataFrame.from_file( pth )

ax = world.plot( figsize=(10, 10) )
ax.set_axis_off()
plt.show()