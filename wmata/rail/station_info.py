"""This module provides functions for interacting with the Washington Metropolitan Area
    Transit Authority (WMATA) API to retrieve information on WMATA's rail system.

Functions:
- get_lines_data(API_KEY: str) -> dict: Get rail lines JSON data.
- get_parking_data(API_KEY: str, STATION_CODE: str = "") -> dict: Get parking JSON data.
- get_path_between_stations(API_KEY: str, START_STATION: str, END_STATION: str) -> dict: Get path between stations.
- get_station_entrances(API_KEY: str, LATITUDE_DEG: float = 0.0, LONGITUDE_DEG: float = 0.0, RADIUS_M: float = 0.0) -> dict: Get nearby station entrances.
- get_station_info(API_KEY: str, STATION_CODE: str) -> dict: Get station information by station code.
- get_station_list(API_KEY: str, LINE_CODE: str = "") -> dict: Get a list of stations for a specific rail line or all rail lines.
- get_station_timing(API_KEY: str, STATION_CODE: str = "") -> dict: Get station arrival times by station code.

Example usage:
    import wmata_api
    api_key = 'YOUR_API_KEY'
    lines_data = wmata_api.get_lines_data(api_key)
    station_info = wmata_api.get_station_info(api_key, 'A01')
    station_timing = wmata_api.get_station_timing(api_key, 'A01')
"""

import urllib
from ..utilities import get_json_data

from logging import getLogger

logger = getLogger(__name__)

"""https://developer.wmata.com/docs/services/5476364f031f590f38092507/operations/5476364f031f5909e4fe330c"""


def get_lines_data(API_KEY: str) -> dict:
    """
    Get rail lines JSON data.

    Args:
        API_KEY (str): WMATA API key.

    Returns:
        dict: JSON data containing rail lines information.
    """
    return get_json_data(
        API_KEY=API_KEY,
        URL="/Rail.svc/json/jLines?",
        function_desc="Get rail lines JSON data",
    )


def get_parking_data(API_KEY: str, STATION_CODE: str = "") -> dict:
    """
    Get parking JSON data.

    Args:
        API_KEY (str): WMATA API key.
        STATION_CODE (str, optional): Station code. Defaults to "".

    Returns:
        dict: JSON data containing parking information.
    """
    params = urllib.parse.urlencode(
        {
            "StationCode": STATION_CODE,
        }
    )
    return get_json_data(
        API_KEY=API_KEY,
        URL="/Rail.svc/json/jStationParking?%s" % params,
        function_desc="Get parking JSON data",
    )


def get_path_between_stations(
    API_KEY: str, START_STATION: str, END_STATION: str
) -> dict:
    """
    Get path between stations.

    Args:
        API_KEY (str): WMATA API key.
        START_STATION (str): Station code for the starting station.
        END_STATION (str): Station code for the ending station.

    Returns:
        dict: JSON data containing path information between the two stations.
    """
    params = urllib.parse.urlencode(
        {
            "FromStationCode": START_STATION,
            "ToStationCode": END_STATION,
        }
    )

    return get_json_data(
        API_KEY=API_KEY,
        URL="/Rail.svc/json/jPath?%s" % params,
        function_desc="Get path between stations",
    )


def get_station_entrances(
    API_KEY: str,
    LATITUDE_DEG: float = 0.0,
    LONGITUDE_DEG: float = 0.0,
    RADIUS_M: float = 0.0,
) -> dict:
    """
    Get nearby station entrances.

    Args:
        API_KEY (str): WMATA API key.
        LATITUDE_DEG (float, optional): Latitude. Defaults to 0.0.
        LONGITUDE_DEG (float, optional): Longitude. Defaults to 0.0.
        RADIUS_M (float, optional): Radius in meters. Defaults to 0.0.

    Returns:
        dict: JSON data containing station entrances information.
    """
    if LATITUDE_DEG == 0.0 and LONGITUDE_DEG == 0.0:
        logger.info("Lat/Lon not specified. Getting all station entrances.")
        URL = "/Rail.svc/json/jStationEntrances?"
    elif RADIUS_M == 0.0:
        logger.warning(
            "Lat/Lon specified but radius==0. Getting all station entrances."
        )
        URL = "/Rail.svc/json/jStationEntrances?"
    else:
        logger.info(
            f"Getting station entrances near {LATITUDE_DEG}, {LONGITUDE_DEG}"
            + f" radius {RADIUS_M}m"
        )
        params = urllib.parse.urlencode(
            {
                "Lat": str(LATITUDE_DEG),
                "Lon": str(LONGITUDE_DEG),
                "Radius": str(RADIUS_M),
            }
        )

        URL = "/Rail.svc/json/jStationEntrances?%s" % params

    return get_json_data(
        API_KEY=API_KEY,
        URL=URL,
        function_desc="Get nearby station entrances",
    )


def get_station_info(API_KEY: str, STATION_CODE: str) -> dict:
    """Get station information by station code.

    Args:
        API_KEY (str): WMATA API key.
        STATION_CODE (str): Station code.

    Returns:
        dict: JSON data containing station information.
    """
    params = urllib.parse.urlencode(
        {
            "StationCode": STATION_CODE,
        }
    )
    return get_json_data(
        API_KEY=API_KEY,
        URL="/Rail.svc/json/jStationInfo?%s" % params,
        function_desc="Get station info JSON data",
    )


def get_station_list(API_KEY: str, LINE_CODE: str = "") -> dict:
    """Get a list of stations for a specific rail line or all rail lines.

    Args:
        API_KEY (str): WMATA API key.
        LINE_CODE (str, optional): Rail line code. Defaults to "".

    Returns:
        dict: JSON data containing station list information.
    """
    params = urllib.parse.urlencode(
        {
            "LineCode": LINE_CODE,
        }
    )
    return get_json_data(
        API_KEY=API_KEY,
        URL="/Rail.svc/json/jStations?%s" % params,
        function_desc="Get stations list for rail line",
    )


def get_station_timing(API_KEY: str, STATION_CODE: str = "") -> dict:
    """Get station arrival times by station code.

    Args:
        API_KEY (str): WMATA API key.
        STATION_CODE (str, optional): Station code. Defaults to "".

    Returns:
        dict: JSON data containing station arrival times.
    """
    params = urllib.parse.urlencode(
        {
            "StationCode": STATION_CODE,
        }
    )
    return get_json_data(
        API_KEY=API_KEY,
        URL="/Rail.svc/json/jStationTimes?%s" % params,
        function_desc="Get stations timing info",
    )


def get_station2station_info(
    API_KEY: str,
    START_STATION: str = "",
    END_STATION: str = "",
) -> dict:
    """Get station-to-station information.

    Args:
        API_KEY (str): WMATA API key.
        START_STATION (str, optional): Starting station code. Defaults to "".
        END_STATION (str, optional): Ending station code. Defaults to "".

    Returns:
        dict: JSON data containing station-to-station information.
    """
    if START_STATION == "":
        URL = "/Rail.svc/json/jSrcStationToDstStationInfo"
    elif END_STATION == "":
        logger.error("End station not specified getting all s2s info")
        URL = "/Rail.svc/json/jSrcStationToDstStationInfo"
    else:
        params = urllib.parse.urlencode(
            {
                "FromStationCode": START_STATION,
                "ToStationCode": END_STATION,
            }
        )
        URL = "/Rail.svc/json/jSrcStationToDstStationInfo?%s" % params

    return get_json_data(
        API_KEY=API_KEY,
        URL=URL,
        function_desc="Get station to station info",
    )
