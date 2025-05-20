import requests
from functools import wraps
from typing import Callable, Union, ParamSpec, TypeVar

P = ParamSpec('P')
R = TypeVar('R')

def _raise_for_status(func) -> Callable[P, Union[dict,list]]:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Union[dict,list]: 
        result = func(*args, **kwargs)
        result.raise_for_status()
        return result.json()
    return wrapper

class API:
    def __init__(self, url : str):
        self.url = url

    @_raise_for_status
    def get(self, endpoint, *args, **kwargs) -> requests.Response:
        res = requests.get(self.url + endpoint, *args, **kwargs)
        return res
  
    @_raise_for_status
    def post(self, endpoint, *args, **kwargs) -> requests.Response:
        return requests.post(self.url + endpoint, *args, **kwargs)

api = API('http://10.32.1.107:5300')