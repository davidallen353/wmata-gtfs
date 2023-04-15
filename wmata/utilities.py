import http.client, urllib.request, urllib.parse, urllib.error, json
from . import gtfs_realtime_pb2
from google.protobuf.json_format import MessageToDict

from logging import getLogger

logger = getLogger(__name__)


def get_gtfs_rt_data(
    API_KEY: str, URL: str, function_desc: str = "Get generic GTFS RT data"
) -> dict:
    # Make the request header
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
