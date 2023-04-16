"""https://developer.wmata.com/docs/services/547636a6f9182302184cda78/operations/547636a6f918230da855363f"""
import urllib
from ..utilities import get_json_data


def get_next_trains(API_KEY: str, STATION_CODE: str = "All") -> dict:
    """
    Retrieves real-time train prediction data for the specified Metro station or all
    stations from WMATA's API using a GET request with the provided API key.

    Args:
        API_KEY (str): The API key to use for authentication.
        STATION_CODE (str, optional): The station code for the station to retrieve train
            predictions for. Defaults to "All" to retrieve predictions for all stations.

    Returns:
        dict: A dictionary containing the real-time train prediction data for the
            specified station(s).

    Raises:
        Warning: If the function fails to retrieve the real-time train prediction data
            from the API.

    TODO:
        The API says you can have a list but syntax is undocumented
    """
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
