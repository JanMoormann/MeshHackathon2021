import requests
from datetime import datetime
import xml.dom.minidom

def getTripSSB(longtitudeStart,latitudeStart,longtitudeDes,latitudeDes,depArrTime=None,turnDescription="true",trackSections="true",legProjection="true",intermediateStops="true",fares="true"):

    #standart variables
    url = "http://efastatic.vvs.de/kleinanfrager/trias"
    requestorRef="" #removed
    currentTime = datetime.now().isoformat()

    #set default of depArrTime
    if depArrTime == None:
        depArrTime = currentTime

    #concertination
    payload=f"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\r\n<Trias version=\"1.1\" xmlns=\"http://www.vdv.de/trias\" xmlns:siri=\"http://www.siri.org.uk/siri\">\r\n\t<ServiceRequest>\r\n\t\t<siri:RequestTimestamp>{currentTime}</siri:RequestTimestamp>\r\n\t\t<siri:RequestorRef>{requestorRef}</siri:RequestorRef>\r\n\t\t<RequestPayload>\r\n\t\t\t<TripRequest>\r\n\t\t\t\t<Origin>\r\n\t\t\t\t\t<LocationRef>\r\n\t\t\t\t\t\t<GeoPosition>\r\n\t\t\t\t\t\t\t<Longitude>{longtitudeStart}</Longitude>\r\n\t\t\t\t\t\t\t<Latitude>{latitudeStart}</Latitude>\r\n\t\t\t\t\t\t</GeoPosition>\r\n\t\t\t\t\t</LocationRef>\r\n\t\t\t\t\t<DepArrTime>{depArrTime}</DepArrTime>\r\n\t\t\t\t</Origin>\r\n\t\t\t\t<Destination>\r\n\t\t\t\t\t<LocationRef>\t\t\t\t\t\t\r\n\t\t\t\t\t\t<GeoPosition>\r\n\t\t\t\t\t\t\t<Longitude>{longtitudeDes}</Longitude>\r\n\t\t\t\t\t\t\t<Latitude>{latitudeDes}</Latitude>\r\n\t\t\t\t\t\t</GeoPosition>\r\n\t\t\t\t\t</LocationRef>\r\n\t\t\t\t</Destination>\r\n\t\t\t\t<Params>\r\n\t\t\t\t\t<IncludeTurnDescription>{turnDescription}</IncludeTurnDescription>\r\n\t\t\t\t\t<IncludeTrackSections>{trackSections}</IncludeTrackSections>\r\n\t\t\t\t\t<IncludeLegProjection>{legProjection}</IncludeLegProjection>\r\n\t\t\t\t\t<IncludeIntermediateStops>{intermediateStops}</IncludeIntermediateStops>\r\n\t\t\t\t\t<IncludeFares>{fares}</IncludeFares>\r\n\t\t\t\t</Params>\r\n\t\t\t</TripRequest>\r\n\t\t</RequestPayload>\r\n\t</ServiceRequest>\r\n</Trias>"
    headers = {
    'Content-Type': 'text/xml',
    'User-Agent': 'Fiddler'
    }

    #api call
    response = requests.request("POST", url, headers=headers, data=payload)

    #format xml file
    dom = xml.dom.minidom.parseString(response.text)
    xmlResponse = dom.toprettyxml()

    #return xml
    return xmlResponse

#run
with open('trip.xml',"w",encoding="UTF-8") as f:
    longtitudeStart="9.113192"
    latitudeStart="48.726900"
    longtitudeDes="9.18445"
    latitudeDes="48.78025"

    f.write(getTripSSB(longtitudeStart,latitudeStart,longtitudeDes,latitudeDes))
    print("done")
