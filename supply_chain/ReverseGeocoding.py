%load_ext autotime
import pandas as pd

import geopandas as gpd
import geopy
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

import matplotlib.pyplot as plt
import plotly_express as px
import tqdm
from tqdm import tqdm
from tqdm._tqdm_notebook import tqdm_notebook

locator = Nominatim(user_agent="myGeocoder")
coordinates = "53.480837, -2.244914"
location = locator.reverse(coordinates)

url = "https://www.dropbox.com/s/15gisj8hx218rn1/street-pole-sample.csv?dl=1"
cols = ["X", "Y", "POLE_NUM","TYPE","HEIGHT","POLE_DATE","OWNER"]
df = pd.read_csv(url, usecols=cols)
df.head()
import plotly_express as px
px.set_mapbox_access_token("pk.eyJ1Ijoic2hha2Fzb20iLCJhIjoiY2plMWg1NGFpMXZ5NjJxbjhlM2ttN3AwbiJ9.RtGYHmreKiyBfHuElgYq_w")
px.scatter_mapbox(df, lat="Y", lon="X",  zoom=15)
locator = Nominatim(user_agent="myGeocoder", timeout=10)
rgeocode = RateLimiter(locator.reverse, min_delay_seconds=0.001)
