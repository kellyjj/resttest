#rest services tool.  written in python3
#kjj 10-20-21  added exmample of using parameters in a querry.

import json
import requests

#the base url for the rest end point
url = "http://gisdata.dot.ca.gov/arcgis/rest/services/Highway/SHN_Postmiles_Tenth/MapServer/0/query?where=Route%3D41+and+county%3D%27FRE%27+and+District%3D6&text=&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&relationParam=&outFields=*&returnGeometry=true&returnTrueCurves=false&maxAllowableOffset=&geometryPrecision=&outSR=&returnIdsOnly=false&returnCountOnly=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&gdbVersion=&returnDistinctValues=false&resultOffset=&resultRecordCount=&f=json"
url2 = "http://gisdata.dot.ca.gov/arcgis/rest/services/Highway/SHN_Postmiles_Tenth/MapServer/0/query"

myparams = {"f":"json","where":"Route=41 and county='FRE' and District=6","outFields":"*","spatialRel":"esriSpatialRelIntersects"}
#the request object is where we call get/put/post of what ever url we are working with  url is the end point we are access.  the url will have to 
#be formated for what ever it is we are dealing with
response = requests.get(url2,params=myparams)

print(response.url)

#standard response code cehck.  this is the normal 200, 404, or whatever
if response.status_code==200:
    print("the status code was 200")

    #turn data returned to dictionary
    #under the response object we have the method json()  this will return to use a object [dicstionary in python] for us to do whatever we want
    jsonstr = response.json()

    #in this case, we are iterating through the features object of the json we got returned.  it could be what ever.  need to check json to see what 
    #to call here.  treat it like a array/dictionary.
    for feat in jsonstr['features']:
        print("Route  "+str(feat['attributes']['Route'])+"   County  "+feat['attributes']['County']+"   District "+str(feat['attributes']['District']))

#we are going to filter down the results.  1st grab the sub object we want
    thefeatures = jsonstr['features']

    #print(thefeatures)
else :
    print("the status code was "+str(response.status_code))

#



