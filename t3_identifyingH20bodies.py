##################
#File name: 
#Author: Kelsey Herndon
#Affiliation: The University of Alabama in Huntsville
#Date Created: 4/12/2017
#Last Date Modified: 4/12/2017
#Purpose: The purpose of this script is to create water body polygons from mndwi raster
#Dependencies: arcpy
###################

#import dependencies
import arcpy
from arcpy import env
from arcpy.sa import *

#check-out ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

#define workspace
arcpy.env.workspace = r"C:\Users\KHerndon\Desktop\test"

#enable overwriting
arcpy.env.overwriteOutput = True

#define local variables
#define mndwi raster
mndwi = arcpy.env.workspace + "\mndwiBasin.tif"

#Execute Con tool
mndwi_reclass1 = Con (mndwi, 1, "", "VALUE>-.2")

#Save the output
mndwi_reclass1.save(arcpy.env.workspace + "\mndwi_reclass1.tif")

#convert mndwi to polygons representing surface water
#define input raster
inRaster = mndwi_reclass1 
#define where to save the output polygons
outpoly = arcpy.env.workspace + "\h2Opoly.shp"
#define which field on which to perform analysis
field = 'Value'

#Excecute Raster to Polygon
arcpy.RasterToPolygon_conversion(inRaster, outpoly, "SIMPLIFY", field)

#project polygon to same as landsat

print "Water body identification complete."
