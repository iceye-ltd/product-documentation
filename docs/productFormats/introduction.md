# Introduction To SAR Data

## From Satellite to SAR

After an imaging operation has taken place, the recorded radar echo return data is downloaded to one of the terminals in the ICEYE ground station network. From here the process of image formation is performed. The focussing algorithm used depends on the acquisition type. The data is then stored and represented as binary data in a container file format ready for exploitation. 

During the development of the final exploitable product several decisions have to be made about the data representation. At ICEYE we realise that not every format is suitable for every customer or use case so starting in 2022 we will be increasing the range of processing options available. To start with a discussion on the possibilities is warrented so that later we can refer to our current formats in context of the larger landscape. 

## The Tree of Processing Options
There are many steps that have to be considered when converting RADAR pulse data into an exploitable image. Here we will talk about each in turn.

### Sample Arrangement
This is the way the image pixels are aligned as a '*raster*' in the container file. Most GIS viewers will convert the projection for you on your screen. Map-oriented images are larger than range-azimuth images as the rotation to make the image 'north-up' in the container file requires the addition of blank pixels to make the image rectangular. Despite this some users prefer to view the map-oriented product as its map representation with north up and east right makes it easier to use with with paper-based maps.

### Axis Alignment
Another file representation option is the alignment of axes in the binary data. Range-azimuth data can be aligned *shadows down* or *aziumuth down*. Modern GIS viewers can display the data in any representation and easily convert between the two. Scientists using algorithms to exploit the data need to understand the data represention though and it needs to be consistent. Historically imagery intelligence analysts are used to using fine resolution imagery to observe subtle features on small objects of interest. In theses situations it is more important to have a consistent alignment of shadows, multipath and layover of an object than to know where north is.

For large-scale mapping, *azimuth down* easily allows a collection to be extended by concatenating more data to the end of a file.

### Projection
The orientation of the focussed resolution cells in 3D space is the projection. Most commonly this is the slant plane or the ground plane but the projection can have any orientation and even be in the form of a curve or a more complex surface.

There are many reasons for a user prefering one projection over another, usually related to how the imagery will be exploited, but it should be recognised that the slant plane is the most efficient and artefact free focus projection.

### Number of Looks
The number of looks allows a trade to be made between finer resolution and better signal to noise ratio. A single look has the finest resolution. Symetric IPR averages the requied number of looks to make a circular impulse response (circular 2D resolution).

### Complex Samples
Each sample starts life as a complex number. This is usually as an in-phase (*I*) and quadrature (*Q*) pair but it can also be represented as amplitude and phase which saves a user some time if they want to look at only the amplitude data. The process of calculating the amplitude is called '*detection*' which is the 'D' in '*Ground Range Detected*' (GRD). 

The number of shades of grey that a pixel in a SAR image can have is determined by the binary representation of that pixel. As very few pixels are very bright or very dark it is often convenient to store the SAR image data as an unsigned integer - typically uint8 or uint16 format- designed to span the majority of the grey-scale values. This reduces the data size of the image and is useful for most tasks. Sometimes however, it is important to be able to discriminate between different kinds of very bright or dark pixel values (for example man-made objects in trees or ocean wave structure on a calm ocean). In these situations a floating point representation is more useful.

### Container Format
The container and file format defines how the data and associated metadata is stored on disk. It also defines which image viewers know how to read the data. 


<figure>
<img src="../img/image-product-tree-all.png" style="width:100%">
<figcaption align = "center"><em>Figure 1: The SAR Image Tree of Processing Options</em></figcaption>
</figure>




<!-- ## Structure

* Where are all the 'levels' ?
* Foundations :
    * How is SAR Data formed?
    * Important stuff :
        * Radiometric Accuracy and Calibration
        * Spatial Accuracy
            * Resolution
            * Geolocation
                * Doppler Centroid Parameters
                * Rational Polynomial Coefficients
        * Slant to Ground conversion -->
