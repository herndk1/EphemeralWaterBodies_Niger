##################
#File name: 
#Author: Kelsey Herndon
#Affiliation: The University of Alabama in Huntsville
#Date Created: 4/12/2017
#Last Date Modified: 4/12/2017
#Purpose: The purpose of this script is to calculate ndvi, ndti, and mndwi for a Landsat scene and clip the indices to the study area
#Dependencies: arcpy
###################

#import dependencies
import arcpy
from arcpy import env
from arcpy.sa import *

#check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension('Spatial')

#set workspace
arcpy.env.workspace = r"C:\Users\KHerndon\Desktop\test"

#enable overwriting
arcpy.env.overwriteOutput = True

#define local variables
basin = r"C:\Users\KHerndon\Desktop\final_project\basin2\basin2.shp" #provided with zipped scripts
Band3 = arcpy.env.workspace + "\lsB3.tif"
Band4 = arcpy.env.workspace + "\lsB4.tif" 
Band5 = arcpy.env.workspace + "\lsB5.tif"
Band6 = arcpy.env.workspace + "\lsB6.tif"

#Calculating Indices
#calculate mndwi
print 'Calculating MNDWI.'
mndwi = Float(Raster(Band3)-Raster(Band6))/Float(Raster(Band3)+Raster(Band6))

#calculate ndti
print 'Calculating NDTI.'
ndti = Float(Raster(Band4)-Raster(Band3))/Float(Raster(Band4)+Raster(Band3))

#calculate ndvi
print 'Calculating NDVI.'
ndvi = Float(Raster(Band5)-Raster(Band4))/Float(Raster(Band5)+Raster(Band4))

#Clipping indices to basin and saving 
#clip mndwi to basin
print 'Clipping MNDWI to basin.'
mndwiBasin = ExtractByMask (mndwi, basin)
#save mndwi clipped to basin
mndwiBasin.save(r"C:\Users\KHerndon\Desktop\test\mndwiBasin.tif")

#clip ndti to basin
print 'Clipping NDTI to basin.'
ndtiBasin = ExtractByMask (ndti, basin)
#save ndti clipped to basin
ndtiBasin.save(r"C:\Users\KHerndon\Desktop\test\ndtiBasin.tif")

#clip ndvi to basin
print 'Clipping NDVI to basin.'
ndviBasin = ExtractByMask (ndvi, basin)
#save ndvi clipped to basin
ndviBasin.save(r"C:\Users\KHerndon\Desktop\test\ndviBasin.tif")

print "Finished calculating indices and clipping to study area."
