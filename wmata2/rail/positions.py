"""
This module provides functions for accessing WMATA API to get information about live
train positions, standard train routes, and track circuits.

Functions:
    get_live_trains_positions(API_KEY: str) -> dict:
        Get live train positions from WMATA API.
    get_standard_routes(API_KEY: str) -> dict:
        Get standard train routes from WMATA API.
    get_track_circuits(API_KEY: str) -> dict:
        Get track circuits from WMATA API.

"""
from ..utilities import get_json_data

from logging import getLogger

logger = getLogger(__name__)


def get_live_trains_positions(API_KEY: str) -> dict:
    """Get live train positions from WMATA API.

    Args:
        API_KEY (str): Your API Key.

    Returns:
        dict: A dictionary containing live train positions.

    """

    URL = "/TrainPositions/TrainPositions?contentType=json"

    return get_json_data(
        API_KEY=API_KEY,
        URL=URL,
        function_desc="Get live train positions",
    )


def get_standard_routes(API_KEY: str) -> dict:
    """Get standard train routes from WMATA API.

    Args:
        API_KEY (str): Your API Key.

    Returns:
        dict: A dictionary containing standard train routes.

    """

    URL = "/TrainPositions/StandardRoutes?contentType=json"

    return get_json_data(
        API_KEY=API_KEY,
        URL=URL,
        function_desc="Get live train positions",
    )


def get_track_circuits(API_KEY: str) -> dict:
    """Get track circuits from WMATA API.

    Args:
        API_KEY (str): Your API Key.

    Returns:
        dict: A dictionary containing track circuits information.

    """

    URL = "/TrainPositions/TrackCircuits?contentType=json"

    return get_json_data(
        API_KEY=API_KEY,
        URL=URL,
        function_desc="Get live train positions",
    )
