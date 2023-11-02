!!! info 
    SAR Video products are only produced when the Dwell collection mode is utilized

## SAR Video (VID)

 SAR Video is similar to the [CSI product](../csi) in which the acquired SAR data is divided into multiple sub-apertures. However, in the case of SAR Video, they are not used to create composite images. Instead, each discrete sub-aperture is used as a frame of a video.

 Video is very useful in applications where moving objects need to be analyzed. By simple inspection and analysis of a video, it is possible to infer the general direction and speed of moving objects such as vessels and vehicles. SAR Video is also effective for detecting objects hidden in the forest area as well as human-made objects as these tend to give bright reflections and show as glint when playing a video.

<figure markdown>
![placeholder](img/vid_harbour.gif){width="800"}
<figcaption align = "center"><em>Figure 1: Detail of a SAR Video (VID) Product showing multiple vessels in movement. </em></figcaption>
</figure> 

## Container format and metadata

The formats of the VID product are MPEG4 and GIF. Additionally, a GeoTIFF format is produces where each of the video frames is available as a separate band to facilitate frame by frame analysis in any image exploitation tools. The user can measure and track changes and moving objects between frames by stepping through the different bands of the image. The VID products made from SAR data acquired in a Dwell collection contain 25 frames. Important metadata on each of each of the video frames and how the VID product is formed is avaiable in the GeoTIFF. GeoTIFF metadata can be accessed by multiple methods including:

* Using the library gdal and running the command <code>gdalinfo filename.tif</code> (for example: <code>gdalinfo ICEYE_X2_VID_SLED_1906432_20231020T110813.tif</code>)  
* In the open source application QGIS by selecting Raster → Miscelaneous → Raster information → Run 


<figure markdown>
## Key VID GeoTIFF Metadata 
| Metadata Element&nbsp;&nbsp;&nbsp;&nbsp;| Description| Type| Unit|
|----|----|----|----|
|`FRAME_DURATION`|Duration of SAR data collection for each video frame. |List of float64|seconds|
|`FRAME_MID_TIME`|Timestamp at the center of each video frame. Documented as seconds after beginning of thecollection  |List of float64|seconds|
|`FRAME_POS`|Satellite position at the center of each video frame|List of float64 triplets|ECEF coordinates|
|`FRAME_VEL`|Velocity vector of the satellite at the center of each video frame |List of float64 triplets|meters per second|
</figure>

<figure markdown>
![placeholder](img/video_waves.gif){width="800"}
<figcaption align = "center"><em>Figure 2: Detail of a SAR Video (VID) Product showing waves and human-made objects highlighted by glint. </em></figcaption>
</figure> 

## Notes and Explanations
1. **Frame duration:** The exact duration and time separation of each video frames varies slightly depending on specific collection characteristics. The actual duration value is avaialable in the [GeoTIFF metadata](#key-vid-geotiff-metadata).