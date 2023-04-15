from .utilities import get_gtfs_rt_data

from logging import getLogger

logger = getLogger(__name__)


def get_rail_alerts(API_KEY: str) -> dict:
    """Get WMATA Rail Alerts

    Args:
        API_KEY (str): Your API Key

    Returns:
        dict: _description_
    """
    return get_gtfs_rt_data(
        API_KEY=API_KEY,
        URL="/gtfs/rail-gtfsrt-alerts.pb?",
        function_desc="Get Rail Alerts",
    )


def get_bus_alerts(API_KEY: str) -> dict:
    """Get WMATA Bus Alerts

    Args:
        API_KEY (str): Your API Key

    Returns:
        dict: _description_
    """

    return get_gtfs_rt_data(
        API_KEY=API_KEY,
        URL="/gtfs/bus-gtfsrt-alerts.pb?",
        function_desc="Get Bus Alerts",
    )
