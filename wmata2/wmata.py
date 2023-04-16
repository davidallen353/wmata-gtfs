"""
This module provides a Python wrapper for the WMATA API that allows a user to get route
and time information.
"""

from gps_time import GPSTime
from datetime import datetime

from .rail.station_info import get_station2station_info
from .rail.predictions import get_next_trains


class WMATA:
    """
    A class that provides methods for interacting with the WMATA API.
    """

    def __init__(self, api_key: str) -> None:
        """
        Initializes a new instance of the WMATA class with the specified API key.

        Args:
            api_key (str): The API key for accessing the WMATA API.
        """
        self.api_key = api_key

    def get_next_departures(
        self, start_station: str, end_station: str, num_trips: int = 5
    ) -> dict:
        """
        Returns the next departures, expected trip durations, and the expected time of
            arrival for the given start and end station codes.

        Args:
            start_station (str): The three-letter station code for the starting station.
            end_station (str): The three-letter station code for the ending station.
            num_trips (int, optional): The number of upcoming trips to return. Defaults to 5.

        Returns:
            dict: A dictionary containing the next departures, expected trip durations,
                and the expected time of arrival.
        """
        current_time = GPSTime.from_datetime(datetime.now())

        # Get the station-to-station information
        station_info = get_station2station_info(
            self.api_key, start_station, end_station
        )

        # Get the next trains
        next_trains = get_next_trains(self.api_key, start_station)

        # Combine the data into a dictionary
        result = {}
        for i in range(min(num_trips, len(next_trains["Trains"]))):
            trip = next_trains["Trains"][i]

            departure_dt_min = float(trip["Min"])

            trip_duration_min = float(
                station_info["StationToStationInfos"][0]["RailTime"]
            )

            departure_time = current_time + departure_dt_min * 60.0
            arrival_time = departure_time + trip_duration_min * 60.0

            # For type checking. GPSTime math can return numpay arrays
            assert isinstance(departure_time, GPSTime)
            assert isinstance(arrival_time, GPSTime)

            result[i] = {
                "departure_time": departure_time.to_datetime(),
                "duration_min": trip_duration_min,
                "arrival_time": arrival_time.to_datetime(),
            }

        return result
