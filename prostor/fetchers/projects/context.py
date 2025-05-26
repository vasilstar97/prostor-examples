import pandas as pd
import geopandas as gpd
from prostor.api import api
from prostor.fetchers.territories import get_territory_geometry

def get_physical_objects(project_id : int, **kwargs) -> dict:
    res = api.get(f'/api/v1/projects/{project_id}/context/physical_objects_with_geometry', params=kwargs)
    features = res['features']
    return gpd.GeoDataFrame.from_features(features, crs=4326).set_index('physical_object_id')
