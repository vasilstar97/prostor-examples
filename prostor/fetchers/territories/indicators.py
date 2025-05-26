import pandas as pd
import geopandas as gpd
from prostor.api import api

def get_indicators(parent_id : int | None = None, **kwargs):
    res = api.get('/api/v1/indicators_by_parent', params={
        'parent_id': parent_id,
        **kwargs
    })
    return pd.DataFrame(res).set_index('indicator_id')

def get_indicators_values(territory_id : int, indicators_ids : list[int] = [], **kwargs):
    res = api.get(f'/api/v1/territory/{territory_id}/indicator_values', params={
        'indicator_ids': str.join(',', [str(ind_id) for ind_id in indicators_ids]) if len(indicators_ids)>0 else None,
        **kwargs
    })
    return pd.DataFrame(res).set_index('indicator_value_id')