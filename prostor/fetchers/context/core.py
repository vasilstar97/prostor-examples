import geopandas as gpd
import pandas as pd
from prostor.api import api

def get_physical_objects(scenario_id : int, **kwargs) -> gpd.GeoDataFrame:
    res = api.get(f'/api/v1/scenarios/{scenario_id}/context/physical_objects_with_geometry', params=kwargs)
    features = res['features']
    return gpd.GeoDataFrame.from_features(features, crs=4326).set_index('physical_object_id')

def get_functional_zones_sources(scenario_id : int, **kwargs) -> pd.DataFrame:
    res = api.get(f'/api/v1/scenarios/{scenario_id}/context/functional_zone_sources')
    return pd.DataFrame(res)

def get_functional_zones(scenario_id : int, year : int, source : int):
    res = api.get(f'/api/v1/scenarios/{scenario_id}/context/functional_zones', params={
        'year': year,
        'source': source
    })
    features = res['features']
    return gpd.GeoDataFrame.from_features(features, crs=4326).set_index('functional_zone_id')

def get_services(scenario_id : int, **kwargs):
    res = api.get(f'/api/v1/scenarios/{scenario_id}/context/services_with_geometry', params=kwargs)
    features = res['features']
    return gpd.GeoDataFrame.from_features(features, crs=4326).set_index('service_id')