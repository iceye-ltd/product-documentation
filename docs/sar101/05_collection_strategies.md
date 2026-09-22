# 5\) Collection Strategies

!!! summary

    - The three primary collection strategies—Spotlight, Stripmap, and ScanSAR—complement each other by providing different resolutions, scene sizes, and collection efficiency to benefit different applications.

    - In Spotlight mode, a small area is imaged over an extended dwell time in order to achieve maximal resolution (even less than 1 m) at the cost of scene size (typically around 5 km squared). Spotlight is suitable for e.g. high-detail infrastructure monitoring.

    - Stripmap provides balanced coverage and resolution by projecting the beam broadside at a fixed orientation to build long strip images parallel to flight direction. Stripmap is preferred for e.g. regional monitoring.

    - In ScanSAR, rapid beam steering is performed to maximize the size of the imaged scene at the cost of resolution. ScanSAR is effective for e.g. maritime surveillance.

    - SAR azimuth resolution equations contain no term for distance, which means that resolution remains constant whether the sensor is mounted on an aircraft or a spacecraft, though signal strength decreases with distance.

    - Antenna size, power, and imaging geometry define the limits of resolution, coverage, and efficiency — making system design inseparable from collection strategy.

There are three primary <span class="underline">collection strategies</span> used to illuminate the surface in SAR data collection. These collection strategies are broadly called Spotlight, Stripmap, and ScanSAR. Each strategy is suited to different applications, and has trade-offs between resolution and coverage.

## 5.1) Spotlight

In Spotlight mode, the radar beam is continuously steered to keep illuminating the same target area as the satellite moves. This allows the radar to observe the target from different angles along the orbit, effectively creating a long synthetic aperture and enabling very high azimuth resolution (see Figure [<span class="underline">5.1</span>](#figure-5.1-spotlight-synthetic-aperture)). The <span class="underline">collection duration</span> (also referred to as dwell time, illumination period, or imaging period) is the amount of time the radar transmits pulses and receives backscatter from the target or scene. The size of the resulting image size, or footprint, is limited by the physical width of the radar beam, which in turn depends on the size of the antenna and its beamwidth in the azimuth direction. As explained in Section [<span class="underline">4.2</span>](04_antennas_and_sar_geometry.md#42-beamwidth-and-illumination-power), only the portion of the total illuminated footprint where the SNR is high enough can be used to create a quality image. This is why Spotlight collections typically limit the scene sizes to around 5 km by 5 km.

<figure id="figure-5.1-spotlight-synthetic-aperture">
<img src="https://github.com/sjjsy/product-documentation/releases/download/additional-assets-test/image20.png">
<figcaption><strong>Figure 5.1: Spotlight Synthetic Aperture.</strong></figcaption>
</figure>

Collection duration is typically around 5 - 25 seconds for a Spotlight image. The images generated with this strategy provide the best resolution and signal-to-noise ratios that SAR can provide. In practical terms, there are diminishing returns beyond a certain integration angle (and collection duration). The radar rarely receives strong, coherent reflections over a wide angular range, and azimuth resolution is already very high within a much smaller interval. Extending the collection time further would simply increase data volume without significantly improving image quality.

To put it another way, while in theory a SAR satellite in a Sun-Synchronous Orbit might have some line-of-sight to a scene for around three minutes during its orbit, the backscatter would be too faint (see Radar Equation in Section [<span class="underline">7.1</span>](07_separating_signals_from_noise.md#71-the-radar-range-equation-and-the-signal-to-noise-ratio), and specular reflection in Section [<span class="underline">9.2</span>](09_data_processing_and_analysis.md#92-backscatter-polarization-and-scattering-mechanisms)) and incoherent (see Section [<span class="underline">6.1</span>](06_spatial_resolution_and_geospatial_accuracy.md#61-azimuth-resolution-phase-history-data-and-prf)) to benefit from a longer synthetic aperture. These geometric constraints prevent SAR satellites from benefitting from indefinitely long collection durations.

## 5.2) Stripmap

In the <span class="underline">Stripmap</span> collection strategy, the ground swath is illuminated with a continuous sequence of pulses while the antenna beam is fixed in a broadside imaging orientation. This results in a long image strip parallel to the flight direction. Having a wide area and a moderate resolution, Stripmap images are useful for moderate resolution monitoring applications over large swaths of sea or land. They are particularly useful for deforestation monitoring, iceberg or glacier monitoring, and assessing the impact of a flood, earthquake or volcano.

As previously described, pulses are emitted broadside to the flight direction. The length of the synthetic aperture (L) is the same as the width of the beam on the ground (Figure [<span class="underline">5.2</span>](#figure-5.2-stripmap-collection)). In other words, the integration angle is the same as the physical beamwidth of the antenna. Thus, wider beams produced by smaller antennas mean longer apertures and better azimuth resolution. This directly contrasts with the real-aperture radar of SLAR (described in Section [<span class="underline">2.3</span>](02_satellite_orbits_and_constellations.md#23-satellite-constellations-and-repeat-imaging)) where the beam was kept as narrow as possible to obtain good resolution.

<figure id="figure-5.2-stripmap-collection">
<img src="https://github.com/sjjsy/product-documentation/releases/download/additional-assets-test/image21.png">
<figcaption><strong>Figure 5.2: Stripmap Collection.</strong></figcaption>
</figure>

Compared with the Spotlight strategy, Stripmap has a shorter dwell time, smaller integration angle and synthetic aperture length, and thus a reduced resolution in order to image much larger ground areas with a single pass.

## 5.3) ScanSAR

The <span class="underline">ScanSAR</span> collection strategy leverages electronic beam steering of a satellite's phased array antenna to create multiple beams in the elevation direction. This beam steering illuminates a wide ground area by imaging multiple adjacent strips. This means that points on the ground are not illuminated for as long as in the conventional Stripmap collection strategy. This reduces the spatial resolution of ScanSAR images. The ScanSAR collection strategy is illustrated in Figure [<span class="underline">5.3</span>](#figure-5.3-scansar-collection).

<figure id="figure-5.3-scansar-collection">
<img src="https://github.com/sjjsy/product-documentation/releases/download/additional-assets-test/image22.png">
<figcaption><strong>Figure 5.3: ScanSAR Collection.</strong></figcaption>
</figure>

In conventional ScanSAR, ground points are illuminated by different parts of the radar beam resulting in brighter and darker regions in the image from near range to far range. In a technique called Terrain Observation by Progressive Scans (TOPS or TOPSAR) the radar beam is also steered sideways (in azimuth) during each burst of radar pulses to improve image quality.

Having the largest area coverage and a modest resolution, ScanSAR images are often utilized in wide area surveillance and mapping projects. ScanSAR images are ideal for maritime monitoring applications, such as oil spill or vessel detection, as well as monitoring vast ground areas.

## 5.4) Resolution Trade-Offs

The three different collection strategies are complementary to each other, as they are each suited to different use cases and applications. One might wonder why there is not a SAR image with both a large footprint and high resolution. To address this, let us briefly examine why the Stripmap and ScanSAR strategies cannot be used to achieve the high resolution and quality possible with the Spotlight strategy.

Consider applying the Spotlight collection strategy with a change in <span class="underline">integration angle</span> \(\left( \Delta\theta \right)\) of 0.35 radians (20°). Such an integration angle is well within the current operational performance of ICEYE's Spotlight collection strategy (See Figure [<span class="underline">5.4</span>](#figure-5.4-spotlight-synthetic-aperture-integration-angle)).

<figure id="figure-5.4-spotlight-synthetic-aperture-integration-angle">
<img src="https://github.com/sjjsy/product-documentation/releases/download/additional-assets-test/image23.png">
<figcaption><strong>Figure 5.4: Spotlight Synthetic Aperture Integration Angle.</strong></figcaption>
</figure>

Now let us take the equation for azimuth resolution from Chapter [<span class="underline">6</span>](06_spatial_resolution_and_geospatial_accuracy.md):

\[\delta_{\text{az}} = \frac{\lambda}{2\Delta\theta}\]

\[\delta_{\text{az}} = \frac{3\text{cm}}{2 \times 0.35} = 4.2\text{cm}\]

Here, \(\lambda\) is the wavelength (x-band has an approximate wavelength of 3cm). With a 20° integration angle, we can achieve azimuth resolution in the centimeter range\!

In the Stripmap strategy, the azimuth resolution equation reduces to a simpler form, where D<sub>A</sub> is the length of the antenna in the azimuth direction:

\[\delta_\text{az} = \frac{D{}_{A}}{2}\]

This is a special Stripmap case of the more general equation, but it seems to imply that a very small antenna could achieve good resolution with the Stripmap collection strategy. While this is mathematically true, it is important to consider engineering trade-offs. Firstly, the small size of the antenna would lessen the total power that could be transmitted and also degrade the ability to record the weak backscattered echoes. Noise would increase significantly. Secondly, it would require a very large pulse repetition frequency because a pulse is required at least every one-half antenna length.

We have illustrated why the Stripmap collection strategy cannot achieve very high-resolution SAR in practice. Neither can the ScanSAR strategy. For high resolution we need to steer the beam during illumination to increase the synthetic aperture, as is done in the Spotlight collection strategy.

## 5.5) Altitude Independence

The azimuth resolution equations above make an astonishing statement about resolution, which is even more amazing when we consider what is missing. Notice that the equations do not include a term for distance. Regardless of if a sensor is on an aircraft or a satellite, azimuth resolution does not change\!

Of course, distance does impact signal strength. When the sensor is further away, the signal strength weakens dramatically and this poses serious challenges to the SAR imaging process, as is explained in Chapter [<span class="underline">7</span>](07_separating_signals_from_noise.md). However, since spaceborne SAR antennas can be very sensitive, they successfully record very weak backscatters, mitigating this challenge with distance.
