"""
This module provides functions to retrieve real-time vehicle position and trip update
data for Metro rail trains from WMATA's API using a provided API key.

Functions:

get_rail_rt_vehicle_positions(API_KEY: str) -> dict: Retrieves real-time vehicle
    position data for Metro rail trains.
get_rail_rt_trip_updates(API_KEY: str) -> dict: Retrieves real-time trip update data for
    Metro rail trains.

Usage:
To use these functions, import them from the module and provide the necessary API key as
    an argument:

Example:
from wmata.realtime.rail import get_rail_rt_vehicle_positions
vehicle_positions_data = get_rail_rt_vehicle_positions(API_KEY)

Raises:
Warning: If the functions fail to retrieve the real-time data from the API, or if there
    is an error converting the data from protobuf to a dictionary.
"""
from ..utilities import get_gtfs_rt_data
from ..alerts import get_rail_alerts

from logging import getLogger

logger = getLogger(__name__)


def get_rail_rt_vehicle_positions(API_KEY: str) -> dict:
    """
    Retrieves real-time vehicle position data for Metro rail trains from WMATA's API
    using a GET request with the provided API key.

    Args:
        API_KEY (str): The API key to use for authentication.

    Returns:
        dict: A dictionary containing the real-time vehicle position data for Metro rail
            trains, converted from the protobuf format.

    Raises:
        Warning: If the function fails to retrieve the real-time vehicle position data
            from the API, or if there is an error converting the data from protobuf to a
            dictionary.

    """
    return get_gtfs_rt_data(
        API_KEY=API_KEY,
        URL="/gtfs/rail-gtfsrt-vehiclepositions.pb?",
        function_desc="Get Rail RT Vehicle Positions",
    )


def get_rail_rt_trip_updates(API_KEY: str) -> dict:
    """
    Retrieves real-time trip update data for Metro rail trains from WMATA's API using a
    GET request with the provided API key.

    Args:
        API_KEY (str): The API key to use for authentication.

    Returns:
        dict: A dictionary containing the real-time trip update data for Metro rail
            trains, converted from the protobuf format.

    Raises:
        Warning: If the function fails to retrieve the real-time trip update data from
            the API, or if there is an error converting the data from protobuf to a
            dictionary.

    """
    return get_gtfs_rt_data(
        API_KEY=API_KEY,
        URL="/gtfs/rail-gtfsrt-tripupdates.pb?",
        function_desc="Get Rail RT Trip Updates",
    )
