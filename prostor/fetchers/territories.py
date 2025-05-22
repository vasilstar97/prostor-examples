import pandas as pd
import geopandas as gpd
import shapely
import json
from prostor.api import api

def _get_territories_with_geometry(**kwargs):
    res = api.get('/api/v1/all_territories', params=kwargs)
    features = res['features']
    return gpd.GeoDataFrame.from_features(features, crs=4326).set_index('territory_id')

def _get_territories_without_geometry(**kwargs):
    res = api.get('/api/v1/all_territories_without_geometry', params=kwargs)
    return pd.DataFrame(res).set_index('territory_id')

def _get_territories(geometry : bool, **kwargs):
    if geometry:
        return _get_territories_with_geometry(**kwargs)
    return _get_territories_without_geometry(**kwargs)

def get_countries(geometry : bool = False):
    return _get_territories(geometry=geometry)

def get_regions(country_id : int | None = None, geometry : bool = False):
    if country_id is not None:
        return _get_territories(geometry=geometry, parent_id=country_id)
    countries = get_countries()
    regions_dfs = [_get_territories(geometry=geometry, parent_id=i) for i in countries.index]
    return pd.concat(regions_dfs)

def get_territories(region_id : int, geometry : bool = False):
    return _get_territories(geometry=geometry, parent_id=region_id, get_all_levels=True)

def get_territory_geometry(territory_id : int):
    res = api.get(f'/api/v1/territory/{territory_id}')
    geometry_json = json.dumps(res['geometry'])
    return shapely.from_geojson(geometry_json)