import pandas as pd
import geopandas as gpd
from prostor.api import api

def get_functional_zones_sources(scenario_id : int):
    res = api.get(f'/api/v1/scenarios/{scenario_id}/functional_zone_sources')
    return pd.DataFrame(res)

def get_functional_zones(scenario_id : int, year : int, source : int):
    res = api.get(f'/api/v1/scenarios/{scenario_id}/functional_zones', params={
        'year': year,
        'source': source
    })
    features = res['features']
    return gpd.GeoDataFrame.from_features(features, crs=4326).set_index('functional_zone_id')

