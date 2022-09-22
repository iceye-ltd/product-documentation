# The ORTHO product 

Because of the way we acquire and process our data, the amplitude image from raw SLC data appears completely distorted. GIS application require correct "location" of our pixels in order to do precise measurements. We account for three components to these distortions: the aquisition geometry, the curvature of the earth and the local toplogy. Hence the necessity for an orthorectified product. 

## What is Orthorectification?

Orthorectification is the process of compensating for three component of distortion. We will have to calculate how much we "move" our pixels in order to correct for thoses. 
First, a correction of the distrotions caused by the sensor/scene geometry. SAR satellites observe their target broadside at an angle which cause a 'tilt' and 'strech' of the iamge when layed on a surface representing the earth's surface, for example. Pixels are moved to so called horizontal coordinates, simply at the correct lattitude and longitude coordinates in WGS84 referencial. Our [GRD product](grd.md) already correct for the satellite geometry and the horizontal positions in WGS84 coordinates, remain the earth curvature and the local topology.
Second we have to account for the global datum of the earth which is mathematically modeled. We evaluation the elevation from the ellipsoid surface model (here EGM16, in WGS84) for each pixels.
Finally we evaluated add the local elevation from a Digital Evelation Model (DEM). Accuracy of the DEM data is an important factor to properly interpolate the pixels positions.
The results is a 3D coordinates for each pixels which can be used to project the image plane. 

### DEM
Currently we can provide orthorectified imagery from the following Digital Elevation models:
 * Copernicus DEM GLO-30 
 * Copernicus DEM GLO-90 
 * NASA DEM version 1
 * ASTER GDEM version 3
 Terrain projection is performed with one the chosen DEM using GDAL gdalwarp tool. The new image is stored as a Geotif just like our GRD product. We produce a new XML file from the GRD one with extra field describing the DEM used for orthorectification. 
