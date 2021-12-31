

## Overview
Single Look Complex (SLC) images have the highest fidelity of all the image products being only one step removed from the original RADAR collected data. They retain all the original sensor measurements and are free from interpolation artefacts or projection issues. A small concession is made with the default SLC product in that the dynamic range of the complex numbers is reduced to make image sizes more manageable. The only reason not to use SLC products is when human wetware is involved in the expoitation as the slant plane projection and radar phenomenology can be difficult to understand without skill and experience. For this reason SLC images are usually used for automated processing and advanced exploitation.

SLC products are most frequently used to expoit phase information, primarily in interferometric applications, or by users who prefer lower level processing in order to implement their own processing chains. The SLC product can be orthorectified using both commercial and free specialized SAR software tools such as the European Space Agency (ESA) Sentinel Application Platform (SNAP)[@snap]. 

## Geometry

Scenes are stored in the satellite image acquisition geometry (AKA the *slant plane*). The image coordinate system is centred on the zero-Doppler (time of closest approach)  SAR coordinates and are arranged in the slant-range-by-azimuth imaging plane. The pixels are spaced equidistant in azimuth (according to the inverse of the pulse repetition frequency) and in slant range (according to the range sampling frequency). Each image pixel is stored with in-phase I and quadrature Q components and therefore, contains both amplitude and phase information.  

## Looks
As the name suggests, SLC images have only a single look. This means that in most cases the impulse response function (the shape of a single, isolated radar-bright object in the radar image) is asymmetrical with azimuth resolutions being smaller (finer).

## Binary Representation

SLC images are stored as binary matrices in an HDF5 file container[@hdf]. Real and imaginary components  are stored separately, using either signed 16 bit integers or IEEE-754 single precision 32-bit floating point format (the version used is annotated in the `sample_precision` metadata element).  It is assumed that all pixels are valid, unless marked with a NaN (Not a Number) value.  

The structure of the binary data is shown in Figure 1. Each row of the matrix is a single range line (often called a *range profile* by RADAR engineers) of the image with increasing range preceding from lower indices to higher indices (left to right in Figure 1). Early row indices in the matrix correspond to early pulses and later rows correspond to later pulses (top to bottom in Figure 1). It is important to recognise that image viewing software needs to take into account the matrix configuration as viewing the matrix as it is stored may result in the image being reflected in either dimension depending on right/left looking and ascending/descending.

<figure>
<img src="../img/pixel-representation.png" style="width:100%">
<figcaption align = "center"><em>Figure 1: The Binary Representation of SLC images</em></figcaption>
</figure>

## Shadows Down
Some analysts or software algorithms prefer to process SLC imagery with increasing range aligned to increasing row index - often called **shadows down**. This approach is usually used for fine resolution SAR imaging systems where its more important for target recognition to have a consistent shadow and layover alignment than it is to know where north is. **Shadows Down** imagery can be provided by request.

## HDF5 Container
The SLC HDF5 container contains metadata associated with the collection in its header structure. The metadata is described [in the Metadata section of this site](metadata.md). HDF and metadata tags can easily be found using a Python interpreter and the commands : 

```python3 
import h5py
f = h5py.File("<filename.h5>")
for key in f.keys():
print(f[key])
```

## Sensor Independent Complex Data
In a welcome move to harmonize the processing of SAR imagery provided by different vendors, the US National Geospatial-Intelligence Agency (NGA) developed a sensor agnostic format called *sensor independent complex data* (SICD). The idea behind this format is that it is carefully designed to remove any sensor specific parameters, providing complex image data in the same format regardless of processing algorithm or collection strategy. In theory, any algorithm that uses SICD will work on SAR imagery from any SAR vendor. 

**SICD** data is stored in a NITF (National Imagery Transmission Format[@nitf]) container and will only work with GIS viewers and algorithms that know how to handle this type of dataset. As this format is not as well known as hdf5 it is currently only available by request.

## SLC in Context
Figure 2 provides a useful summary of SLC images in the context of the processing options available with the red line highlighting the decisions made during product production. 



<figure>
<img src="../img/SLC-Image-product-tree.png" style="width:100%">
<figcaption align = "center"><em>Figure 2: The Processing Steps and Implementation Considerations for ICEYE SLC images</em></figcaption>
</figure>



## References
\bibliography