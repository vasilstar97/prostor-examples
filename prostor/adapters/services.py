import geopandas as gpd
import pandas as pd

def _adapt_service_type(data : dict, service_types : pd.DataFrame) -> int:
    service_type_id = int(data['service_type_id'])
    if service_type_id in service_types.index:
        service_type_name = service_types.loc[service_type_id, 'name']
        return service_type_name
    return None

def adapt_services(buildings_gdf : gpd.GeoDataFrame, service_types : pd.DataFrame) -> dict[int, gpd.GeoDataFrame]:
    gdf = buildings_gdf[['geometry', 'capacity']].copy()
    gdf['service_type'] = buildings_gdf['service_type'].apply(lambda st : _adapt_service_type(st, service_types))
    gdf = gdf[~gdf['service_type'].isna()].copy()
    return {st:gdf[gdf['service_type']==st].drop(columns=['service_type']) for st in sorted(gdf['service_type'].unique())}