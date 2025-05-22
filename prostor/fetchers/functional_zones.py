from prostor.api import api
import pandas as pd
import geopandas as gpd

def get_functional_zones_sources(territory_id : int):
    res = api.get(f'/api/v1/territory/{territory_id}/functional_zone_sources')
    return pd.DataFrame(res)

def get_functional_zones(territory_id : int, year : int, source : int):
    res = api.get(f'/api/v1/territory/{territory_id}/functional_zones_geojson', params={
        'year': year,
        'source': source
    })
    features = res['features']
    return gpd.GeoDataFrame.from_features(features, crs=4326).set_index('functional_zone_id')