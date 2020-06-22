# zipcodes

Fairly simply script that was made to retrieve lat, lon from a zipcode.\
The data itself may be incomplete?\
(full-zips.csv: contains 43,192 lines - according to wikipedia, the US has 41,702 zip codes as of Oct 2019) - it was retrieved from opendatasoft.  I did find some missing zipcodes in the data which I added manually where possible.\
with the following changes:

Changes to the full-zips.csv\
  Added some zip codes that I found were missing to the data\
  Remove a trailing comma in each line, including header line which was resulting in\
    an empty key/value pair when reading the csv into python.\
  Rename the DST flag to "DST_Flag" from "Daylight savings time flag", which seemed\
    an odd name for a fieldname value to me.

In either event:

coords_from_zip returns a tuple containing (lat,lon)

get_all_data returns the following in a dict:\
  Zip:        The zip code\
  City:       The city\
  State       The state\
  Latitude:   The latitude\
  Longitude:  The longitude\
  Timezone:   Timezone difference from UTC\
  DST_Flag:   Not sure what this is, maybe if the location observes DST,\
              I've only observed 1's and 0's here, so this makes sense\
  geopoint:   a comma-separated string value representing the geo point of (lat,lon)
  
Run as __main__ for testing/demo and enter the zipcode you are searching for when prompted.
