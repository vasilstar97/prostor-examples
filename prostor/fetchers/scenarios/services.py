import geopandas as gpd
from prostor.api import api

def get_services(scenario_id : int, **kwargs) -> dict:
    res = api.get(f'/api/v1/scenarios/{scenario_id}/services_with_geometry', params=kwargs)
    features = res['features']
    return gpd.GeoDataFrame.from_features(features, crs=4326).set_index('service_id')