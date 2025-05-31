import geopandas as gpd
import pandas as pd

BUILDINGS_RULES = {
    'number_of_floors': [
        ['floors'],
        ['properties', 'storeys_count'],
        ['properties', 'osm_data', 'building:levels']
    ],
    'footprint_area': [
        ['building_area_official'],
        ['building_area_modeled'],
        ['properties', 'area_total']
    ],
    'build_floor_area': [
        ['properties', 'area_total'],
    ],
    'living_area': [
        ['properties', 'living_area_official'],
        ['properties', 'living_area'],
        ['properties', 'living_area_modeled']
    ],
    'non_living_area': [
        ['properties', 'area_non_residential'],
    ],
    'population': [
        ['properties', 'population_balanced']
    ]
}

def _parse(data : dict | None, *args):
    key = args[0]
    args = args[1:]
    if data is not None and key in data and data[key] is not None:
        if len(args) == 0:
            value = data[key]
            if isinstance(value, str):
                value = value.replace(',', '.')
            return value
        return _parse(data[key], *args)
    return None

def _adapt(data : dict, rules : list):
    for rule in rules:
        value = _parse(data, *rule)
        if value is not None:
            return value
    return None

def adapt_buildings(buildings_gdf : gpd.GeoDataFrame, living_pot_id : int = 4):
    gdf = buildings_gdf[['geometry']].copy()
    gdf['is_living'] = buildings_gdf['physical_object_type'].apply(lambda pot : pot['physical_object_type_id'] == 4)
    for column, rules in BUILDINGS_RULES.items():
        series = buildings_gdf['building'].apply(lambda b : _adapt(b, rules))
        gdf[column] = pd.to_numeric(series, errors='coerce')
    return gdf