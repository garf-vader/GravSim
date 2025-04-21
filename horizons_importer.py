# this code can be called as function by other programmes to import the position and velocity of solar system objects
# code is slow and inefficient but doesnt matter because the API call is infinitely slower than my regex
# function should be called extremely rarely, only to populate txt file and then never again

# Nasa Horizons API is terrible and does not return a useful json, so I have to use regex
# Extremely likely to break if Nasa changes the API

import requests
import json
import re


def importer(body):
    response_API = requests.get(
        f"https://ssd.jpl.nasa.gov/api/horizons.api?COMMAND='{body}'&CENTER='500@0'&OBJ_DATA='YES'&MAKE_EPHEM='YES'&EPHEM_TYPE='VECTORS'&START_TIME='2023-12-04'&STOP_TIME='2023-12-05'&STEP_SIZE='1%20d'&QUANTITIES='2'"
    )

    data = response_API.text
    parse_json = json.loads(data)
    # print(parse_json["result"])

    name = (
        re.search("Target body name:(.*) \(", parse_json["result"])
        .group(1)
        .replace(" ", "")
    )

    posvel = re.search("SOE(.*?)EOE", "".join(parse_json["result"]), re.DOTALL).group(0)

    pos = re.search("X =(.*?)VX=", "".join(posvel), re.DOTALL).group(0).replace(" ", "")
    pos = pos.replace("\nVX=", "")
    pos = pos.replace("X=", "")
    pos = pos.replace("Y=", ",")
    pos = pos.replace("Z=", ",")
    pos = pos.split(",")
    pos = [
        float(i) * 1000 for i in pos
    ]  # Horizons uses km and common sense uses meters so I convert

    vel = re.search("VX=(.*?)\n", "".join(posvel), re.DOTALL).group(0).replace(" ", "")
    vel = vel.replace("\n", "")
    vel = vel.replace("VX=", "")
    vel = vel.replace("VY=", ",")
    vel = vel.replace("VZ=", ",")
    vel = vel.split(",")
    vel = [
        float(i) * 1000 for i in vel
    ]  # Horizons uses km/s and common sense uses m/s so I convert

    return name, pos, vel


if __name__ == "__main__":
    # allows function to be called in other python programmes
    importer(body)
