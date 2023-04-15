"""https://developer.wmata.com/docs/services/547636a6f9182302184cda78/operations/547636a6f918230da855363f"""
import urllib
from ..utilities import get_json_data


def get_next_trains(API_KEY: str, STATION_CODE: str = "All") -> dict:
    # TODO: The API says you can have a list but syntax is undocumented
    params = urllib.parse.urlencode(
        {
            "StationCodes": STATION_CODE,
        }
    )
    URL = "/StationPrediction.svc/json/GetPrediction/" + STATION_CODE
    return get_json_data(
        API_KEY=API_KEY,
        URL=URL,
        function_desc="Get real time next train predictions",
    )
