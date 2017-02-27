"""
Script to calculate distance & time between two cities
"""

#!/bin/python2

import requests
import sys

def calc_dist_time(origin, destination):
    """
    Returns distance and time between two cities
    """

    dist = ""
    time = ""

    api_link = "https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&origins={0}&destinations={1}".format(origin, destination)

    # get distance using Google Distance Matrix API
    req = requests.get(api_link)

    result = req.json()

    if result["status"] == "OK":
        if result["rows"][0]["elements"][0]["status"] == "OK":
            dist = result["rows"][0]["elements"][0]["distance"]["text"]
            time = result["rows"][0]["elements"][0]["duration"]["text"]
        else:
            return [result["rows"][0]["elements"][0]["status"]]

    else:
        return [result["status"]]

    return [dist, time]

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print "Please provide origin and destination"
        print "Help: python howlong.py [origin] [destination]\n"
        exit(-1)

    ORI = sys.argv[1]

    DEST = sys.argv[2]

    RES = calc_dist_time(ORI, DEST)

    if len(RES) == 2:
        print RES[0]
        print RES[1]

    else:
        print RES[0]
