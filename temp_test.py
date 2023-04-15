from wmata import alerts
from wmata.rail import gtfs_rt as rail_gtfs
from wmata.rail import station_info
from wmata.rail import predictions

from time import sleep

# Load API Key

with open("parts/wmata_api_key") as f:
    api_key = f.read().strip()

# rail_alerts = alerts.get_rail_alerts(api_key)
# bus_alerts = alerts.get_bus_alerts(api_key)

# sleep(1)
# train_positions = rail_gtfs.get_rail_rt_vehicle_positions(api_key)
# train_trip_updates = rail_gtfs.get_rail_rt_trip_updates(api_key)

# sleep(1)
# rail_lines = station_info.get_lines_data(api_key)
# rail_parking = station_info.get_parking_data(api_key, "F06")
# rail_path_between_stations = station_info.get_path_between_stations(
#     api_key, "K08", "C05"
# )
# rail_station_entrances_all = station_info.get_station_entrances(api_key)
# rail_station_entrances_example = station_info.get_station_entrances(
#     api_key, LATITUDE_DEG=38.8978168, LONGITUDE_DEG=-77.0404246, RADIUS_M=500.0
# )

# sleep(1)
# rail_station_info_ex = station_info.get_station_info(api_key, "C01")
# rail_station_list = station_info.get_station_list(api_key, "OR")
# rail_station_timing = station_info.get_station_timing(api_key, "K08")

# # rail_station2station_all = rail_station_info.get_station2station_info(api_key)
# rail_station2station = station_info.get_station2station_info(api_key, "K08", "C05")

predict_all = predictions.get_next_trains(api_key)
predict_ex = predictions.get_next_trains(api_key, STATION_CODE="F03")

# print("==================")
# print(rail_alerts)

# print("==================")
# print(bus_alerts)

# print("==================")
# print(train_positions)

# print("==================")
# print(train_trip_updates)

# print("==================")
# print(rail_lines)

# print("==================")
# print(rail_parking)

# print("==================")
# print(rail_path_between_stations)

# print("==================")
# print(rail_station_entrances_all)

# print("==================")
# print(rail_station_entrances_example)

# print("==================")
# print(rail_station_info_ex)


# print("==================")
# print(rail_station_list)

# print("==================")
# print(rail_station_timing)

# print("==================")
# print(rail_station2station_all)

# print("==================")
# print(rail_station2station)
print("==================")
print(predict_all)
print(predict_ex)
