import pandas as pd
import os
import numpy as np
import xarray as xr

dfMain = pd.read_csv("../data/Sep18/FACTDATA_SEP2018.TXT", header=0, low_memory=False)
print(dfMain.to_xarray())

# # Agency data frame
# agy = pd.read_csv("../data/Sep18/DTagy.txt", header=0, low_memory=False)
# occ = pd.read_csv("../data/Sep18/DTocc.txt",header=0, low_memory=False)
#prior_pred.draws_xr(obs_stock_lst).to_netcdf("data/mngInvenPriorPredData_gp.nc")
#dfMain.to_xarray().to_netcdf("../data/main.nc")
# print(xr.open_dataset("../data/main.nc"))
# dfMain.to_xarray().to_netcdf("../data/main.nc")
# Xarray is multi-dim labeled array which would allow temporal and cross-sectional comparison
# It use `coordinates` and `data variables`; the latter is equivalent to pandas' column name
# arviz (Bayes computation visualization library) used netCDF data structure as it need
# labels (posterior, prior, prior predictive, loglik) for each of the parameters each of which has 1,000 samples

## label
times = pd.date_range("2000-01-01", "2001-12-31", name="time")
annual_cycle = np.sin(2 * np.pi * (times.dayofyear.values / 365.25 - 0.28))

## multidimension
# base = 10 + 15 * annual_cycle.reshape(-1, 1)
# tmin_values = base + 3 * np.random.randn(annual_cycle.size, 3)
# tmax_values = base + 10 + 3 * np.random.randn(annual_cycle.size, 3)
#
# ds = xr.Dataset(
#     {
#         "tmin": (("time", "location"), tmin_values),
#         "tmax": (("time", "location"), tmax_values),
#     },
#     {"time": times, "location": ["IA", "IN", "IL"]},
# )
#
# print(ds)

