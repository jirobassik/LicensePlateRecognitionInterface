import requests
import json
from typing import Final

URL: Final = "https://app.airops.com/public_api/data_apps/10/execute"
API_KEY: Final = 'PXzgyDmk4lbkgCIvNw3o2cDa9We4IzBKDntkLOSIIJ4mf1l1GfAJ0GNNKPhf'


def ai_query(query: str) -> str:
    def remove_substring(string: str) -> str:
        string = string.replace('```', '')
        string = string.replace('zrbsdrtr.', '')
        string = string.replace(';', '')
        string = string.replace('\n', ' ')
        return string

    def add_id(string_: str) -> str:
        string_ = string_.split()
        string_.insert(1, 'id,')
        return " ".join(string_)

    payload = {
        "input": {
            "tables": "search_ownermodel",
            "provider": "zrbsdrtr",
            "question": f'{query}'
        }
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    response = requests.post(URL, data=json.dumps(payload), headers=headers)
    query_json: dict[str, str] = response.json()

    print(query_json['result'])
    string_query = add_id(remove_substring(query_json['result']))
    print(string_query)
    return string_query
