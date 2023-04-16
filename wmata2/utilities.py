"""
A module for retrieving data from WMATA's API.

This module contains functions for retrieving GTFS Real-Time and JSON data from
WMATA's API using a GET request with the provided API key and URL.

Functions:
- get_gtfs_rt_data(API_KEY, URL, function_desc="Get generic GTFS RT data"): 
  Retrieves GTFS Real-Time data from WMATA's API and returns a dictionary containing
  the data converted from the protobuf format. Raises a warning if the function fails
  to retrieve the data or convert it to a dictionary.

- get_json_data(API_KEY, URL, function_desc="Get generic GTFS RT data"):
  Retrieves JSON data from WMATA's API and returns a dictionary containing the data.
  Raises a warning if the function fails to retrieve the data.

- get_station_code(station_name: str) -> str:
  Returns the station code for a given station name.

- get_station_name(station_code: str) -> str:
  Returns the station name for a given station code.

Dependencies:
- http.client: a module that provides a low-level interface for making HTTP requests
- json: a module that provides methods for working with JSON data
- gtfs_realtime_pb2: a module that contains the classes and methods for working with
  GTFS Real-Time data in protobuf format
- MessageToDict: a method from the google.protobuf.json_format module that converts
  protobuf messages to dictionaries
- getLogger: a method from the logging module that returns a logger object for logging
  messages to a file or stream

"""

import http.client, json, csv, os, difflib
from . import gtfs_realtime_pb2
from google.protobuf.json_format import MessageToDict

from logging import getLogger

logger = getLogger(__name__)

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
RAIL_DATA_DIR = os.path.join(DATA_DIR, "rail_gtfs_static")
STOPS_FILE = os.path.join(RAIL_DATA_DIR, "stops.txt")


def get_gtfs_rt_data(
    API_KEY: str, URL: str, function_desc: str = "Get generic GTFS RT data"
) -> dict:  # type: ignore
    """
    Retrieves GTFS Real-Time data from WMATA's API using a GET request with the provided
    API key and URL.

    Args:
        API_KEY (str): The API key to use for authentication.
        URL (str): The URL of the GTFS Real-Time API endpoint to retrieve data from.
        function_desc (str, optional): A description of the function being performed.
            Defaults to "Get generic GTFS RT data".

    Returns:
        dict: A dictionary containing the GTFS Real-Time data returned by the API,
            converted from the protobuf format.

    Raises:
        Warning: If the function fails to retrieve the GTFS Real-Time data from the API,
            or if there is an error converting the data from protobuf to a dictionary.

    """
    headers = {
        "api_key": API_KEY,
    }

    try:
        logger.info(function_desc)
        logger.info("Connecting to GTFS API")
        conn = http.client.HTTPSConnection("api.wmata.com")
        conn.request("GET", URL, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
        logger.debug("Data received")

        feed = gtfs_realtime_pb2.FeedMessage()  # type: ignore
        feed.ParseFromString(data)

        data_as_dict = MessageToDict(feed)

        return data_as_dict

    except Exception as e:
        logger.warning(f"Failed to {function_desc}|| Error: {e}")


def get_json_data(
    API_KEY: str, URL: str, function_desc: str = "Get generic GTFS RT data"
) -> dict:  # type: ignore
    """
    Retrieves JSON data from WMATA's API using a GET request with the provided API key
    and URL.

    Args:
        API_KEY (str): The API key to use for authentication.
        URL (str): The URL of the API endpoint to retrieve data from.
        function_desc (str, optional): A description of the function being performed.
            Defaults to "Get generic GTFS RT data".

    Returns:
        dict: A dictionary containing the JSON data returned by the API.

    Raises:
        Warning: If the function fails to retrieve the JSON data from the API.

    """
    headers = {
        "api_key": API_KEY,
    }

    try:
        logger.info(function_desc)
        logger.info("Connecting to JSON API")
        conn = http.client.HTTPSConnection("api.wmata.com")
        conn.request("GET", URL, "{body}", headers)
        response = conn.getresponse()
        data_bytes = response.read()

        conn.close()
        logger.debug("Data received")

        data = json.loads(data_bytes.decode("utf-8"))

        return data
    except Exception as e:
        logger.warning(f"Failed to {function_desc}|| Error: {e}")


def get_station_code(station_name: str) -> str:
    """
    Returns the station code for a given station name.

    Args:
        station_name: A string representing the name of the station.

    Returns:
        A string representing the station code.
    """

    # station_code = None
    closest_match = None

    if not (os.path.exists(STOPS_FILE)):
        raise FileNotFoundError(
            "No rail stops file found. Try rebuilding the GTFS static files."
        )

    with open(STOPS_FILE, newline="", encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)
        stations = [row for row in reader if row["stop_id"].startswith("STN")]

    station_names = [station["stop_name"].lower() for station in stations]
    try:
        index = station_names.index(station_name.lower())
        return stations[index]["stop_id"][-3:]
    except ValueError:
        closest_match = difflib.get_close_matches(
            station_name.lower(), station_names, n=1, cutoff=0.2
        )[0]
        if closest_match:
            logger.warning(
                f"Warning: Could not find station {station_name.upper()}, "
                + f"did you mean {closest_match.upper()}?"
            )
            return get_station_code(closest_match)
        else:
            logger.error(f"Warning: Could not find station {station_name}")
        return None  # type: ignore


def get_station_name(station_code: str) -> str:
    """
    Returns the name of the station corresponding to the provided station code.

    Args:
        station_code (str): The 3 character station code.

    Returns:
        str: The name of the station.

    Raises:
        ValueError: If the station code is not found.
    """
    if not (os.path.exists(STOPS_FILE)):
        raise FileNotFoundError(
            "No rail stops file found. Try rebuilding the GTFS static files."
        )

    with open(STOPS_FILE, "r", encoding="utf-8") as stops_file:
        reader = csv.DictReader(stops_file)
        for row in reader:
            if row["stop_id"].startswith("STN_") and row["stop_id"][4:] == station_code:
                return row["stop_name"]
    raise ValueError(f"No station found for code: {station_code}")
