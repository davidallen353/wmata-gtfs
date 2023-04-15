import urllib
from ..utilities import get_json_data

from logging import getLogger

logger = getLogger(__name__)


"""https://developer.wmata.com/docs/services/5476364f031f590f38092507/operations/5476364f031f5909e4fe330c"""


def get_lines_data(API_KEY: str) -> dict:
    return get_json_data(
        API_KEY=API_KEY,
        URL="/Rail.svc/json/jLines?",
        function_desc="Get rail lines JSON data",
    )


def get_parking_data(API_KEY: str, STATION_CODE: str = "") -> dict:
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
            f"Getting station entrances near {LATITUDE_DEG}, {LONGITUDE_DEG} radius {RADIUS_M}m"
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
