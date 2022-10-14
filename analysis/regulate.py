import pandas as pd
import os
import numpy as np
import xarray as xr

def txt2df(filename):
    df = pd.read_csv(f"{filename}", header=0, low_memory=False)
    # df.to_xarray().to_netcdf(f"{filename[:-4]}.nc")
    # nc_loc = []
    # nc_loc += filename[:-4] + ".nc"
    # return nc_loc
    return df

date_lst = ["Sep18", "Sep21"]
data_lst = ["FACTDATA", "DTagy", "DTocc", "DTsuper"]
# df_lst = [""]
#Get supervisory status; SUPERVIS: (2,6,7), (4,5,8,*)
# super = pd.read_csv("/Users/vcy/Dropbox/1 Work/Data bank/Fedscope/2018 Sept/DTsuper.txt",header=0, low_memory=False)
df_lst = dict()
for date in date_lst:
    for filename in data_lst:
        location = f"5_BayesCalib/experiment/regulatory_function/data/{date}/" + f"{filename}.txt"
        print(location)
        df_lst[f"{filename}_{date}"] = pd.read_csv(location, header=0, low_memory=False)
        df_lst[f"agency_supervis_{date}"].groupby("AGY").EMPLOYMENT.count()
        # merge agency then isSup as the later is for
        df_lst[f"agency_supervis_{date}"].groupby("AGY")[['EMPLOYMENT', 'LOC']].agg(["count", "sum"])

# # count the numer of SUPERTYP (2,6,7) FACTDATA with agency level
# df_lst["Sep18"] = df_lst["FACTDATA_Sep18"].merge(df_lst["FACTDATA_Sep18"], on = "AGYSUB")
#
# # aggregate FACTDATA with agency level
# df_lst["FACTDATA_Sep18"].groupby("AGYSUB").supervistype
#
# SUPERVIS == 2,6,7 or SUPERVIS == 4,5,8,*
df["isSup"] = df[df["SUPVIS"].isin('2', '6', '7')]
df.groupby("AGY"), "isSUP"))
df_lst[f"FACTDATA_{date}"].groupby("AGY")["EMPLOYMENT"].count()
for date in date_lst:
    location = f"5_BayesCalib/experiment/regulatory_function/data/{date}/" + f"{filename}.txt"
    df_lst[f"{filename}_{date}"] = pd.read_csv(location, header=0, low_memory=False)
    #df_lst[f"agency_supervis_{date}"] = pd.merge(df_lst[f"FACTDATA_{date}"], df_lst[f"DTagy_{date}"][["AGYSUB", "AGY"]], on = "AGYSUB", how = "left")
    df = df_lst[f"FACTDATA_{date}"]
    df_super = df[df["SUPERVIS"].isin('2', '6', '7')]
    df_sub = df[~df["SUPERVIS"].isin('2', '6', '7')]
    df_super.to_pickle(f"data/super_{date}")
    df_sub.to_pickle(f"data/sub_{date}")
    df_super = pd.read_pickle(f"data/super_{date}.pkl")
    df_sub = pd.read_pickle(f"data/sub_{date}.pkl")

    print(df_super.groupby("AGY")["EMPLOYMENT"].count())
    print(df_sub.groupby("AGY")["EMPLOYMENT"].count())
for date in date_lst:
    df_18 = df_lst[f"FACTDATA_Sep18"]

df_18 = df_lst[f"FACTDATA_Sep18"]
df_21 = df_lst[f"FACTDATA_Sep21"]
df18_sup = df_18[df_18["SUPERVIS"].isin(('2', '6', '7'))] # 291271
df21_sup = df_21[df_21["SUPERVIS"].isin(('2', '6', '7'))] #295234
df18_sub = df_18[~df_18["SUPERVIS"].isin(('2', '6', '7'))] #1809531
df21_sub = df_21[~df_21["SUPERVIS"].isin(('2', '6', '7'))] #1885872

df18_sup.merge(df_lst["DTagy_Sep18"]), groupby("AGYSUB")
sup_sub_ratio_18 = df18_sub.shape[0]/ df18_sup.shape[0] #6.21
sup_sub_ratio_18 = df18_sub.shape[0]/ df18_sup.shape[0] #6.21
sup_sub_ratio_21 = df21_sub.shape[0]/ df21_sup.shape[0] #6.39

# test

# merge
#Get supervisory status; SUPERVIS: (2,6,7), (4,5,8,*)
# superv = pd.read_csv("/Users/vcy/Dropbox/1 Work/Data bank/Fedscope/2018 Sept/DTsuper.txt",header=0, low_memory=False)
# for date in date_lst:
#     df_lst[""]
# df.groupby("agency").agg()
# print(ds_sup)
# print(ds_sup.sel(SUPERTYP = 1))

# # Agency data frame
# agy = pd.read_csv("../data/Sep18/DTagy.txt", header=0, low_memory=False)
# occ = pd.read_csv("../data/Sep18/DTocc.txt",header=0, low_memory=False)
# prior_pred.draws_xr(obs_stock_lst).to_netcdf("data/mngInvenPriorPredData_gp.nc")
# dfMain.to_xarray().to_netcdf("../data/main.nc")
# print(xr.open_dataset("../data/main.nc"))
# dfMain.to_xarray().to_netcdf("../data/main.nc")

#superv = pd.read_csv("../data/Sep18/DTsuper.txt",header=0, low_memory=False)
# superv = xr.read_csv("../data/Sep18/DTsuper.txt",header=0, low_memory=False)
# print(superv.to_xarray())
## label
# times = pd.date_range("2000-01-01", "2001-12-31", name="time")
# annual_cycle = np.sin(2 * np.pi * (times.dayofyear.values / 365.25 - 0.28))

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
#
# dfMain = pd.read_csv("../data/Sep18/FACTDATA_SEP2018.TXT", header=0, low_memory=False)
# print(dfMain.to_xarray())
#
# ## multiple dataset into one
# # ds_all = xr.open_mfdataset('../data/Sep18/*nc', combine='by_coords')
# # ds_all
#
# ds_sup = pd.read_csv("../data/Sep18/DTagy.txt")
# print(ds_sup.describe())
# print(ds_sup.columns)
# print(ds_sup.head())
