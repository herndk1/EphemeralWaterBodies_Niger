##################
#File name: 
#Author: Kelsey Herndon
#Affiliation: The University of Alabama in Huntsville
#Date Created: 4/12/2017
#Last Date Modified: 4/12/2017
#Purpose: The purpose of this script is to download the desired bands of a Landsat Tile from Amazon Web Services
#Dependencies: arcpy, urllib2
###################

#import dependencies
import urllib2
import arcpy

#enable overwriting
arcpy.env.overwriteOutput = True

#define the workspace
arcpy.env.workspace = r"C:\Users\KHerndon\Desktop\test"

#download band 3
    #define url of image band3
urlB3 = 'http://landsat-pds.s3.amazonaws.com/L8/191/049/LC81910492015086LGN00/LC81910492015086LGN00_B3.TIF'
file_name = urlB3.split('/')[-1]
u = urllib2.urlopen(urlB3)
f = open(file_name, 'wb')

response = urllib2.urlopen(urlB3)  

    #open a file and pass data into it
outfile = arcpy.env.workspace + "\lsB3.tif"
with open(outfile, 'wb') as output: 
    output.write(response.read())

print "band 3 download complete"

#download band 4
    #define url of image band
urlB4 = 'http://landsat-pds.s3.amazonaws.com/L8/191/049/LC81910492015086LGN00/LC81910492015086LGN00_B4.TIF'
file_name = urlB4.split('/')[-1]
u = urllib2.urlopen(urlB4)
f = open(file_name, 'wb')

response = urllib2.urlopen(urlB4)  

    # open a file and pass data into it
outfile = arcpy.env.workspace + "\lsB4.tif"
with open(outfile, 'wb') as output: 
    output.write(response.read())

print "band 4 download complete"

#download band 5
    #define url of image band
urlB5 = 'http://landsat-pds.s3.amazonaws.com/L8/191/049/LC81910492015086LGN00/LC81910492015086LGN00_B5.TIF'
file_name = urlB5.split('/')[-1]
u = urllib2.urlopen(urlB4)
f = open(file_name, 'wb')

response = urllib2.urlopen(urlB5)  

    # open a file and pass data into it
outfile = arcpy.env.workspace + "\lsB5.tif"
with open(outfile, 'wb') as output: 
    output.write(response.read())

print "band 5 download complete"

#download band 6
    #define url of image band
urlB6 = 'http://landsat-pds.s3.amazonaws.com/L8/191/049/LC81910492015086LGN00/LC81910492015086LGN00_B6.TIF'
file_name = urlB6.split('/')[-1]
u = urllib2.urlopen(urlB6)
f = open(file_name, 'wb')

response = urllib2.urlopen(urlB6)  

    # open a file and pass data into it
outfile = arcpy.env.workspace + "\lsB6.tif"
with open(outfile, 'wb') as output: 
    output.write(response.read())

print "band 6 download complete"

#close the webpage
response.close()

print "All bands downloaded"
