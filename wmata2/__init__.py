import http.client, urllib.request, urllib.parse, urllib.error, os, shutil
from zipfile import ZipFile
from logging import getLogger

logger = getLogger(__name__)


def rebuild_static_data(api_key: str) -> None:
    module_path = os.path.dirname(__file__)
    data_path = os.path.join(module_path, "data")

    if os.path.isdir(data_path):
        logger.debug("Deleting existing data")
        shutil.rmtree(data_path, ignore_errors=True)
        os.mkdir(data_path)
    
    RAIL_OUTPUT_DIR = os.path.join(data_path, "rail_gtfs_static")
    BUS_OUTPUT_DIR = os.path.join(data_path, "bus_gtfs_static")
    RAIL_OUTPUT_PATH = RAIL_OUTPUT_DIR + ".zip"
    BUS_OUTPUT_PATH = BUS_OUTPUT_DIR + ".zip"

    headers = {'api_key': api_key, }

    params = urllib.parse.urlencode({})

    try:
        logger.info("Downloading rail static data...")
        conn = http.client.HTTPSConnection('api.wmata.com')
        conn.request("GET", "/gtfs/rail-gtfs-static.zip?%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        
        with open(RAIL_OUTPUT_PATH, "wb") as f:
            f.write(data)
        conn.close()

        logger.debug("Extracting rail data...")
        with ZipFile(RAIL_OUTPUT_PATH, 'r') as zObject:
            # Extracting all the members of the zip 
            # into a specific location.
            zObject.extractall(path=RAIL_OUTPUT_DIR)

        logger.debug("Rail static data complete.")
    except Exception as e:
        logger.warning(f"Error getting rail static data: {e}")

    try:
        logger.info("Downloading bus static data...")
        conn = http.client.HTTPSConnection('api.wmata.com')
        conn.request("GET", "/gtfs/bus-gtfs-static.zip?%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        
        with open(BUS_OUTPUT_PATH, "wb") as f:
            f.write(data)
        conn.close()

        logger.debug("Extracting bus data...")
        with ZipFile(BUS_OUTPUT_PATH, 'r') as zObject:
            # Extracting all the members of the zip 
            # into a specific location.
            zObject.extractall(path=BUS_OUTPUT_DIR)

        logger.debug("Bus static data complete.")
    except Exception as e:
        logger.warning(f"Error getting rail static data: {e}")