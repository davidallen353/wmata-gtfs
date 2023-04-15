import http.client, json
from . import gtfs_realtime_pb2
from google.protobuf.json_format import MessageToDict

from logging import getLogger

logger = getLogger(__name__)


def get_gtfs_rt_data(
    API_KEY: str, URL: str, function_desc: str = "Get generic GTFS RT data"
) -> dict:
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

        feed = gtfs_realtime_pb2.FeedMessage()
        feed.ParseFromString(data)

        data_as_dict = MessageToDict(feed)

        return data_as_dict

    except Exception as e:
        logger.warning(f"Failed to {function_desc}|| Error: {e}")


def get_json_data(
    API_KEY: str, URL: str, function_desc: str = "Get generic GTFS RT data"
) -> dict:
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
