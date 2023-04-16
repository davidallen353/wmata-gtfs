"""
This script provides functions for retrieving WMATA Rail and Bus Alerts from the GTFS Real-Time API.

Functions:
    - get_rail_alerts(API_KEY: str) -> dict:
        Retrieves WMATA Rail Alerts from the GTFS Real-Time API using the provided API key.
        
    - get_bus_alerts(API_KEY: str) -> dict:
        Retrieves WMATA Bus Alerts from the GTFS Real-Time API using the provided API key.

Args:
    API_KEY (str): The API key to use for authentication.

Returns:
    dict: A dictionary containing the GTFS Real-Time alerts returned by the API, converted from the protobuf format.
    
Raises:
    Warning: If the function fails to retrieve the alerts from the API, or if there is an error converting the data 
        from protobuf to a dictionary.
"""

from .utilities import get_gtfs_rt_data

from logging import getLogger

logger = getLogger(__name__)


def get_rail_alerts(API_KEY: str) -> dict:
    """Retrieves WMATA Rail Alerts from GTFS Real-Time API using the provided API key.

    Args:
        API_KEY (str): The API key to use for authentication.

    Returns:
        dict: A dictionary containing the WMATA Rail Alerts data returned by the API,
            converted from the protobuf format.

    Raises:
        Warning: If the function fails to retrieve the WMATA Rail Alerts data from the
            API, or if there is an error converting the data from protobuf to a
            dictionary.
    """
    return get_gtfs_rt_data(
        API_KEY=API_KEY,
        URL="/gtfs/rail-gtfsrt-alerts.pb?",
        function_desc="Get Rail Alerts",
    )


def get_bus_alerts(API_KEY: str) -> dict:
    """Retrieves WMATA Bus Alerts from GTFS Real-Time API using the provided API key.

    Args:
        API_KEY (str): The API key to use for authentication.

    Returns:
        dict: A dictionary containing the WMATA Bus Alerts data returned by the API,
            converted from the protobuf format.

    Raises:
        Warning: If the function fails to retrieve the WMATA Bus Alerts data from the
            API, or if there is an error converting the data from protobuf to a
            dictionary.
    """
    return get_gtfs_rt_data(
        API_KEY=API_KEY,
        URL="/gtfs/bus-gtfsrt-alerts.pb?",
        function_desc="Get Bus Alerts",
    )
