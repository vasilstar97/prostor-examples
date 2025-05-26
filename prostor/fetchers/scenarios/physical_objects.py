import pandas as pd
import geopandas as gpd
from prostor.api import api

def get_physical_objects(scenario_id : int, **kwargs):
    res = api.get(f'/api/v1/scenarios/{scenario_id}/physical_objects_with_geometry', params=kwargs)
    features = res['features']
    return gpd.GeoDataFrame.from_features(features, crs=4326).set_index('physical_object_id')

