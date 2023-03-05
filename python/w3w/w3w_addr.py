#!/usr/bin/python3
import sys
import what3words
import json

gps_info = sys.stdin.readlines()
data = json.loads(" ".join(gps_info))

geocoder = what3words.Geocoder("3DBD7L0X")

age = data.get("age", 9999)
orig_lat = data.get("latitude",0)
orig_lng = data.get("longitude",0)

lat = round(orig_lat, 4)
lng = round(orig_lng, 4)

print(f"{orig_lat}, {orig_lng} ({age})", file=sys.stderr)
print(f"{lat}, {lng}", file=sys.stderr)

words = "gps.has.no-signal"
if lat != 0 and lng != 0:
    res = geocoder.convert_to_3wa(what3words.Coordinates(lat, lng))
    words = res['words']

print(f"///{words}")
