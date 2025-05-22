import geopandas as gpd
from blocksnet.enums import LandUse

LAND_USE_RULES = {
    1 : LandUse.RESIDENTIAL,
    2 : LandUse.RECREATION,
    3 : LandUse.SPECIAL,
    4 : LandUse.INDUSTRIAL,
    5 : LandUse.AGRICULTURE,
    6 : LandUse.TRANSPORT,
    7 : LandUse.BUSINESS,
    10 : LandUse.RESIDENTIAL,
    11 : LandUse.RESIDENTIAL,
    12 : LandUse.RESIDENTIAL,
    13 : LandUse.RESIDENTIAL,
}

def _adapt_functional_zone(data : dict):
    functional_zone_type_id = data['id']
    return LAND_USE_RULES.get(functional_zone_type_id)

def adapt_functional_zones(functional_zones_gdf : gpd.GeoDataFrame):
    gdf = functional_zones_gdf[['geometry']].copy()
    gdf['functional_zone'] = functional_zones_gdf['functional_zone_type'].apply(_adapt_functional_zone)
    return gdf