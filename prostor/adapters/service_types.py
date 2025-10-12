import pandas as pd
import prostor.fetchers.misc as misc
from blocksnet.config import service_types_config

SERVICE_TYPES_MAPPING = {
    # basic
    1: 'park',
    21: 'kindergarten',
    22: 'school',
    28: 'polyclinic',
    34: 'pharmacy',
    61: 'cafe',
    66: 'pitch',
    68: None, # спортивный зал
    74: 'playground',
    78: 'police',
    # additional
    30 : None, # стоматология
    35 : 'hospital',
    50 : 'museum',
    56 : 'cinema',
    57 : 'mall', 
    59 : 'stadium',
    62 : 'restaurant',
    63 : 'bar',
    77 : None, # скейт парк
    79 : None, # пожарная станция
    80 : 'train_station',
    89 : 'supermarket',
    99 : None, # пункт выдачи
    100 : 'bank',
    107 : 'veterinary',
    143 : 'sanatorium',
    # comfort
    5 : 'beach',
    27 : 'university',
    36 : None, # роддом
    48 : 'library',
    51 : 'theatre',
    91 : 'market',
    93 : None, # одежда и обувь
    94 : None, # бытовая техника
    95 : None, # книжный магазин
    96 : None, # детские товары
    97 : None, # спортивный магазин
    108 : None, # зоомагазин
    110 : 'hotel',
    114 : 'religion', # религиозный объект
    # others
    26 : None, # ССУЗ
    32 : None, # женская консультация
    39 : None, # скорая помощь
    40 : None, # травматология
    45 : 'recruitment',
    47 : 'multifunctional_center',
    55 : 'zoo',
    65 : 'bakery',
    67 : 'swimming_pool',
    75 : None, # парк аттракционов
    81 : 'train_building',
    82 : 'aeroway_terminal', # аэропорт??
    86 : 'bus_station',
    88 : 'subway_entrance',
    102 : 'lawyer',
    103 : 'notary',
    109 : 'dog_park',
    111 : 'hostel',
    112 : None, # база отдыха
    113 : None, # памятник
}

for st_id,st_name in SERVICE_TYPES_MAPPING.items():
    if st_name is None:
        continue
    assert st_name in service_types_config, f'{st_id}:{st_name} not in config'


def _adapt_name(service_type_id : int):
    return SERVICE_TYPES_MAPPING.get(service_type_id)

def _adapt_infrastructure_weight(data : dict):
    return data.get('weight_value', None)

def _adapt_social_values(service_type_id : int):
    social_values = misc.get_service_type_social_values(service_type_id)
    if social_values is None:
        return None
    else:
        return list(social_values.index)

def adapt_service_types(service_types_df : pd.DataFrame):
    df = service_types_df[['infrastructure_type']].copy()
    df['infrastructure_weight'] = service_types_df['properties'].apply(_adapt_infrastructure_weight)
    df['name'] = df.apply(lambda s : _adapt_name(s.name), axis=1)
    # df = df[~df['name'].isna()].copy()
    
    df['social_values'] = df.apply(lambda s : _adapt_social_values(s.name), axis=1)

    return df[['name', 'infrastructure_type', 'infrastructure_weight', 'social_values']].copy()
