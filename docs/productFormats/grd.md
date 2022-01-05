
## 'Ground Range Detected' - 😵‍💫?
Most current SAR providers sell an image that contains the words '*Ground*', '*Range*' and '*Detected*', often abreviated to *GRD*. Over the last two years of trying to make SAR more accessible we have come to the realization that only electronic engineers understand what the combination of these words really mean. The words 'ground-range' suggests that these images are projected onto some representation of the ground. If you didn't realise that SAR images are collected in the 'slant-range' plane then you might think "well yeah - of course". 
 
The term '*detected*' though is very strange and might lead some users to think that some sort of target detection or post processing has been applied to the image. The term '*detection*' is an old electronic engineering term used when signal processing was mainly performed on oscilloscopes. From [[@detection]]:

!!! quote 

    **detection**, in electronics, the process of rectifying a radio wave and recovering any information superimposed on it; it is essentially the reverse of modulation (q.v.).
 
 So thats clear 😐.The term *detection* when applied to SAR images is the process of converting the complex numbers that make up the single-look *complex* image into amplitude only values. This is usually performed to reduce the size of the image by throwing away the half of the image that stores phase information because most visual exploiters don't care about this so much.  At ICEYE we like to use 'plain english' so we usually refer to this as the **amplitude** image. We struggle to shake off our legacy though so don't mind if customers prefer GRD and we still keep the acronym in some of our product filenames for compatibility reasons (although this is likely to change in the future).

## Amplitude Image Description

Amplitude images represent focused SAR data that has been detected and (usually) multi-look processed and projected to the ground plane using an Earth ellipsoid model.  The image coordinates are oriented along the flight direction and ground range (figure 1).  The pixel spacing is equidistant in azimuth and in ground range.  Ground range coordinates are the slant range coordinates projected onto the ellipsoid of the Earth. For this projection the WGS84 reference ellipsoid (table 1) is used and an averaged fixed value of terrain height is used. This makes the ellipsoid surface closer to the true ground surface and reduces (but doesn't eliminate) pixel location errors. The mean ellipsoid height used is annotated in the `avg_scene_height` metadata element.

!!! Tip
    For an explanation of why see [Terrain Height](../geospatialAccuracy#terrain-height) in the 'Geospatial Accuracy' section under 'Foundations'.


<figure markdown>
|Ellipsoid Reference | Semi Major Axis | Semi Minor Axis | Inverse Flattening |
|--------------------|----------------|------------------|--------------------|
|WGS84               | 6378137.0 m    | 6356752.314245 m | 298.257 223 563    |
<figcaption align = "center"><em>Table 1 : WGS84 Reference Ellipsoid used in ICEYE Amplitude images</em></figcaption>
</figure>


Pixel values represent a scaled aamplitude. The resulting product has approximately circular spatial resolution and square pixel spacing. Additionally, an incidence angle dependence in range, calculated using the ellipsoidal Earth model has been applied to facilitate the conversion of radar brightness to backscatter intensity. This is explained in more detail in Section ?

One advantage of this product is that no image rotation to a map coordinate system has been performed and interpolation artefacts are thus avoided. This product is useful for applications that only require amplitude information and if geocoding or orthorectification is to be applied by the user, or for applications where geocoding is not required. 

To assist users that require geocoded imagery with minimal interpolation artefacts, ICEYE amplitude image products are tagged with ground control points (GCP) and rapid positioning capability polynomial coefficients (RPC’s). These allow precise geospatial exploitation using freely available tools such as QGIS[@qgis] or GDAL[@gdal].

<figure>
<img src="../img/pixel-representation-grd.png" style="width:100%">
<figcaption align = "center"><em>Figure 1: The Binary Representation of Amplitude Images</em></figcaption>
</figure>

## Binary Representation

The 'digital numbers' in the image data layer $DN_{GRD}$ of amplitude SAR products are stored in a GeoTIFF file format using unsigned 16 bit integer representation along with a combination of commonly used and specifically defined GeoTIFF tags. GeoTiff files are readable with standard image processing and GIS software tools.

Different imaging modes and different incidence angles may have a native sample spacing in the slant range that is not square and so square sample spacing and a circular impulse response function in the ground plane is achieved either by varying the transmitted bandwidth or by applying multi-looking during the slant to ground transformation and detection process. 

Typically, the conversion from complex samples to amplitude only samples is performed as

$$
|DN_{SLC}|^2 = (I^2 + Q^2)
$$

with $I^2$ and $Q^2$ representing the real and imaginary amplitude of the complex backscatter.

For amplitude image scenes, a conversion to  $\sigma_0$ has been already applied using an incidence angle $\theta$ that is calculated from the ellipsoidal Earth model:

$$
|DN_{GRD}|^2 =|DN_{SLC}|^2\sin(\theta)
$$

Ellipsoid parameters and metadata tags can easily be found using the command :

```python
gdalinfo <geotiff_filename.tif>
```
The amplitude image metadata elements can be found in [the metadata section](../metadata). 

## Amplitude Image in Context
Figure 2 provides a useful summary of Amplitude images in the context of the processing options available with the red line highlighting the decisions made during product production. 

<figure>
<img src="../img/GRD-Image-product-tree.png" style="width:100%">
<figcaption align = "center"><em>Figure 2: The Processing Steps and Implementation Considerations for ICEYE amplitude images</em></figcaption>
</figure>

## References
\bibliography