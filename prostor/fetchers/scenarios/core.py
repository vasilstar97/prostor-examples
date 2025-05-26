from prostor.api import api
import pandas as pd
import geopandas as gpd

def get_scenario(scenario_id : int) -> dict:
    res = api.get(f'/api/v1/scenarios/{scenario_id}')
    return res