from configparser import ConfigParser

# Load Config

cp = ConfigParser()
cp.read('config.ini')

api_key = cp.get("api", "api_key")
org_id = cp.get("meraki", "org_id")

config = {"api_key": api_key, "org_id": org_id}
