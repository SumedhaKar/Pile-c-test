from ecmwf.opendata import Client
import xarray as xr

client = Client(source="ecmwf", model="aifs-ens")
result = client.retrieve(time=0, stream="enfo", type="cf", step=120,
                         param="tp", target="latest.grib2")
print("Prediction started:", result.datetime)

data = xr.open_dataset("latest.grib2", engine="cfgrib")
india = data["tp"].sel(latitude=slice(38, 6), longitude=slice(68, 98))
print("India shape:", india.shape)
print("Highest value:", float(india.max()))
