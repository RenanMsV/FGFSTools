def get_FR24_nearplanes (coords) :
    import urllib.request
    import json

    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

    # SP Area
    #lat_min = -16
    #lat_max = -27
    #lon_min = -51
    #lon_max = -40

    bounds = "{},{},{},{}".format(coords[5], coords[3], coords[2], coords[4])
    print(bounds + "\n")
    url = "http://data-live.flightradar24.com/zones/fcgi/feed.js?bounds=" + bounds + "&faa=1&mlat=1&flarm=1&adsb=1&gnd=1&air=1&vehicles=0&estimated=0&maxage=900&gliders=0&stats=1&array=1"
    headers={'User-Agent':user_agent,} 
    print(url+"\n")
    request=urllib.request.Request(url,None,headers) #The assembled request
    response = urllib.request.urlopen(request)
    data = response.read() # The data u need
    print(data)
    print("\n")
    return json.loads(data.decode('utf8'))

def get_coords_bounding_box (lat, lon, dist):
    import math
    global MIN_LAT, MAX_LAT, MIN_LON, MAX_LON, R, radDist, degLat, degLon, radLat, radLon, minLat, maxLat, minLon, maxLon, deltaLon
    if dist < 0:
        return "[Error - get coords bounding box] Illegal Arguments"
    MIN_LAT = deg2rad(-90)
    MAX_LAT = deg2rad(90)
    MIN_LON = deg2rad(-180)
    MAX_LON = deg2rad(180)
    R = 6378.1
    radDist = dist / R
    degLat = lat
    degLon = lon
    radLat = deg2rad(degLat)
    radLon = deg2rad(degLon)
    minLat = radLat - radDist
    maxLat = radLat + radDist
    minLon = None
    maxLon = None
    deltaLon = math.asin(math.sin(radDist) / math.cos(radLat))
    if (minLat > MIN_LAT and maxLat < MAX_LAT):
        minLon = radLon - deltaLon
        maxLon = radLon + deltaLon
        if (minLon < MIN_LON) :
            minLon = minLon + 2 * math.pi
        if (maxLon > MAX_LON) :
            maxLon = maxLon - 2 * math.pi
    else:
        minLat = max(minLat, MIN_LAT)
        maxLat = min(maxLat, MAX_LAT)
        minLon = MIN_LON
        maxLon = MAX_LON
    return [lat,lon,rad2deg(minLon),rad2deg(minLat),rad2deg(maxLon),rad2deg(maxLat)]

def deg2rad(number):
    import math
    return number * (math.pi / 180)
def rad2deg(number):
    import math
    return (180 * number) / math.pi

def main():
    coords = get_coords_bounding_box(-22.907104,-47.063240, 20) # lat , lon , box distance in km
    get_FR24_nearplanes(coords)

if __name__ == "__main__":
    main()

'''
JSON - Acquire flight information on flight from Flightradar 24!
2016-02-08 00: 20 [Programming] [JSON]
     Send by LINE
※ This article was posted more than 2 years ago, information may be old.
Good evening.

It is a memorandum on how to acquire the information of the aircraft currently in flight from the website Flightradar 24.com which can check the operational status of the aircraft in real time by specifying the area.

For the airport information list and airline list acquisition, please refer to the previous and previous articles.

Get airport information list from Ruby - Flightradar 24!
Get airline information list from Ruby - Flightradar 24!
0. Prerequisites
Since the data to be acquired is JSON format, it has basic knowledge of JSON.
Not all flights can be acquired.
(Information may not be provided in areas where there is no volunteer (so-called Feeder) that provides the signal of the received ADS-B etc. to the Flightradar 24, when the signal transmitted from the aircraft is weak, etc. In some cases, information is not originally transmitted There are obviously no aircraft)
The method to be introduced below is to acquire by yourself using a web browser.
(We actually create and use Ruby scripts)
1. Obtain the load balancer server name
Access the URL http://www.flightradar24.com/balance.json in the browser to obtain JSON data.

The following JSON data can be acquired.
If there are multiple load balancers, multiple load balancers can be acquired. 1000 is like priority, and if there are two or more, it is supposed to add 1000 in total.

1
{"data.flightradar24.com": 1000}
2. Acquisition of flight information
Access the following URL in the browser: http: // [load_balancer] /zones/fcgi/feed.js?bounds= [bounds] & adsb = 1 & mlat = 1 & faa = 1 & flarm = 1 & estimated = 1 & air = 1 & gnd = 1 & vehicles = 1 & gliders = 1 & array = 1 Get JSON data.

load_balancer is the server name of the load balancer obtained in the previous section.
bounds is for setting the area to be acquired (latitude (north), latitude (south), longitude (west), latitude (east)). If it is not set, all data are subject.
(E.g., 35.57, 35.38, 132.96, 133.20)
adsb = 1, mlat = 1, faa = 1, flarm = 1, estimated = 1 is a setting for receiving ADS-B, MLAT, FAA, FLARM, Estimated signal.
Air = 1, gnd = 1, vehicles = 1, gliders = 1 are settings (?) for receiving signals of aircraft (overhead?), aircraft (ground?), ground traveling cars, and gliders.
array = 1 is an option to get in an array within an aircraft item.
3. Confirmation of acquisition information
For the following, please see http://data.flightradar24.com/zones/fcgi/feed.js?bounds=35.6, 34.2, 131.55, 133.55 & adsb = 1 & mlat = 1 & faa = 1 & flamm = 1 &estimated= 1 & air = 1 & gnd = 1 & vehicles = 1 & gliders = 1 & Data acquired in 1. (It is shaping for easy viewing)

{
  "full_count": 7841,
  "version": 5,
  "copyright": "The contents of this file of Flightradar 24 AB, use modifying or redistributing the data without the prior written permission of Flightradar 24 AB is not allowed and may result in prosecutions. ",
  "aircraft": [
    "" HND "," NGS "," JL 609 "," FB "," F - RJOH 1 "," B - 763 "," JA 657 J ", 1454302287, , 0, 0, "JAL 609", 0],
    "" HND "," FUK "," NH 253 "," FB "," FB "," FB "," F 8 "," 8 D 13 F 4 "," 86 D 2 E ", 34.5986, 132. 8036, 255, 40000, 356," 1776 "," F-RJOH 1 "," B 788 "," JA 818 A ", 1454302287, , 0, 0, "ANA 253", 0],
    "" 8 J 1438 d "," 850 E 15 ", 34.5947, 131.7789, 236, 35425, 308," 0464 "," T-MLAT 5 "," B 735 "," JA 305 K ", 1454302289," SDJ "," FUK "," NH 1276 " , 0, -1920, "", 0]
  ]
}
Information on aircraft in flight is within the aircraft item, and the part surrounded by [and] is one piece of information.

The meaning of each item is as follows. (In order from the left)

  "8b13efc" # 0: ID
  "862 D 94" # 1: SSR mode S code
  34.2681 # 2: Latitude (unit: degree)
  132.5959 # 3: Longitude (unit: degree)
  252 # 4: Progress direction (unit: degree (degree), 0 degree clockwise in the north)
  40000 # 5: Flight altitude (unit: feet)
  600 # 6: Speed ​​(Unit: knot)
  "2010" # 7: squawk (identification signal 4 digit set in the transponder)
  "F-RJOH 1" # 8: Receiving radar
  "B763" # 9: Aircraft type
  "JA657J" # 10: Flight number (ICAO code)
  1454302287 # 11: Time (Unix time)
  "HND" # 12: Departure airport (IATA code)
  "NGS" # 13: Arrival Airport (IATA Code)
  "JL 609" # 14: Flight number (IATA code)
  0 # 15:?
  0 # 16:?
  "JAL 609" # 17: Call sign (ICAO code)
  0 # 18:?
4. Reference site
Cykey's blog - Analyzing Flightradar 24's internal API structure
Although it hits to some extent about the method of acquiring real time flight information when searching the Web, the information is old about 90%. (The above site also becomes informative but contents are old)

We implement this mechanism in Ruby (designate the area including your home) and use it. (In fact, it is acquired & recorded by periodically running. In some cases, we plan to tweet if the aircraft intrudes into the designated area)

Receiving the ADS - B signal is not so difficult, so I feel that I can become a Feeder. (If you feel like it)

that's all.
'''