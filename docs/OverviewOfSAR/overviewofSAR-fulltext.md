# An Overview of SAR Imaging

!!! Note
    This overview is exercepted with permission from [The Essentials of SAR](https://www.amazon.com/dp/B09CGKTLZV/ref=cm_sw_em_r_mt_dp_H9NDBJSVREXRK5PA4Z58), by Thomas P. Ager[@ageressentials]This comprehensive text was written for SAR users, not electrical engineers. It reviews the many interesting aspects of SAR and its uses that we cannot cover in this short overview.

## The Value of SAR Imaging
Synthetic aperture radar is well known as the imaging technique that can see through clouds and darkness. But SAR provides a number of other capabilities that are simply not available from optical sources. These include:

* *High Resolution Independent of Distance*: One of the outstanding characteristics of SAR is that it is capable of detailed resolution regardless of how far away the sensor is from the ground. SAR sensors can provide very high resolution, even from space.
* *Variable Resolution and Coverage*: SAR illumination is controlled electronically, and it can be manipulated to vary resolution and coverage. Images can be collected over small areas at fine resolution, over medium-sized areas at medium resolution or over large areas at coarse resolution.
* *Precision Geolocation*: SAR measurements are inherently precise. Properly calibrated images can have geolocation accuracy less than the scale of a single pixel for well-defined features.
* *Coherent Illumination and Many Products*: The controlled nature of SAR imaging enables the formation of images and many other products. These include sub-aperture image stacks that highlight glinting features and motion, dense elevation models, precise measurements of surface motion, and amplitude and coherent change images or series.

## Radar Bands
There are several radar bands ranging from wavelengths at the millimeter level to a full meter (Table 1). X-Band has the best combination of cloud-penetration and resolution for spaceborne sensors. 
In addition to atmospheric gases, there are larger atmospheric particles that scatter visible light but which are transparent to microwaves. In addition to penetrating clouds, X-band radar waves travel through smog, volcanic ash, and sandstorms. 

<figure markdown>
| BAND | WAVELENGTH [cm] | FREQUENCY [GHZ] | Origin |
|------|-----------------|-----------------|--------|
UHF | 30 to 100 | 1 to 0.3 | Ultra High Frequency 
P | 60 to 120 | 0.5 to 0.25 | P for "previous", as the British used the band for the earliest radars, but later switched to higher frequencies. 
L  | 15 to 30 | 2 to 1 | for 'Long Wave' 
S | 7.5 to 15 | 4 to 2 | for 'Short Wave'. Not to be confused with the radio band 
C | 3.75 to 7.5 | 8 to 4 | Originally for 'compromise' between S and X band 
X | 2.5 to 3.75 | 12 to 8 | Used in WWII for fire control, X for cross as in crosshair  
Ku | 1.67 to 2.5 | 18 to 12 | for "Kurz-under" 
K | 1.11 to 1.67 | 27 to 18 | German "kurz" means short, another reference to short wavelength 
Ka | 0.75 to 1.11 | 40 to 27 | Ka for "kurz-above" 
V | 0.40 to 0.75 | 75 to 40 | V for 'very' high frequency - not to be confused with VHF 
W | 0.27 to 0.40 | 110 to 75 | W follows V in the alphabet 
mm | 0.10 to 0.27 | 300 to 110 | millimeter wave 
<figcaption align = "center"><em>Table 1 : Radar Bands</em></figcaption>
</figure>    

## A Simple Form of Radar Imaging
As seen in Figure 1 the radar antenna emits a series of pulses toward the ground where they are scattered in many directions. The sensor records the “backscatter”, which is the portion reflected toward the antenna. It measures the strength of the echo and the time it took for the pulse to travel to the ground and back.

<figure>
<img src="../img/PulseBackscatter.png" style="width:100%">
<figcaption align = "center"><em>Figure 1: Pulse Transmission and Backscatter</em></figcaption>
</figure>

Signal strength corresponds to pixel brightness and the timing provides range information. The range is one-half the total travel time. In the equation below, $\Delta T$ is the travel time and $c$ is the speed of light:

$$Range = \frac{\Delta T\ c}{2}$$

### Side-Looking Illumination
Since the pixels of a radar imaging system are placed on the image based partly on their range, the antenna cannot illuminate the ground in a vertical orientation. If it did, features on the same imaging line at equivalent angles off nadir would have identical ranges, like the two purple diamonds in Figure 2, and they would occupy the same pixel location.

<figure>
<img src="../img/verticalIllumination.png" style="width:100%">
<figcaption align = "center"><em>Figure 2: Vertical Illumination</em></figcaption>
</figure>

Radar imaging must be side-looking so that ground points from the near to far range have different range values (Figure 3). The illumination is typically broadside, or perpendicular, to the flight direction. 

<figure>
<img src="../img/sideIllumination.png" style="width:100%">
<figcaption align = "center"><em>Figure 3: Side-Looking Illumination</em></figcaption>
</figure>


### Radar Angles
The angles associated with radar illumination are shown in Figure 4, which is based on a spherical earth surface. Most radar imaging is broadside to the flight direction, but some systems can collect off-broadside in a squinted orientation. The angle down from the local level at the sensor is called the depression angle. The angle between the line-of-sight ray and the local vertical is the incidence angle. The angle between the tangent to the surface and the line of sight is the grazing angle. Note that the incidence and grazing angles are complements in that they form a right angle when combined. This means that a 60° incidence angle is the same as a 30° grazing angle.

<figure>
<img src="../img/RadarImagingAngles.png" style="width:100%">
<figcaption align = "center"><em>Figure 4: Radar Imaging Angles</em></figcaption>
</figure>

### Side Looking Airborne Radar
The first useful radar imaging technique was a form called Side-Looking Airborne Radar (SLAR) (Figure 5). The image is built up via the forward motion of the antenna, one line at a time. The pulses are emitted at a rate called the pulse repetition frequency (PRF), which can range from a few hundred pulses each second for airborne systems to thousands each second for spacecraft. In the SLAR technique, the individual pulses create each image line.
The angular width of the pulse on the ground along the direction of flight, or azimuth direction, determines one component of resolution. The range measurements are collected in the “slant range” direction, and range variations to different objects form the second dimension of resolution.

<figure>
<img src="../img/sidelookingRadar.png" style="width:100%">
<figcaption align = "center"><em>Figure 5: Side-Looking Airborne Radar</em></figcaption>
</figure>

SLAR was used the early days of radar imaging but it had serious limitations. Range resolution was one-half the length of the pulse in the range direction. Since the pulses are emitted at light speed, even a very brief pulse of one-millionth of a second would be 300 meters long and produce range resolution of 150 meters (Figure 6).

Azimuth resolution was based on the angular width of the pulse in the azimuth direction ($\beta$). Long antennas create narrow beams, but the beam spreads out from the antenna to the distant ground surface. Antennas cannot be made long enough to produce good azimuth resolution, and SLAR produced images with resolutions in the hundreds of meters, even from aircraft. This is why the brilliant concept of synthesizing a long antenna from the actions of a small one was developed. We call this Synthetic Aperture Radar.

<figure>
<img src="../img/SLAR_PulseDimensions.png" style="width:100%">
<figcaption align = "center"><em>Figure 6: SLAR Pulse Dimensions</em></figcaption>
</figure>

## The Remarkable Story of Synthetic Aperture Radar
### Improving Azimuth Resolution by Synthesizing a Long Antenna
It takes a long antenna to create narrow radar beams, but the aperture itself does not have to be a giant physical antenna. Instead, a “synthetic” aperture can be created from a small antenna and a linear extent of recording locations. Figure 7 shows a radar antenna sequentially emitting a series of pulses, like a microwave strobe light, and recording the echoes from a string of receive positions.

<figure>
<img src="../img/RecordingLocations.png" style="width:100%">
<figcaption align = "center"><em>Figure 7: Linear Extent of Recording Locations</em></figcaption>
</figure>

In the SAR technique all of the measurements are stored and later processed together. It is as if they were collected from one long antenna equal in length to the extent of the sensor locations that received the echoes. Synthetic Aperture Radar is a post-processing scheme applied to data collected by a standard radar antenna and receiver. 

### Stripmap and Spotlight Apertures
There are a few methods to illuminate the ground in SAR imaging. These collection modes trade off resolution and coverage in different ways. To establish how we can simulate long apertures we’ll contrast the two most common forms of SAR imaging: stripmap and spotlight.
In stripmap mode the pulses are sent out at a constant angle, usually broadside to the flight direction. In this case, the length of this simulated aperture ($L$) is the same as the width of the beam on the ground (Figure 8). Wider beams produced by smaller antennas mean longer apertures and better azimuth resolution. This directly contrasts with the real-aperture radar of SLAR where the beam was kept as narrow as possible to obtain good resolution.

<figure>
<img src="../img/stripmapSynAp.png" style="width:100%">
<figcaption align = "center"><em>Figure 8: Stripmap Synthetic Aperture</em></figcaption>
</figure>

The spotlight form of SAR varies the boresight angle in the azimuth direction to illuminate a fixed ground location (Figure 9). This technique greatly increases the synthetic-aperture length and offers excellent azimuth resolution, at the cost of limited ground coverage. At ICEYE we are capable of illuminating a fixed spot for as long as 30 seconds. Given the velocity of low-earth orbits (7.5 km/sec), this yields a synthetic aperture more than 225 kilometers long !

<figure>
<img src="../img/spotlightSynAp.png" style="width:100%">
<figcaption align = "center"><em>Figure 9: Spotlight Synthetic Aperture</em></figcaption>
</figure>

### Phase History Data and SAR Azimuth Resolution
We can create long “synthetic” apertures because radar illumination is coherent. That is, the sensor controls the structure of the transmitted pulses and they all have the same form. It emits pulses and measures the details of each echo: time, strength and “phase”. Phase refers to the position of the wave in its cycle, denoting whether it is at its peak, trough or somewhere in between.

The SAR antenna moves only slightly from pulse to pulse. It turns out that the change in location must be less than one-half the antenna length. But this small change in location causes the successive measurements of the range to some object to change as well. The slight change in position imparts a slight change in range. Since the phase is dependent on the range, the small change in adjacent sensor locations also imparts a slight change in phase. These phase changes form a pattern across the aperture, which changes depending on the azimuth location of a ground feature. The record of all the changing phases for all the scatterers in the scene is called phase history data. For a particular object, this is the “history” of how phase changed from one receive location to the next.

Given carefully measured sensor locations, the phase histories for each location across the scene are predictable. The azimuth position of each scatterer can be calculated by comparing the predicted phase pattern of some location to the measured phase history pattern for that point. This is the essence of azimuth resolution. Phase history data and their reference patterns are compared to discriminate the azimuth position of scatterers in the scene.

Now that we have that huge aperture and the equation for azimuth resolution becomes: 

$$ \delta_{az} = \frac{\lambda}{2\Delta \theta} $$

where $\delta_{az}$ is the SAR azimuth resolution.

This equation is gorgeous. It says that azimuth resolution is based on the wavelength of our radar waves and the change in the integration angle ($\Delta \theta$) while the point was being imaged (Figure 10). Resolution improves when the wavelength is small and the integration angle change is large.

<figure>
<img src="../img/spotSAAngle.png" style="width:100%">
<figcaption align = "center"><em>Figure 10: Spotlight Synthetic Aperture Angle</em></figcaption>
</figure>

Now let’s use SAR with an integration angle change of 0.07 radians (4.5°). This is reasonable because the current operational performance of ICEYE's spotlight mode can easily exceed this angle. 

$$\delta_{az} = \frac{\lambda}{2\Delta \theta} $$

$$\delta_{az} = \frac{3 cm}{2 \times 0.07} $$

$$\delta_{az} = 0.21m $$

For stripmap mode the azimuth resolution equation reduces to a simpler form, where $D_A$ is the length of the antenna in the azimuth direction:

$$\delta_{az} = \frac{D_A}{2} $$

This is just a special stripmap case of the more general equation, but it seems to imply that we could make the antenna really small to achieve good stripmap resolution. While this is literally true, the small size of the antenna would lessen the total power that could be transmitted and also degrade the ability to record the weak backscattered echoes. Noise would increase significantly. It would also require the PRF to get unreasonably large because a pulse is required at least every one-half antenna length.

Stripmap cannot support high-resolution SAR. For that we need to steer the beam during illumination to increase the synthetic aperture, as with a spotlight collection. This mode is capable of fine resolution and it can use a larger, and therefore more powerful and sensitive antenna.

### Something Is Missing
These elegant equations are an astonishing statement about resolution, but it is even more amazing when we consider what is missing. Notice that the SAR azimuth resolution equations do not include a term for distance. Use it on an aircraft or move it all the way out into space, and azimuth resolution does not change.

Of course, distance does impact signal strength. When the sensor is further away, the signal strength weakens dramatically and this poses serious challenges to the SAR imaging process. We will not discuss this issue in this overview, but we can say here that radar antennas are very sensitive. Spaceborne SARs successfully record very weak backscatters.

## Fixing Range Resolution by Synthesizing a Short Pulse
In our discussions about aperture synthesis, we did not say anything about range resolution. This is because the “synthetic aperture” technique itself deals only with azimuth. It does not do anything to address the problem we saw with brute-force range resolution. Recall that this is one-half of the pulse length, which is the speed of light ($c$) times the pulse duration, $T$: 

$$\delta_{ra} = \frac{c\ T}{2}$$

where $\delta_{ra}$ is the slant range resolution.

Thus far, we have described our radar pulses as if they have a fixed frequency, like X-band pulses of 10 GHz frequency and a 3 cm wavelength. But most radars actually transmit *chirped* pulses in which the frequency changes (Figure 11). Notice how the wavelength of the green pulse is manipulated and varies from long to short

<figure>
<img src="../img/chirped.png" style="width:100%">
<figcaption align = "center"><em>Figure 11: Chirped Pulse</em></figcaption>
</figure>

When we state the frequency or wavelength of a SAR sensor, those values typically apply at the mid-way time of the pulse. This is known as the radar center frequency or wavelength. The actual transmitted wavelengths are varied quite a bit on either side to form chirped pulses (Figure 12).

<figure>
<img src="../img/centreFreq.png" style="width:100%">
<figcaption align = "center"><em>Figure 12: Centre Frequency</em></figcaption>
</figure>

There are many different pulse modulation techniques, but the chirp with a smoothly varying frequency is most common. A chirped pulse is easy to produce and since the total transmitted energy is a product of amplitude and duration, a long pulse can contain a substantial amount of energy without needing a large peak power.

A chirped pulse enables high range resolution because its form is exactly specified and its echo is a reversed and weakened copy. The reflection has the same shape as the emitted signal, it’s just flipped and has a much smaller amplitude. The two are compared in what is called a matched filter process. The known structure of the emitted pulse is compared to the echo at various locations. A calculation is performed, and if they are misaligned the result of this calculation is zero. At the exact location where they match there is a strong signal that indicates the match. A synthetic pulse that is narrow in range replaces the spread-out pulse (Figure 13).

<figure>
<img src="../img/RangeCompression.png" style="width:100%">
<figcaption align = "center"><em>Figure 13: Range Compression</em></figcaption>
</figure>

The width of the compressed pulse is based entirely on the bandwidth of the emitted pulse. The slant range resolution equation is transformed:

$$ \delta_{slant\ range\ chirp\ compressed} = \frac{c}{2B} $$

This is a really beautiful equation. It is so simple and powerful. Resolution in range is entirely based on how much bandwidth we impart to chirped pulses, and like its azimuth counterpart it has nothing whatsoever to do with distance to the ground.

### Slant Range Resolution Examples
So how much can we vary pulse frequency? Well, bandwidths can be made really large. Consider an X-band system capable of 300,000,000 cycles per second (300 MHz) of bandwidth. We can calculate resolution in the slant range:

$$ \delta_{sr} = \frac{3\times10^8\ m/sec}{2\times300MHz} $$

$$ \delta_{sr} = \frac{3\times10^8\ m/sec}{2\times300\times10^8Hz} $$

$$ \delta_{sr} = 0.5 metres $$

Plans for the next generation of ICEYE satellites include pulse bandwidths of 600 MHz and 1200 MHz. These will yield a slant range resolution cell of 0.25 meters and better from a satellite that is perhaps 750,000 meters away from the imaged area.

### Ground Range Resolution
The slant range is the distance between the antenna and the target, and that is the direction where range resolution is measured. To produce images along the ground surface, the pixels have to be projected to the “ground range” from their original slant range orientation (Figure 14). This has the effect of elongating the pixels in range.

<figure>
<img src="../img/groundRangeRes.png" style="width:100%">
<figcaption align = "center"><em>Figure 14: Ground Range Resolution</em></figcaption>
</figure>


The illustration shows the relationship between slant range resolution, shown in blue, and the length of the equivalent resolution distance along the ground, shown in green. When the illumination is steep, as in this example, the projection to the ground surface results in a much longer ground range cell. You can imagine what would happen as the steepness continued to approach nadir. This is exactly opposite to the situation with optical imaging resolution, which is best at nadir.

Slant range and ground range resolution comparisons for two incidence angles are shown in Table 2. Notice the dramatic increase for the steeper illumination.

<figure markdown>
| | Incidence Angle 30° | Incidence Angle 60° |
|-|---------------------|---------------------|
| Slant Range | 0.50m | 0.50m |
|  Ground Range | 1.00m | 0.55m |
<figcaption align = "center"><em>Table 2: Resolution comparison between slant range and ground range</em></figcaption>
</figure>

While slant range resolution seems “better” than ground range resolution, keep in mind that it refers to the sensor’s ability to discriminate features along the oblique path of the energy. Most of the features we care about lie along the ground surface, and ground range resolution is a useful way to describe image resolution.

## The Beautiful Equations
The brute force method of real-aperture radar cannot produce high-resolution images. In synthetic-aperture radar we take advantage of the natural coherence of radar illumination to produce structured and consistent pulses. These enable the measurement of slight pulse-to-pulse phase shifts and the use of frequency-modulated chirps. The innovations of aperture synthesis, modulated waveforms and pulse compression produce images capable of a remarkable pixel resolution and which does not degrade as distance to the ground increases. 

Even though they are handled differently, the azimuth and range processes have a fundamental similarity:

!!! quote " "
    Azimuth resolution is based on phase variations
    across the collection interval.
    These are compared to known phase variations
    across that area to produce a long “synthetic” aperture
    and a resolution cell narrow in azimuth.

    Range resolution is based on frequency variations
    across the returned pulse.
    These are compared to known frequency variations
    in the reference pulse to produce a short “synthetic” pulse
    and a resolution cell narrow in range.


These processes result in two of the most simple and powerful equations in all of remote sensing. They are the equations that describe the spatial resolution of a SAR sensor. They are ***The Beautiful Equations*** : 

$$ \delta_{az} = \frac{\lambda}{2\Delta \theta} $$

$$ \delta_{sr} = \frac{c}{2B} $$

with $\delta_{az}$ and $\delta_{sr}$ being the azimuth resolution and the slant range resolution respectively.

## The SAR Processing Flow and Its Products
SAR image generation begins with the emission of thousands of coherent pulses and the decomposition of each echo into raw measurements of time, amplitude and phase. The first part of the processing flow is called Phase History Processing because it accounts for the changes over time of the phase values of each scatterer. Phase history data are focused into the azimuth and range components of each resolution cell to produce an image product called a “complex image” (Figure 15).

<figure>
<img src="../img/ProcessingFlow.png" style="width:100%">
<figcaption align = "center"><em>Figure 15: The SAR Processing Flow and Its Products</em></figcaption>
</figure>

### The Complex Image
!!! info inline end
    By the way, you will hear SAR engineers refer to the two parameters of a complex image as “In-Phase” and “Quadrature”. These are just another way to describe the complex values.

The left image in Figure 16 is a ICEYE amplitude image of agricultural fields. In this image each pixel has a brightness value assigned to it. This is what many people consider to be the base SAR product, but this is really only half of the full image. The SAR processor calculates the average phase value for each pixel as well. The matching “phase image” of that same scene is on the right in the figure. The combination of these two images is called a complex image, in which every pixel has amplitude and phase values. We use the term “complex” because the pixels are described by a mathematical construct called a complex number, where every number has two components.

<figure>
<img src="../img/complexAmpPhase.png" style="width:100%">
<figcaption align = "center"><em>Figure 16: Amplitude and Phase Structure of a Complex Image</em></figcaption>
</figure>

Of course, phase data are not useful for direct human interpretation. And while they may look like random noise, phase pixels are a unique and valuable aspect of SAR imaging. Phase data can be used to manipulate the synthetic aperture in different ways to extract useful information that is not available from amplitude images. Moreover, changes in the phase measurements of the same object on different images can be used to detect small surface structure characteristics. In the next section we’ll discuss how we can use phase data to refine images and create other products.

## SAR Products Derived from Complex Data
### Amplitude Images
!!! info inline end
    You should also be aware that an engineering calculation called “detection” converts in-phase and quadrature values to amplitude values. Engineers often refer to SAR amplitude images as “detected” images.
An amplitude image is certainly the most common SAR product, but you need to appreciate that this image is produced for human viewing and analysis. It is not the core image product. Amplitude images do not contain any phase information. Furthermore, the version of the amplitude image used for human viewing is not a direct copy of the amplitude values in a complex image. This is because radar sensors record an enormous span of brightness levels for each complex pixel. The maximum intensity of amplitude in a complex image is usually more than 100,000 times (50 dB) the minimum intensity, and for the best-quality images with bright targets, it is much greater. ICEYE images are produced with 16 bits of dynamic range per pixel (65536 gray levels) but even this is not sufficient to record the full dynamic range of SAR.

As valuable as they are, amplitude images have no phase data and they lose much of the dynamic range of complex pixels.  You can imagine the growing potential for computers and algorithms to process those complex pixels in ways the human visual system cannot.

### Multi-look Amplitude Images
One way in which we can use complex data is to produce different versions of the seemingly simple amplitude image. One common form of an amplitude image, for example, is called a multi-look image. Consider that azimuth and range resolution are handled independently. One is based on the length of the synthetic aperture and the other is based on the signal bandwidth, and sometimes these are quite different in magnitude. It is common for azimuth resolution to be collected at a higher fidelity than range resolution. If a full-resolution image were produced from such data it would look compressed in range. To view the image in a more natural aspect we need to “square the pixels” so that the range and azimuth scales are the same. 

!!! info inline end 
    Speckle is a grainy, noise-like feature of SAR images. It is caused by the coherent nature of SAR illumination. The reflections from small scatterers within a resolution cell combine constructively and destructively to brighten or darken the returns.
This is done by manipulating the synthetic aperture into smaller sub-apertures and then combining them. The sub-apertures are called “looks” and they each produce an image with lower azimuth resolution. This may sound disappointing, but when these individual sub-aperture images are combined, they form a multi-look image in which the noisy effect of speckle is reduced.  Complex images are stored at full-resolution and are called single-look complex (SLC) images. Amplitude images are typically multi-looked in azimuth using two to 12 sub-apertures. If range resolution exceeds azimuth resolution a similar multi-look process can be applied in the range dimension.

### Sub-aperture Stack or Video Image
Suppose we take the aperture splitting further and create six or seven segments to produce multiple sub-aperture images. One advantage of this sub-aperture stack is that it can indicate glints that are bright in only a portion of the full aperture. This signature might be washed out on the full-resolution image by the bulk of the aperture in which there was no glinting, but it can be very noticeable in one of the low-resolution sub-apertures. Glints tend to be important signatures because they are usually caused by human-made features. We could even loop the stack like a short movie, or SAR video image, to look for such glints and moving objects. This product works best for long spotlight exposures of ten seconds or more.

### Amplitude and Coherent Change Images
Perhaps the most useful SAR products are the amplitude and coherent change images (ACI, CCI). Two or more images of the same site are collected at different times to detect scene changes. For ACD only the brightness values are compared, while CCD uses phase data.

In order for change detection to work, the images have to be collected from nearly the same location in space with similar illumination geometries. For ACD the two images can be overlaid in the complementary colors (eg red and cyan). In this way, features with similar backscatters will be gray, but features with backscatters that changed during the imaging period will appear in one of the two colors. It is conventional for the first image to be displayed in red and the second in cyan. If something on the ground changes between the two collections you will see whichever color signature is dominant.

A mnemonic is used to help interpret ACD products: “Red is fled. Blue is new”. That is, a red signature indicates a feature that was present on the first image but left the scene prior to the second image, and a blue signature indicates a feature that appears only on the second image. This mnemonic is an easy way to help remember the order of the images, but appreciate that the second image is actually cyan, not blue. The intentional sloppiness of the mnemonic is acceptable here because verbal precision would ruin the rhyme.

In contrast to amplitude change detection, CCD compares the phase values of two nearly identical images taken at different times. CCD is far more sensitive to changes because it is based on phase differences rather than pixel brightness differences and, as we know, phase is measured to within a small fraction of a wavelength. The collection constraints to ensure image-to-image coherence are tighter for CCD than ACD.

When the collection parameters are nearly identical, the phase values are also nearly identical, and any changes are due to backscatter differences at a scale of less than one wavelength. It is typical for CCD images to display pixels where phase is consistent in white and the pixels where the phase has changed are dark. These are areas where the two images have “decorrelated”, or lost phase consistency, due to some subtle change in the scene.

### Other Multi-image SAR Products
The amplitude and phase data of SAR images can be combined to produce other useful products that are too numerous to describe in detail in this overview. These include **digital elevation models** derived from pixel brightness values or phase data, millimeter-level **surface motion measurements** derived phase comparisons of sets of matching images, and **automated detections** of ships, oil spills and other features. Once constellations of small SARs are established it will be possible to monitor any site in the world with large stacks of exactly matching images whose consistent signatures are linked to known ground features. These images could be collected within hours of each other and they will be the basis of **intelligent site monitoring** services that will not only detect changes, but which will also say what has changed and how it has changed.

## Separating Signals from Noise
### The Whisper
As a radar pulse travels from the antenna to the ground surface its total power remains constant, but as it moves away from the antenna, it spreads out into space and its power density weakens. As shown in Figure 17, it is as if the “skin” of the pulse becomes thinner with distance. This weakening is dramatic; it decreases with the square of the distance from the antenna.

<figure>
<img src="../img/pulseSurface.png" style="width:100%">
<figcaption align = "center"><em>Figure 17: Expanding Surface Area of a Pulse</em></figcaption>
</figure>

Given that the ground might be 750 km from the antenna, the pulse is quite weak by the time it finally reflects from surface objects. This presents even more of a problem because only a portion of the weakened pulse is reflected toward the receive antenna, and then it has to travel all the way back, weakening again with the square of the distance. By the time the microwaves return to the antenna, they are microscopically faint. The antenna and radar receiver manage to detect, amplify, and record these echoes so that they can be processed into SAR resolution cells that span more than 100,000 brightness values. SAR is amazing.

### The Challenge of Noise
Those backscattered microwaves are so weak when they arrive at the antenna that they are perturbed by any noise sources that get mixed in with them. Noise is an artifact of random microwave emissions caused mostly by onboard sensor hardware. One of the tenets of remote sensing is that all objects emit electromagnetic energy based on their temperature. The thermal noise of heated receiver hardware spans wide swaths of the spectrum, including the microwave bands, and this competes with those whispering pulse echoes.

As they struggle to capture those fading backscatter whispers, radar receivers also record random, interfering microwaves that they themselves produce. One of the disappointing aspects of the noise level is that it increases as range bandwidth increases. The large signal bandwidth that the receiver has to be capable of recording also lets more noise enter the receiver.

One of the ways that noise is quantified for SAR sensors is called the Noise Equivalent Sigma Zero (NESZ). This parameter describes the noise floor of an image. All received signals have to be stronger than the NESZ value to rise above the noise level, so it is best for NESZ to be as low as possible. Images with high NESZ values look grainy.

Unfortunately, NESZ is mystifying to SAR users who are not familiar with the dB language of engineering. Many users are confused by NESZ values like -20 dB, which actually indicates a fractional level of 1%. That is, an NESZ of -20 dB means the noise level is 1% as strong as a reference reflection from an idealized metal sphere. An NESZ of -17 dB would means the noise level is 2% as strong as the reference.

System designers have to consider many competing imaging parameters to balance image quality, resolution and noise. For spacecraft, the best choices are increased average power, larger antennas, the use of high-quality receivers with low noise factors, steeper illumination angles, and lower orbits.

## The ICEYE Innovation
In this overview of SAR, we have discussed several remarkable capabilities beyond its famous ability to penetrate clouds. These include image resolution independent of distance, electronic beam control to vary resolution and coverage, pristine geolocation, and the natural ability to measure phase to within a small fraction of a wavelength. We’ve seen that SAR pixels have both amplitude and phase, and from these we can produce many useful products.
At ICEYE, we have developed an innovative way to incorporate all of these aspects of SAR in our small and adaptable systems. We are launching a full constellation of small SARs, and we’ll upgrade them routinely to better image this ocean planet.

## References
\bibliography