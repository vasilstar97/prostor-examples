from prostor.api import api
import pandas as pd
import geopandas as gpd
import json
import shapely

def get_project(project_id : int) -> dict:
    res = api.get(f'/api/v1/projects/{project_id}')
    return res

def get_project_geometry(project_id : int):
    res = api.get(f'/api/v1/projects/{project_id}/territory')
    geometry_json = json.dumps(res['geometry'])
    return shapely.from_geojson(geometry_json)