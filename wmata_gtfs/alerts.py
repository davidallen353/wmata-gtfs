import http.client, urllib.request, urllib.parse, urllib.error, base64
from . import gtfs_realtime_pb2
from google.protobuf.json_format import MessageToDict

from logging import getLogger

logger = getLogger(__name__)

def get_rail_alerts(API_KEY: str) -> dict:
    """Get WMATA Rail Alerts

    Args:
        API_KEY (str): Your API Key
    
    Returns:
        dict: _description_
    """


    # Make the request header
    headers = {'api_key': API_KEY,}

    params = urllib.parse.urlencode({})

    try:
        conn = http.client.HTTPSConnection('api.wmata.com')
        conn.request("GET", "/gtfs/rail-gtfsrt-alerts.pb?%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()

        feed = gtfs_realtime_pb2.FeedMessage()
        feed.ParseFromString(data)

        data_as_dict = MessageToDict(feed)

        return data_as_dict

    except Exception as e:
        logger.warning(f"Could not get rail alerts. Error: {e}")

def get_bus_alerts(API_KEY: str) -> dict:
    """Get WMATA Bus Alerts

    Args:
        API_KEY (str): Your API Key
    
    Returns:
        dict: _description_
    """


    # Make the request header
    headers = {'api_key': API_KEY,}

    params = urllib.parse.urlencode({})

    try:
        conn = http.client.HTTPSConnection('api.wmata.com')
        conn.request("GET", "/gtfs/bus-gtfsrt-alerts.pb?%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()

        feed = gtfs_realtime_pb2.FeedMessage()
        feed.ParseFromString(data)

        data_as_dict = MessageToDict(feed)

        return data_as_dict

    except Exception as e:
        logger.warning(f"Could not get bus alerts. Error: {e}")