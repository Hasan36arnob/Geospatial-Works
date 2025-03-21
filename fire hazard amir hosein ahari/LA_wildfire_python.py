

# import ee
# import geemap as gee
# import xarray as xr

# import xee

# ee.Authenticate()
# ee.Initialize(project = 'ee-arnobhasanice1232', opt_url='https://earthengine-highvolume.googleapis.com')

# map = gee.Map(basemap = 'TERRAIN')
# map

# roi = map.draw_last_feature.geometry()

# time_start = ee.Date('2025-01-01')
# time_end = ee.Date('2025-02-01')

# sr  = ee.ImageCollection("NASA/VIIRS/002/VNP09GA").filterDate(time_start, time_end).select('I1','I2')

# def ndvi(img):
#   index = img.normalizedDifference(['I2','I1']).rename('ndvi')
#   return index.copyProperties(img, img.propertyNames())

# viirs_ndvi = sr.map(ndvi)

# ds_ndvi  = xr.open_dataset(viirs_ndvi, engine = 'ee', crs = 'EPSG:4326', scale = 0.05, geometry = roi)

# ds_ndvi

# import matplotlib.pyplot as plt

# ds_ndvi.ndvi.plot(x = 'lon', y ='lat', col = 'time', col_wrap = 5, robust =True, cmap = 'jet')
# plt.savefig('ndvi_fire.png', dpi = 360, bbox_inches = 'tight')

# temp = ee.ImageCollection("NASA/VIIRS/002/VNP14A1").select('MaxFRP').filterDate(time_start, time_end)

# ds_temp = xr.open_dataset(temp, engine = 'ee', crs = 'EPSG:4326', scale = 0.5, geometry = roi)

# ds_temp

# ds_temp.MaxFRP.plot(x = 'lon', y = 'lat', cmap = 'Reds', col = 'time', col_wrap = 5, robust = True)

# lst = ee.ImageCollection("NASA/VIIRS/002/VNP21A1D").select('LST_1KM').filterDate(time_start, time_end)

# ds_lst = xr.open_dataset(lst, engine = 'ee', crs = 'EPSG:4326', scale = 0.05, geometry = roi)

# ds_lst

# ds_lst.LST_1KM.plot(x = 'lon', y = 'lat', cmap = 'hot_r', col = 'time', col_wrap = 5, robust = True)