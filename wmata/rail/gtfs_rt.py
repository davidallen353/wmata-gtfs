from ..utilities import get_gtfs_rt_data

from logging import getLogger

logger = getLogger(__name__)


def get_rail_rt_vehicle_positions(API_KEY: str) -> dict:
    return get_gtfs_rt_data(
        API_KEY=API_KEY,
        URL="/gtfs/rail-gtfsrt-vehiclepositions.pb?",
        function_desc="Get Rail RT Vehicle Positions",
    )


def get_rail_rt_trip_updates(API_KEY: str) -> dict:
    return get_gtfs_rt_data(
        API_KEY=API_KEY,
        URL="/gtfs/rail-gtfsrt-tripupdates.pb?",
        function_desc="Get Rail RT Trip Updates",
    )
