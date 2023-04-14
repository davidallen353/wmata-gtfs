import requests
import json

import http.client, urllib.request, urllib.parse, urllib.error, base64
import gtfs_realtime_pb2
from google.protobuf.json_format import MessageToDict, MessageToJson

# Load API Key

with open("parts/wmata_api_key") as f:
    api_key = f.read().strip()
    print(api_key)


headers = {
    # Request headers
    'api_key': api_key,}

params = urllib.parse.urlencode({})

try:
    conn = http.client.HTTPSConnection('api.wmata.com')
    conn.request("GET", "/gtfs/rail-gtfsrt-alerts.pb?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    conn.close()

    print(" ")
    feed = gtfs_realtime_pb2.FeedMessage()
    feed.ParseFromString(data)

    data_as_dict = MessageToDict(feed)
    # print(data_as_dict)

    for _entity  in data_as_dict["entity"]:
        for _idx in _entity:
            print(_idx)
            
            if type(_entity[_idx]) == dict:
                print(_entity[_idx])
                print(_entity[_idx]["informedEntity"])
            print("----")

    # for entity in feed.entity:
    #     print(entity.alert)
    #     print(type(entity))
    #     print("-------")

except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################

# # Define the API endpoint and parameters
# endpoint = "https://api.wmata.com/StationPrediction.svc/json/GetPrediction/All"
# params = {"api_key": api_key, "StationCode": "A01"}

# # Make the API request
# response = requests.get(endpoint, params=params)

# # Parse the JSON response
# data = json.loads(response.text)

# # Print the results
# for train in data["Trains"]:
#     print(f"Destination: {train['DestinationName']}")
#     print(f"Line: {train['Line']}")
#     print(f"Arrival time: {train['Min']}")
#     print()

# # Make the API request
# endpoint = "https://api.wmata.com/Rail.svc/json/jStations"
# response = requests.get(endpoint, params=params)

# # Parse the JSON response
# data = json.loads(response.text)
# print(data)
# # Extract the station codes
# station_codes = []
# for station in data["Stations"]:
#     station_codes.append(station["Code"])

# # Print the station codes
# print(station_codes)


# ########### Python 3.2 #############
# import http.client, urllib.request, urllib.parse, urllib.error, base64

# headers = {
#     # Request headers
#     'api_key': api_key,
# }

# params = urllib.parse.urlencode({
# })

# try:
#     conn = http.client.HTTPSConnection('api.wmata.com')
#     conn.request("GET", "/gtfs/rail-gtfs-static.zip?%s" % params, "{body}", headers)
#     response = conn.getresponse()
#     data = response.read()
#     with open("bus_data.zip", "wb") as f:
#         f.write(data)
#     conn.close()
# except Exception as e:
#     print("[Errno {0}] {1}".format(e.errno, e.strerror))

# ####################################

