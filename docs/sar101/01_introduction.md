# Introduction to SAR

!!! summary

    - Radar is a form of active remote sensing where a radar system emits electromagnetic radiation and records the returned echoes which can be used to form images of distant objects and areas.

    - A Real Aperture Radar (RAR) is limited by the size of its physical antenna, and engineers can only build and deploy antennas of a certain size.

    - The innovation of Synthetic Aperture Radar (SAR) solves this limitation by using the motion of a platform (either an aircraft or satellite) to collect and combine radar echos to synthesize a very long antenna, which makes it possible to generate high resolution images.

    - SAR systems look to the side to get unique range values, or distance measurements, for each object on the ground. This is important for distinguishing objects from each other during data collection, but can impact the appearance of the image (distortions).

    - The resolution of a radar image is based on two components that are independent of each other: range resolution (which depends on pulse bandwidth) and azimuth resolution (which depends on the size of the antenna and the emitted wavelength).

<span class="underline">Synthetic Aperture Radar (SAR)</span> is a remote sensing method unique in its ability to image day and night, and in all weather conditions. While optical imagery uses light from the sun to illuminate the surface, SAR and other radar systems are <span class="underline">active sensors</span>: they emit their own energy in the form of electromagnetic radiation (in the microwave region) to illuminate a scene and then measure the returned echo. See Figure [<span class="underline">1.1</span>](#figure-1.1-passive-and-active-remote-sensing) for an illustrative comparison of passive and active remote sensing.

<figure id="figure-1.1-passive-and-active-remote-sensing">
<img src="https://github.com/sjjsy/product-documentation/releases/download/additional-assets-test/image3.png">
<figcaption><strong>Figure 1.1: Passive and Active Remote Sensing.</strong> Passive sensing systems leverage the sun’s powerful illumination while active systems benefit from independence, allowing all-weather, day-night imaging and coherent measurements.</figcaption>
</figure>

SAR uses microwave wavelengths to produce very high-resolution images of the Earth’s surface from both air and space regardless of weather. The essence of SAR is that by collecting radar measurements sequentially along a system’s flight path and then processing the returned echoes together, we synthesize a large “virtual” antenna. Since spatial resolution is directly proportional to antenna length, SAR thereby enables the generation of images with spatial resolutions that would otherwise require infeasibly long antennas.

This chapter explains this principle further, introduces several foundational terms, and outlines the history of SAR.

## 1.1) Radar Imaging, Antenna Aperture, and Beamwidth

The fundamental capabilities of radar stem from its ability to measure the distance and direction of electromagnetic echoes, allowing it to map its surroundings.

Radar is an acronym meaning <span class="underline">RAdio Detection And Ranging (RADAR)</span>. A radar transmitter emits electromagnetic radiation—typically in the form of radio or microwave signals—toward a target, and the reflected echoes are captured by a receiver. This is the *detection* part of radar. The time delay between emission and receipt of each signal is precisely measured and used to calculate distances to each target in the scene. Because electromagnetic waves travel at the speed of light, we can determine how far away an object is by multiplying the time it takes for the signal to return by the speed of light—then dividing by two, since the signal travels to the target and back. Determining the distance to a target is called *ranging.*

While measuring the distance from a sensor to a target is valuable, distance alone does not provide enough information for locating objects. To more precisely locate the source of a radar echo, we need additional information. In radar systems, this can be achieved using a directive <span class="underline">antenna</span>. A directive antenna focuses transmitted (and received) energy more in some directions than others, forming what is known as a <span class="underline">beam pattern</span>. This allows the radar to illuminate and receive signals from specific directions, enabling angular discrimination. Using this property, we can determine the angle of arrival of incoming echoes. When range and angle measurements are combined, they form a two-dimensional representation of the reflected microwave energy—what we refer to as a <span class="underline">radar image</span>.

It is important to understand that an image is constructed from the <span class="underline">backscatter</span>—the reflected signals or echoes—of radar pulses transmitted by the sensor. These pulses are emitted at a regular rate called the <span class="underline">Pulse Repetition Frequency (PRF)</span>, which typically ranges from a few hundred pulses per second in airborne systems to several thousand in spaceborne platforms. After each pulse is transmitted, the radar receives echoes from objects on the ground. The collection of these echoes forms a range profile, representing the distribution of reflected energy at different distances from the radar. This <span class="underline">range profile</span> corresponds to a single line in the final radar image, capturing information from the area illuminated by that specific pulse (shown as the shaded area in Figure [<span class="underline">1.3</span>](#figure-1.3-side-looking-airborne-radar-slar)). As the radar platform moves forward and continues transmitting pulses, a sequence of range profiles is recorded and assembled into a two-dimensional radar image.

The range measurements are collected perpendicular to the flight direction, in the <span class="underline">slant range direction</span>, which is the line of sight direction between the radar and a scatterer on the surface. The word *slant* comes from the fact that the side-looking radar mounted on an airplane is inclined, or slanted, to measure surface returns. The ability to distinguish range variations to different objects is represented by the <span class="underline">slant range resolution</span>, and it is determined by the length of the transmitted pulses. Figure [<span class="underline">1.3</span>](#figure-1.3-side-looking-airborne-radar-slar) also shows <span class="underline">ground range resolution</span> which is the slant range resolution projected to the ground plane.

These three resolutions – azimuth, slant range and ground range – are introduced here, but their genesis is discussed in more depth in Chapter [<span class="underline">6</span>](06_spatial_resolution_and_geospatial_accuracy.md). Note that sometimes the word *slant* or *ground* is omitted and only the word *range* is used and one must use context to deduce which term is being discussed.

In imaging systems such as those used in optics, photography, microscopy, and astronomy, the <span class="underline">aperture</span> refers to the physical opening (or collecting area) through which waves (typically light) are gathered. This aperture defines the spatial extent of the incoming wavefront that the system captures. The larger the aperture, the more of the wavefront is collected and coherently summed by the lens, which enables the system to better focus energy or <span class="underline">signal power</span> into a sharp point on the image plane. This focusing ability has a direct impact on the <span class="underline">spatial resolution</span> of the data collected by the system—and thereby, the ability to distinguish fine details or closely spaced objects. We will discuss resolution more in Chapter [<span class="underline">6</span>](06_spatial_resolution_and_geospatial_accuracy.md).

In radar, the aperture refers to the area of the antenna that captures incoming electromagnetic waves. This area defines the spatial extent of the wavefront being received and thus determines how sharply the waves can be summed or focused in a particular direction. The result of this wave summation is the beam pattern of the antenna: a directional sensitivity profile that dictates how well the radar can resolve targets at different angles.

Just as a larger optical aperture can lead to finer spatial detail, a larger radar antenna leads to a narrower beam, and therefore better angular resolution. In both cases, the aperture governs how well the system can distinguish fine spatial features. In radar, when a single antenna is used for both transmitting and receiving—common in <span class="underline">monostatic</span> radar systems, including most Synthetic Aperture Radar (SAR) satellites—the aperture impacts resolution and sensitivity twice: once during transmission and again during reception.

!!! note
    A radar where the receiver and transmitter have their own antennas and are physically separate and distant is called a <span class="underline">bistatic radar</span>. Moreover, a system that fuses data from multiple spatially distributed monostatic and/or bistatic radars is called a <span class="underline">multistatic radar</span>.
    
    Synthetic aperture radar and multistatic radar share some principles and benefits: While a long effective aperture is synthesized in SAR using the motion of the radar, multistatic radar also synthesizes a large effective aperture using multiple radars situated apart. Both require advanced computational processing to *synthesize* and fuse the data but typically produce much better imaging results than stationary monostatic radars.
    
    Note also that multistatic radar and SAR are not mutually exclusive: An even more powerful <span class="underline">effective aperture</span> can be synthesized with a multistatic SAR system, where data is fused from multiple spatially distributed antennas that also move!

Figure [<span class="underline">1.2</span>](#figure-1.2-basic-radar-imaging-terms) illustrates basic concepts relating to monostatic radar: <span class="underline">Antenna aperture</span> refers to the physical dimensions of the antenna, which for rectangular antennas are defined as width and length. <span class="underline">Beamwidth</span> defines the angular spread of an antenna's radiated and received signal power. The beamwidth of an antenna is inversely proportional to its aperture size.

<figure id="figure-1.2-basic-radar-imaging-terms">
<img src="https://github.com/sjjsy/product-documentation/releases/download/additional-assets-test/image4.png">
<figcaption><strong>Figure 1.2: Basic Radar Imaging Terms.</strong></figcaption>
</figure>

Before delving further into the principles of radar imaging, it is helpful to first define some essential terminology illustrated in Figure [<span class="underline">1.2</span>](#figure-1.2-basic-radar-imaging-terms). <span class="underline">Illumination</span> refers to the fact that objects on the surface can become visible to the radar only if they interact with the transmitted signal. The energy that returns back to the sensor is called <span class="underline">backscatter</span> and it is the signal data that is measured and received by the antenna to form an image. A <span class="underline">scatterer</span> is anything in the scene that scatters the incoming microwave signal. A ground feature that blocks the illumination of other scatterers creates a radar <span class="underline">shadow</span> which prevents the area in the shadow from being imaged. <span class="underline">Range</span> refers to the distance between the radar and specific targets or points in a scene. The <span class="underline">azimuth</span> angle of a target is defined as its angle relative to the antenna’s boresight in the horizontal plane.

## 1.2) Side-Looking Illumination and Ranging

Radar imaging systems illuminate the ground from the side rather than directly beneath the sensor. This technique, known as <span class="underline">Side-Looking Illumination (SLI)</span> or <span class="underline">Side-Looking Radar (SLR)</span>, is essential because radar determines the position of targets based on the *time delay* of returned signals—i.e., by measuring range.

If the radar were to look straight down (nadir), then for targets lying on a flat ground surface, the differences in range between nearby points would be extremely small. This would make it nearly impossible to distinguish between them based on signal travel time, resulting in poor or no resolution on the ground plane. By contrast, a side-looking geometry introduces greater variation in the slant range to different points on the ground, even if the surface is flat. These differences in distance translate into measurable time delays in the returned signal, allowing the radar to reliably separate targets in the range direction. In other words, side-looking geometry ensures that variations in target distance translate into measurable time delays, enabling reliable range discrimination.

For example, the two purple diamonds in the vertical illumination illustration in Figure [<span class="underline">1.3</span>](#figure-1.3-vertical-vs-side-looking-illumination) would be represented as a single pixel in the image despite occupying unique ground positions. Radar imaging must therefore be side-looking so that all ground points from the <span class="underline">near range</span> – the edge of the scene closest to the radar – all the way to the <span class="underline">far range</span> – the edge of the scene farthest from the radar – have different range values (assuming flat terrain). Pixels in a radar image are placed on the image based partly on their range, or distance, from the sensor along the radar line of sight.

This constraint has important geometric consequences for radar images, which we’ll explore in more detail later. Unlike optical systems—which passively capture images in a plane perpendicular to the direction of incoming light—radar systems actively form images using ranging. One dimension of the radar image, the *range direction*, lies along the direction of illumination itself. This results in a unique and sometimes counterintuitive image geometry that distinguishes radar from traditional optical imaging systems.

!!! note
    The Line-Of-Sight (LOS) refers to the path travelled by the medium of sight – typically electromagnetic waves – from the target to the observer, or sensor. In simple cases, the LOS is a straight line, but it may be curved or segmented due to refraction, reflection, or obstructions in the environment, in which case the observer might incorrectly estimate the target’s location.

<figure id="figure-1.3-vertical-vs-side-looking-illumination">
<div class="figure-row">
  <img src="https://github.com/sjjsy/product-documentation/releases/download/additional-assets-test/image5.png" alt="Vertical looking illumination">
  <img src="https://github.com/sjjsy/product-documentation/releases/download/additional-assets-test/image6.png" alt="Side-looking illumination">
</div>
<figcaption><strong>Figure 1.3: Vertical vs Side-Looking Illumination.</strong> Radar imaging must be side-looking so that ground points from the near to far range have mostly different range values. The illumination is typically broadside, or perpendicular, to the flight direction.</figcaption>
</figure>

## 1.3) Real Aperture and Side-Looking Airborne Radar

In this section we will discuss the basics of Real Aperture Radar (RAR), as well as the limitations of RAR which led to the development of spaceborne SAR.

<span class="underline">Real Aperture Radar (RAR)</span> can be thought of as the most straightforward form of radar imaging. In its simplest form, RAR involves a radar system transmitting pulses and recording the time it takes for echoes to return, thereby measuring the range to targets. When the radar is stationary, this range information is very accurate and straightforward to compute. However, determining the position of targets in the <span class="underline">azimuth</span> (or <span class="underline">cross-range</span>) direction—perpendicular to the line of sight (see Figure [<span class="underline">1.3</span>](#figure-1.3-side-looking-airborne-radar-slar))—is a completely separate, independent and much more challenging task.

<span class="underline">Resolution</span> refers to the ability to distinguish between two closely spaced objects (We will discuss resolution more in Chapter [<span class="underline">6</span>](06_spatial_resolution_and_geospatial_accuracy.md), but we touch on it here to help explain why system design needed to evolve) or signals (tackled in Chapter [<span class="underline"> 7</span>](07_separating_signals_from_noise.md#75-radiometric-resolution-quantization-and-dynamic-range) when discussing radiometric resolution). When discussing resolution in SAR images, we are often referring to spatial resolution. Spatial resolution is dependent on two independent measures of resolution: range and azimuth resolution. While range resolution in RAR can be made quite precise using short pulses, azimuth resolution is fundamentally limited by the size of the antenna and the way it captures angular information. A RAR system can be used to produce a two-dimensional range-azimuth image in different ways:

1.  **Rotating the antenna**: By sweeping the radar beam in a circular or sector pattern, the system effectively builds up a two-dimensional image by observing the scene from multiple angles. This technique is commonly used in weather radar (e.g., precipitation mapping) and marine surveillance, where targets are relatively close and resolution requirements are modest. However, as distance to the target increases, the angular spread of the radar beam causes the cross-range resolution to degrade significantly.

2.  **Moving the antenna**: When the radar is mounted on a moving platform—such as a vehicle, ship, or aircraft—it can record backscatter from different points on the ground as it moves forward. The radar can build up an intensity map of the scene in the azimuth direction simply by collecting and storing these echoes along the path of motion.

Even with a very large stationary antenna, azimuth resolution of RAR is still limited. A larger antenna produces a narrower beam which helps focus energy, but the beam still widens with distance. This results in range-dependent resolution: high resolution near the radar, and poorer resolution farther away. While this can be useful for identifying large objects, RAR is not able to generate high resolution images.

The first widely used ground imaging real aperture radars were side-looking and mounted on aircraft, and were consequently referred to as <span class="underline">Side-Looking Airborne Radar (SLAR)</span>. Not only did the aircraft provide the RAR a larger view of the surface, but its steady movement made it possible to build a two-dimensional image one straight line at a time (see Figure [<span class="underline">1.3</span>](#figure-1.3-side-looking-airborne-radar-slar)). Azimuth resolution was relatively consistent between the near and far range due to the high altitude of the platform relative to the size of the scene in range.

In SLAR, the azimuth resolution—the ability to distinguish targets along the flight path—is determined by the angular width of the radar beam on the ground in the azimuth direction (i.e., the direction of flight). This angular width depends on the beamwidth of the antenna in that direction, which in turn is governed by the physical size of the antenna: a larger antenna produces a narrower beam and thus better azimuth resolution.

!!! note inline end
    The terms azimuth, along-track, azimuthal, and cross-range are often used interchangeably in radar literature. They all refer to the same direction—parallel to the motion of the radar platform.

<figure id="figure-1.3-side-looking-airborne-radar-slar">
<img src="https://github.com/sjjsy/product-documentation/releases/download/additional-assets-test/image7.png">
<figcaption><strong>Figure 1.3: Side-Looking Airborne Radar (SLAR).</strong> As the platform advances along the azimuth direction, each pulse emitted in the slant plane results in the collection of another range profile, spanning echoes from each point between the near and the far range.</figcaption>
</figure>

Again, azimuth resolution in SLAR is based on the angular width of the pulse in the azimuth direction (represented by ꞵ in Figure [<span class="underline">1.3</span>](#figure-1.3-side-looking-airborne-radar-slar)). Antennas that are long in the azimuth direction create narrow beams, which focus the signal and enable the detection of individual objects. However, even a narrow beam spreads out as it propagates from the antenna to the distant ground surface (See Figure [<span class="underline">1.4</span>](#figure-1.4-slar-pulse-dimensions)). In a RAR system, azimuth resolution is much better in the <span class="underline">near range</span> than the <span class="underline">far range</span>, illustrated by the following equation:

\[\delta_{\text{az}} = \frac{R\lambda}{L} = \frac{H\lambda}{L\sin\gamma}\]

Here, \(R\) is the slant range, \(\lambda\) is the wavelength used by the radar, and \(L\) is the physical length of the antenna in the azimuth direction. In the second representation slant range is replaced with \(H\), the altitude of the airplane or the height of the imaging platform, and we introduce \(\gamma\), the slant or *depression angle* (the angle between the dotted vertical line and the beam in Figure [<span class="underline">1.3</span>](#figure-1.3-side-looking-airborne-radar-slar)), to make the equation reflect the SLAR use case.

Ground range resolution in SLAR is independent from azimuth resolution, and is based on pulse length (see Figure [<span class="underline">1.4</span>](#figure-1.4-slar-pulse-dimensions)). The equation is as follows:

\[\delta_{\text{gr}} = \frac{\tau c}{2\cos\gamma}\]

Here, \(\tau\) is the radar pulse duration and \(c\) is the speed of light.

<figure id="figure-1.4-slar-pulse-dimensions">
<img src="https://github.com/sjjsy/product-documentation/releases/download/additional-assets-test/image8.png">
<figcaption><strong>Figure 1.4: SLAR Pulse Dimensions.</strong></figcaption>
</figure>

To illustrate the differences in resolution in azimuth and range, let us examine an airborne system. This example uses an airplane flying at an altitude of 3 km with a RAR system with a 1 microsecond pulse duration, operating in [<span class="underline">L-band</span>](03_radar_frequency_bands.md) with a wavelength of 20 cm, with a 3 meter antenna at a 45° slant or depression angle. We achieve approximately the following azimuth and ground range resolutions:

\[\delta_{\text{az}} = \frac{H\lambda}{L\sin\gamma} = \frac{3000m \cdot 0.20m}{3m \cdot \sin 45{^\circ}} \approx 283m\]

\[\delta_{\text{gr}} = \frac{\tau c}{2\cos\gamma} = \frac{1\mu s \cdot 299792458\frac{m}{s}}{2 \cdot \cos 45{^\circ}} \approx 212m\]

These values highlight the limitations of SLAR, which uses a small physical antenna. It produces images with resolution in the hundreds of meters, even from relatively low flying aircraft. Such images could not even distinguish city blocks let alone individual buildings from one another. Applying the same techniques would have had serious limitations when it came time to move from airborne to spaceborne systems. To achieve a high resolution image of about 0.3 meters using an X-band (\~3 cm wavelength) antenna in space, an ultra short pulse duration of about 2 nanoseconds and an antenna about 75 kilometers long would be required. Obviously, these are in no way feasible engineering parameters\!

!!! history
    Note that while both azimuth and range resolution are showcased in the above examples as limiting factors, the challenge with range resolution was quickly resolved: In the 1950s, scientists and engineers invented a set of *intra-pulse modulation* techniques, namely *pulse chirping* (explained in Section [<span class="underline">6.2</span>](06_spatial_resolution_and_geospatial_accuracy.md/#62-range-resolution-pulse-chirping-and-pulse-bandwidth)), to effectively *compress* or shorten pulses further without reducing their total energy content and recognizability, and thus without making it overly difficult to receive and distinguish their echoes as they returned to the radar. These innovations greatly improved range resolution and have therefore been leveraged by both RAR and SAR systems ever since. However, the challenge with azimuth resolution remained for years longer, until the invention of aperture synthesis.

## 1.4) The Invention of Aperture Synthesis

We have established that for SLAR, an infeasibly huge antenna would be required to create the aperture and the narrow radar beam necessary for high azimuth resolution. However, an invention by mathematician Carl A. Wiley and subsequent development by Emmett N. Leith and others during the 1950s proved that a huge physical antenna was not needed.

Instead, it is possible to use a small physical antenna to emit a large number of pulses throughout a precisely known trajectory. By applying a computational post-processing scheme to all the data collected, an enormous *synthetic aperture* enabling very fine azimuth resolution can be created. When all of the measurements are stored and processed together, it is as if they were collected from one antenna equal in length to the whole trajectory through which echoes were received.

This technique is called <span class="underline">Synthetic Aperture Radar (SAR)</span> and it has become so pervasive in radar imaging that the non-synthesizing method is now called *real aperture* radar imaging (as presented in the previous section) in order to be clear. Indeed, the invention of SAR has been foundational not only to the genesis of spaceborne radar imaging but to various other radar imaging applications.

The long extent of the synthetic aperture allows for the combination of many wave measurements to produce a very narrow azimuth beamwidth, which is the key to achieving high resolution. In an optical system, a lens or mirror collects and focuses light waves from different points across the aperture, enabling high-resolution imaging. In SAR, a similar physical principle is applied: electromagnetic waves received at different positions along the flight path (aperture) are combined to form a focused image. However, instead of doing this physically, SAR performs the summation digitally, by combining the recorded voltage signals from each pulse. In this way, the signal processor plays the same role that a lens or objective does in an optical system.

Figure [<span class="underline">1.5</span>](#figure-1.5-linear-extent-of-recording-locations) shows a radar antenna sequentially emitting a series of pulses and recording the echoes from a series of sequential receive positions. In the resulting image, these echoes are integrated to form a representation of the scatterers on the surface.

<figure id="figure-1.5-linear-extent-of-recording-locations">
<img src="https://github.com/sjjsy/product-documentation/releases/download/additional-assets-test/image9.png">
<figcaption><strong>Figure 1.5: Linear Extent of Recording Locations.</strong></figcaption>
</figure>

The synthetic aperture length is approximately:

\[L_{\text{syn}} = vT\]

Where \(v\) is the platform velocity, and \(T\) is the time over which signal pulse transmission and receipt data is coherently processed and integrated. In Chapter [<span class="underline">2</span>](02_satellite_orbits_and_constellations.md) it is explained that a typical SAR satellite might orbit the Earth at an altitude of roughly 600 km with an orbital velocity of roughly 8 km/s. Consequently, over a 25 second illumination period, a synthetic aperture length of about 200 km is generated. A 200km long synthetic aperture is clearly well suited for generating high resolution radar imagery from spaceborne systems.

!!! history
    The inventor Carl. A. Wiley’s work at Goodyear Aircraft Company demonstrated the earliest pioneering SAR systems in the 1950s, and by the 1970s, NASA/JPL started to work on the Airborne Imaging Radar (AIR) that showcased the utility of L-band SAR for Earth science experiments. Finally, in 1978 the first spaceborne SAR mission was launched, the SEASAT-A developed jointly by NASA and JPL, and it demonstrated how vast synthetic apertures can be created in space to provide relatively high resolution Earth imagery.
