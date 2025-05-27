import geopandas as gpd
from blocksnet.enums import LandUse

LAND_USE_RULES = {
    'residential' : LandUse.RESIDENTIAL,
    'recreation' : LandUse.RECREATION,
    'special' : LandUse.SPECIAL,
    'industrial' : LandUse.INDUSTRIAL,
    'agriculture' : LandUse.AGRICULTURE,
    'transport' : LandUse.TRANSPORT,
    'business' : LandUse.BUSINESS,
    'residential_individual' : LandUse.RESIDENTIAL,
    'residential_lowrise' : LandUse.RESIDENTIAL,
    'residential_midrise' : LandUse.RESIDENTIAL,
    'residential_multistorey' : LandUse.RESIDENTIAL,
}

def _adapt_functional_zone(data : dict):
    functional_zone_type_id = data['name']
    return functional_zone_type_id

def adapt_functional_zones(functional_zones_gdf : gpd.GeoDataFrame):
    gdf = functional_zones_gdf[['geometry']].copy()
    gdf['functional_zone'] = functional_zones_gdf['functional_zone_type'].apply(_adapt_functional_zone)
    return gdf