import pandas as pd
import geopandas as gpd
from prostor.api import api

def get_physical_object_types(**kwargs):
    res = api.get('/api/v1/physical_object_types', params=kwargs)
    return pd.DataFrame(res).set_index('physical_object_type_id')

def get_physical_objects(territory_id : int, **kwargs):
    res = api.get(f'/api/v1/territory/{territory_id}/physical_objects_geojson', params=kwargs)
    features = res['features']
    return gpd.GeoDataFrame.from_features(features, crs=4326).set_index('physical_object_id')

