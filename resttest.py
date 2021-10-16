#rest services tool.  written in python3

import json
import requests

#the base url for the rest end point
url = "http://gisdata.dot.ca.gov/arcgis/rest/services/Highway/SHN_Postmiles_Tenth/MapServer/0/query?where=Route%3D41+and+county%3D%27FRE%27+and+District%3D6&text=&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&relationParam=&outFields=*&returnGeometry=true&returnTrueCurves=false&maxAllowableOffset=&geometryPrecision=&outSR=&returnIdsOnly=false&returnCountOnly=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&gdbVersion=&returnDistinctValues=false&resultOffset=&resultRecordCount=&f=json"

#http://gisdata.dot.ca.gov/arcgis/rest/services/Highway/SHN_Postmiles_Tenth/MapServer/0/query?where=Route%3D41+and+county%3D%27FRE%27+and+District%3D6&text=&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&relationParam=&outFields=*&returnGeometry=true&returnTrueCurves=false&maxAllowableOffset=&geometryPrecision=&outSR=&returnIdsOnly=false&returnCountOnly=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&gdbVersion=&returnDistinctValues=false&resultOffset=&resultRecordCount=&f=json

response = requests.get(url)

if response.status_code==200:
    print("the status code was 200")

    #turn data returned to dictionary
    jsonstr = response.json()
    for feat in jsonstr['features']:
        print("Route  "+str(feat['attributes']['Route'])+"   County  "+feat['attributes']['County']+"   District "+str(feat['attributes']['District']))
else :
    print("the status code was "+str(response.status_code))

#



