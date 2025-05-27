import pandas as pd
import geopandas as gpd
from prostor.api import api

def get_physical_objects(project_id : int, **kwargs) -> dict:
    res = api.get(f'/api/v1/projects/{project_id}/context/physical_objects_with_geometry', params=kwargs)
    features = res['features']
    return gpd.GeoDataFrame.from_features(features, crs=4326).set_index('physical_object_id')

def get_services(project_id : int, **kwargs) -> dict:
    res = api.get(f'/api/v1/projects/{project_id}/context/services_with_geometry', params=kwargs)
    features = res['features']
    return gpd.GeoDataFrame.from_features(features, crs=4326).set_index('service_id')

def get_functional_zones_sources(project_id : int):
    res = api.get(f'/api/v1/projects/{project_id}/context/functional_zone_sources')
    return pd.DataFrame(res)

def get_functional_zones(project_id : int, year : int, source : int):
    res = api.get(f'/api/v1/projects/{project_id}/context/functional_zones', params={
        'year': year,
        'source': source
    })
    features = res['features']
    return gpd.GeoDataFrame.from_features(features, crs=4326).set_index('functional_zone_id')

