# Introduction To SAR Data

## From Satellite to SAR

After an imaging operation has taken place, the recorded radar echo data is downloaded to one of the terminals in the ICEYE ground station network where the images are formed. The focussing algorithm varies depending on the acquisition type. The data is then stored and represented as binary data in a container file format ready for exploitation. 
When producing different forms of exploitable products, several decisions have to be made about the data representation. At ICEYE we realise that not every format is suitable for every customer or use case, so starting in 2022 we will be increasing the range of processing options available. This section includes a discussion of format options so that later we can refer to our current formats in context of the larger landscape.

<figure markdown>
![placeholder](img/port.gif){width="600"}
<figcaption align = "center"><em>Figure 8: The Port of Rotterdam on three consecutive days.</em></figcaption>
</figure> 

## The Tree of Processing Options
There are many steps that have to be considered when converting RADAR pulse data into an exploitable image. Here we will talk about each in turn.
<figure>
<img src="../img/Image-product-tree-all.png" style="width:100%">
<figcaption align = "center"><em>Figure 1: The SAR Image Tree of Processing Options</em></figcaption>
</figure>

### Sample Arrangement
This is the way the image pixels are aligned as a *raster* in the container file. Most GIS viewers will convert the projection for you on your screen. Map-oriented images are larger than range-azimuth images as the rotation to make the image 'north-up' in the container file requires the addition of blank pixels to make the image rectangular. Map projection layouts are often projected to a single elevation surface; thus, they lack the geometric fidelity of range-azimuth images. They also can impart flipped terrain-perception effects in which mountains appear to be valleys and valleys appear elevated. Despite this, some users prefer the map-oriented product because its map representation with north up can be directly used with paper-based maps without any rotations.


### Axis Alignment
Another file representation option is the alignment of axes in the binary data. Range-azimuth data can be aligned *shadows down* or *azimuth down*. Modern GIS viewers can display the data in either representation and easily convert between the two. Scientists using algorithms to exploit the data need to understand the data representation thought. Historically, imagery intelligence analysts require fine resolution imagery to observe subtle features on small objects of interest. In these situations it is more important to have a consistent alignment of shadows, multipath and layover of an object than to  have North ‘up’.
For large-scale mapping, *azimuth down* easily allows a collection to be extended by concatenating more data to the end of a file.

### Projection Suface
The focussed SAR resolution cells are fit to a projection surface. Most commonly this is the slant plane,  the ground plane or an ellipsoid surface, but the projection surface can have any orientation and even be an inclined plane, a curve or the topographic surface.

There are many reasons for a user preferring one projection surface over another. This is usually related to how the imagery will be exploited, but it should be recognised that the slant plane is the most efficient and artefact-free focus projection surface.


### Number of Looks
The multi-look process reduces resolution in order to reduce the speckle in the image. A single look has the finest resolution which may be different in range and azimuth. *Symmetric IPR* is the term used when the resolution (sometimes referred to as IPR or *impulse response*) is symmetrical in range and azimuth.

### Complex Samples
Each sample starts life as a complex number. This is usually as an in-phase (*I*) and quadrature (*Q*) pair, but it can also be represented as amplitude and phase, which saves a user some time if they want to look at only the amplitude data. The process of calculating the amplitude from I and Q is called *detection*, which is the *D* in *Ground Range Detected* (GRD). 

The number of shades of grey that a pixel in a SAR image can have is determined by the binary representation of that pixel. As very few pixels are very bright or very dark it is often convenient to store the SAR image data as an unsigned integer - typically uint8 or uint16 format- designed to span the majority of the grey-scale values. This reduces the data size of the image and is useful for most tasks. Sometimes however, it is important to be able to discriminate between different kinds of very bright or dark pixel values (for example man-made objects in trees or ocean wave structure on a calm ocean). In these situations, a floating-point representation is more useful as it has a larger bit depth..


### Container Format
The container and file format defines how the data and associated metadata is stored on disk. It also defines which image viewers know how to read the data. 
