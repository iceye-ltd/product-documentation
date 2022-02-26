# The Remarkable Story of Synthetic Aperture Radar
## Improving Azimuth Resolution by Synthesizing a Long Antenna
It takes a long antenna to create narrow radar beams, but the aperture itself does not have to be a giant physical antenna. Instead, a “synthetic” aperture can be created from a small antenna and a linear extent of recording locations. Figure 7 shows a radar antenna sequentially emitting a series of pulses, like a microwave strobe light, and recording the echoes from a string of receive positions.

<figure>
<img src="../img/RecordingLocations.png" style="width:100%">
<figcaption align = "center"><em>Figure 7: Linear Extent of Recording Locations</em></figcaption>
</figure>

In the SAR technique all of the measurements are stored and later processed together. It is as if they were collected from one long antenna equal in length to the extent of the sensor locations that received the echoes. Synthetic Aperture Radar is a post-processing scheme applied to data collected by a standard radar antenna and receiver. 

## Stripmap and Spotlight Apertures
There are a few methods to illuminate the ground in SAR imaging. These collection modes trade off resolution and coverage in different ways. To establish how we can simulate long apertures we’ll contrast the two most common forms of SAR imaging: stripmap and spotlight.
In stripmap mode the pulses are sent out at a constant angle, usually broadside to the flight direction. In this case, the length of this simulated aperture ($L$) is the same as the width of the beam on the ground (Figure 8). Wider beams produced by smaller antennas mean longer apertures and better azimuth resolution. This directly contrasts with the real-aperture radar of SLAR where the beam was kept as narrow as possible to obtain good resolution.

<figure markdown>
![image title](../img/stripmapSynAp.png){ width="250"}
<figcaption><em>Figure 8: Stripmap Synthetic Aperture</em></figcaption>
</figure>

The spotlight form of SAR varies the boresight angle in the azimuth direction to illuminate a fixed ground location (Figure 9). This technique greatly increases the synthetic-aperture length and offers excellent azimuth resolution, at the cost of limited ground coverage. At ICEYE we are capable of illuminating a fixed spot for as long as 30 seconds. Given the velocity of low-earth orbits (7.5 km/sec), this yields a synthetic aperture more than 225 kilometers long !

<figure markdown>
![image title](../img/spotlightSynAp.png){ width="300"}
<figcaption><em>Figure 9: Spotlight Synthetic Aperture</em></figcaption>
</figure>

## Phase History Data and SAR Azimuth Resolution
We can create long “synthetic” apertures because radar illumination is coherent. That is, the sensor controls the structure of the transmitted pulses and they all have the same form. It emits pulses and measures the details of each echo: time, strength and “phase”. Phase refers to the position of the wave in its cycle, denoting whether it is at its peak, trough or somewhere in between.

The SAR antenna moves only slightly from pulse to pulse. It turns out that the change in location must be less than one-half the antenna length. But this small change in location causes the successive measurements of the range to some object to change as well. The slight change in position imparts a slight change in range. Since the phase is dependent on the range, the small change in adjacent sensor locations also imparts a slight change in phase. These phase changes form a pattern across the aperture, which changes depending on the azimuth location of a ground feature. The record of all the changing phases for all the scatterers in the scene is called phase history data. For a particular object, this is the “history” of how phase changed from one receive location to the next.

Given carefully measured sensor locations, the phase histories for each location across the scene are predictable. The azimuth position of each scatterer can be calculated by comparing the predicted phase pattern of some location to the measured phase history pattern for that point. This is the essence of azimuth resolution. Phase history data and their reference patterns are compared to discriminate the azimuth position of scatterers in the scene.

Now that we have that huge aperture and the equation for azimuth resolution becomes: 

$$ \delta_{az} = \frac{\lambda}{2\Delta \theta} $$

where $\delta_{az}$ is the SAR azimuth resolution.

This equation is gorgeous. It says that azimuth resolution is based on the wavelength of our radar waves and the change in the integration angle ($\Delta \theta$) while the point was being imaged (Figure 10). Resolution improves when the wavelength is small and the integration angle change is large.

<figure markdown>
![image title](../img/spotSAAngle.png){ width="300"}
<figcaption><em>Figure 10: Spotlight Synthetic Aperture Angle</em></figcaption>
</figure>

Now let’s use SAR with an integration angle change of 0.07 radians (4.5°). This is reasonable because the current operational performance of ICEYE's spotlight mode can easily exceed this angle. 

$$\delta_{az} = \frac{\lambda}{2\Delta \theta} $$

$$\delta_{az} = \frac{3 cm}{2 \times 0.07} $$

$$\delta_{az} = 0.21m $$

For stripmap mode the azimuth resolution equation reduces to a simpler form, where $D_A$ is the length of the antenna in the azimuth direction:

$$\delta_{az} = \frac{D_A}{2} $$

This is just a special stripmap case of the more general equation, but it seems to imply that we could make the antenna really small to achieve good stripmap resolution. While this is literally true, the small size of the antenna would lessen the total power that could be transmitted and also degrade the ability to record the weak backscattered echoes. Noise would increase significantly. It would also require the PRF to get unreasonably large because a pulse is required at least every one-half antenna length.

Stripmap cannot support high-resolution SAR. For that we need to steer the beam during illumination to increase the synthetic aperture, as with a spotlight collection. This mode is capable of fine resolution and it can use a larger, and therefore more powerful and sensitive antenna.

## Something Is Missing
These elegant equations are an astonishing statement about resolution, but it is even more amazing when we consider what is missing. Notice that the SAR azimuth resolution equations do not include a term for distance. Use it on an aircraft or move it all the way out into space, and azimuth resolution does not change.

Of course, distance does impact signal strength. When the sensor is further away, the signal strength weakens dramatically and this poses serious challenges to the SAR imaging process. We will not discuss this issue in this overview, but we can say here that radar antennas are very sensitive. Spaceborne SARs successfully record very weak backscatters.