from wmata2.wmata import WMATA


with open("parts/wmata_api_key") as f:
    api_key = f.read().strip()

wmata = WMATA(api_key)
departures = wmata.get_next_departures("K08", "C08", num_trips=5)
print(departures)
