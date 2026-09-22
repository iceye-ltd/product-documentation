# 6\) Spatial Resolution and Geospatial Accuracy

!!! summary inline end

    - There are many measures of resolution—slant range, ground range, azimuth, and spatial—each describing a different aspect of detail or measurement sensitivity.

    - Slant range resolution is determined by pulse bandwidth; shorter effective pulses result in finer range resolution, enabling even decimeter-level detail from orbit, with pulse chirping and matched filtering used to achieve high bandwidth while maintaining energy.

    - Ground range resolution is the projection of slant range resolution to the ground plane and depends on incidence angle: it is highest at shallow look angles and degrades near nadir or in steep topography.

    - Azimuth resolution is determined by azimuthal Doppler bandwidth, synthetic aperture length (integration angle and dwell time), and wavelength, and is achieved through synthetic aperture processing of coherent radar pulses.

    - Spatial resolution is a function of both ground range and azimuth resolutions and is thus a holistic measure of the smallest discernible objects in the scene.

    - Geolocation and geospatial accuracy determine how truthfully the relative sizes, shapes, distances and locations of the objects in the image represent reality. These accuracies depend on accurate orbit data, calibration targets, digital elevation models, and other data used to eliminate distortions through orthorectification.

In this chapter we explore the concepts of resolution and geolocation accuracy, their various measures, and how they are derived.

As explained in Section [<span class="underline">1.3</span>](01_introduction.md#13-real-aperture-and-side-looking-airborne-radar), range and azimuth resolution are independent of each other in a SAR image. The range resolution, or more specifically the <span class="underline">slant range resolution,</span> of a SAR image is the resolution determined by the pulse bandwidth of the radio wave signals emitted and received by the sensor: the higher the pulse bandwidth, the higher the resolution. Conversely, <span class="underline">azimuth resolution</span> is determined by the wavelength of the emitted microwave and the integration angle. The genesis of azimuth and slant range resolutions, and what the term pulse bandwidth and other related concepts mean are discussed further in Sections [<span class="underline">6.1</span>](#61-azimuth-resolution-phase-history-data-and-prf) and [<span class="underline">6.2</span>](#62-range-resolution-pulse-chirping-and-pulse-bandwidth). A third measure of resolution is the <span class="underline">ground range resolution</span> which is a function of slant range resolution and (local) incidence angle, as it is the projection of slant range onto the ground plane in the imaged scene. The ground range resolution is discussed further in Section [<span class="underline">6.3</span>](#63-ground-range-resolution-and-incidence-angle).

<span class="underline">Spatial resolution</span> is the degree to which one can resolve objects or features on the imaged scene as distinct, regardless of the direction (azimuth, ground range or some other direction in between). The higher the spatial resolution of an image, the easier it is to discriminate between details in the scene.

All four measures of resolution are summarized in Table [<span class="underline">6.1</span>](#table-6.1-the-measures-of-spatial-resolution-in-sar). While the table provides a summary, the following sections explain these resolutions in more depth.

<figure id="table-6.1-the-measures-of-spatial-resolution-in-sar">
<figcaption><strong>Table 6.1: The Measures of Spatial Resolution in SAR.</strong></figcaption>
<table>
<thead>
<tr>
<th align="left"><strong>Name of Resolution Measure</strong></th>
<th align="left"><strong>Target of Resolvability</strong></th>
<th align="left"><strong>Primary Determining Factors</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Slant Range</td>
<td align="left">Objects and features along the boresight axis (slant range)</td>
<td align="left">Pulse Bandwidth</td>
</tr>
<tr>
<td align="left">Ground Range</td>
<td align="left">Objects and features along the projection of the slant range onto the ground plane</td>
<td align="left">Slant Range Resolution, Incidence Angle</td>
</tr>
<tr>
<td align="left">Azimuth</td>
<td align="left">Objects and features along the ground plane perpendicular to the ground range</td>
<td align="left">Azimuthal Doppler Bandwidth, Synthetic Aperture Length, Wavelength</td>
</tr>
<tr>
<td align="left">Spatial</td>
<td align="left">Objects and features in the ground plane regardless of direction</td>
<td align="left">Ground Range Resolution, Azimuth Resolution</td>
</tr>
</tbody>
</table>
</figure>

Finally, Section [<span class="underline">6.5</span>](#65-geolocation-geospatial-accuracy-and-orthorectification) moves beyond resolution and introduces two important measures of accuracy, namely geolocation and geospatial accuracy, as well as some key concepts and processes like orthorectification. It is important to understand that while resolution and accuracy are both needed to maximize the usability of SAR imagery, they are distinct concepts that are sometimes confused.

## 6.1) Azimuth Resolution, Phase History Data and PRF

### 6.1.1 Azimuth Resolution 

The <span class="underline">azimuth resolution</span> of a SAR image is determined by the wavelength of the radar and the length of the synthetic aperture (longer aperture results in higher resolution). As discussed in Section [<span class="underline">1.3</span>](01_introduction.md#13-real-aperture-and-side-looking-airborne-radar), real aperture radar cannot produce high-resolution images. Synthetic aperture radar takes advantage of the phase coherence of radar illumination to produce structured and consistent pulses. These enable the measurement of small pulse-to-pulse phase shifts and the use of frequency-modulated chirps. The innovations of aperture synthesis, modulated waveforms, and pulse compression can produce images with high resolution regardless of imaging altitude.

We can create long synthetic apertures because radar illumination is coherent. That is, the sensor controls the structure – most importantly, the frequency and phase – of the transmitted pulses so they all have the same form. The sensor emits pulses and measures the details of each backscatter echo: time, strength and phase.

Again, the equation for azimuth resolution \(\delta_{\text{az}}\) is:

\[\delta_{\text{az}} = \frac{\lambda}{2\Delta\theta}\]

This equation states that azimuth resolution is based on the wavelength of a radar wave and the integration angle (\(\Delta\theta\) ) over a ground target (Figure [<span class="underline">5.4</span>](#figure-5.4-spotlight-synthetic-aperture-integration-angle)). Resolution improves when the wavelength is small and the integration angle is large. This relationship is why the long imaging time and large integration angle used in the Spotlight collection strategy results in high resolution imagery (see Section [<span class="underline">5.4</span>](05_collection_strategies.md#54-resolution-trade-offs)). As described in Chapter [<span class="underline">3</span>](03_radar_frequency_bands.md), shorter wavelengths suffer from greater atmospheric attenuation and cannot penetrate clouds as well as longer wavelengths. Therefore, X-band is seen as an optimal wavelength because it offers both high resolution and reliable cloud penetration.

!!! note
    <span class="underline">Phase</span> refers to the position of an oscillating wave in its wave cycle. <span class="underline">Oscillation</span> is the movement back and forth in a regular periodic rhythm. A <span class="underline">periodic wave</span> is a propagating dynamic disturbance that causes one or more physical quantities to oscillate around an equilibrium at some frequency. <span class="underline">Wave cycle</span> is a complete oscillation of such a wave from one point to the next identical point, as illustrated in Figure [<span class="underline">6.1</span>](#figure-6.1-periodic-wave-terminology). Because it is a cycle, phase is often measured as an angle with degrees or radians, with 360° or \(2\pi\) rad equalling 0° and 0 rad. <span class="underline">Phase offset</span> is the difference in phase between two waves. Assuming identical waveform and frequency, a phase offset of zero means that the waves are in sync and interfere constructively, while a phase offset of 180° means they are completely out of phase, and one always reaches its peak when the other reaches its trough, thus negating each other, if they are of equal amplitude.

<figure id="figure-6.1-periodic-wave-terminology">
<img src="https://github.com/sjjsy/product-documentation/releases/download/additional-assets-test/image24.png">
<figcaption><strong>Figure 6.1: Periodic Wave Terminology.</strong> This illustration shows a sine wave annotated with basic waveform terminology, clarifying the concepts of wavelength, wave cycle, amplitude, peak, and trough. Note that the units of wavelength and wave cycle are distance (meters) and angle (radians), while period is measured in time.</figcaption>
</figure>

!!! note
    Figure [<span class="underline">6.1</span>](#figure-6.1-periodic-wave-terminology) illustrates the concepts of <span class="underline">wavelength</span> (the distance between two consecutive points on a wave cycle that have identical phase) and <span class="underline">period</span> (the time it takes for a wave to complete a full cycle). <span class="underline">Peak</span> and <span class="underline">trough</span> are the maximum and minimum phase values in the repeating wave cycle, respectively. <span class="underline">Peak amplitude</span> is the difference at the peak, <span class="underline">peak-to-peak amplitude</span> is the difference between the peak and the trough, and <span class="underline">amplitude</span> is peak-to-peak amplitude divided by two. All these measures of amplitude are used to represent the strength of the wave.

Before concluding this discussion on azimuth resolution, let us clarify why we use the term <span class="underline">slant azimuth resolution</span> instead of azimuth resolution when specifying the resolution performance of a SAR system. Slant azimuth resolution is measured in the <span class="underline">slant range geometry</span>, i.e. the line of sight plane that connects the orbiting radar’s trajectory tangent line with the plane of the imaged scene. The term <span class="underline">ground azimuth resolution</span> is used to communicate the projected resolution in the ground plane. Ground azimuth resolution will often be larger than slant azimuth resolution as a result of projection.

### 6.1.2 Phase History Data

An electromagnetic wave is made up of two parts: an electric field and a magnetic field. These fields move together through space, and they both oscillate at right angles to each other and to the direction the wave is traveling. When the wave reaches the radar antenna, it causes tiny voltages (which is a measure of the strength of the electric field) to oscillate inside it. The radar system records these voltage changes over time. The system can also measure the phase of the wave—how far along the wave cycle it is—by comparing it with the phase of the signal that was originally transmitted.

As a SAR platform moves along its flight path, it transmits a series of radar pulses at different positions along the orbit. With each pulse, the distance between the antenna and the ground scene changes slightly. This small change in distance affects the number of wave cycles the signal travels, which in turn causes a change in phase from one pulse to the next.

For any given point on the ground, the pattern of phase changes across all the pulses depends on its azimuth position—that is, where it lies along the flight direction. This sequence of phase measurements for each target is known as its <span class="underline">Phase History Data (PHD)</span>. You can think of it as the “fingerprint” of how the phase of the echo from a specific location changes as the radar moves. Because we know the precise positions of the radar along its path, we can predict the phase history that a scatterer at a particular azimuth position should produce. By comparing the measured phase history with these predicted patterns, we can determine where each scatterer is located in the azimuth direction. This is the key principle behind achieving azimuth resolution in SAR.

### 6.1.3 Pulse Repetition Frequency (PRF)

The synthetic aperture in SAR is built from a discrete set of pulse measurements, each taken as the radar platform moves along its flight path. These measurements are made at specific positions where pulses are transmitted and echoes are received, meaning we are sampling the radar signal in space, specifically along the azimuth direction. Because this sampling is not continuous, we need to ensure that we’re capturing enough detail to accurately reconstruct the phase history of each target. According to the Nyquist sampling theorem, we must take at least two samples per wave cycle to avoid ambiguity. In SAR, this means the radar must not move so far between pulses that the phase of the returning signal changes by more than half a wavelength. If it does, we can no longer tell how much the phase has changed—was it a small shift or a full extra cycle? This uncertainty leads to phase ambiguities.

To prevent this, the spacing between successive pulse measurements (which is determined by the platform’s speed and the <span class="underline">pulse repetition frequency, or PRF</span>) must be small enough to ensure that the distance to any given target doesn't change by more than half a wavelength between pulses. Since the satellite’s orbital height sets its velocity, achieving sufficient azimuth sampling requires a high enough PRF. If the PRF is too low, these phase ambiguities appear in the final image as <span class="underline">azimuth ambiguities</span>—false or “ghost” targets that can interfere with image interpretation.

Most of ICEYE’s SAR satellites orbit the Earth at a speed of approximately 7.58 km/s. To avoid azimuth ambiguities, the satellite must transmit pulses frequently enough that the radar does not move more than half a wavelength between measurements. This requirement translates to a minimum pulse repetition frequency (PRF) of around 5 kHz, corresponding to a pulse repetition interval (PRI) of about 200 microseconds, during which the satellite moves roughly 1.6 meters.

However, one cannot infinitely increase the PRF. While a higher PRF helps avoid azimuth ambiguities, it also increases the chance of range ambiguities—where echoes from different targets overlap in range, making it harder to distinguish their actual distances. For this reason, PRF must be carefully balanced. ICEYE typically limits PRF to around 7 kHz, ensuring reliable performance in both azimuth and range dimensions.

In this section we discussed how we are able to generate a large synthetic aperture, resulting in high resolution imagery, due to the coherent nature of radar pulses. This is tied to the essence of azimuth resolution: Phase history data and their reference patterns are compared to discriminate the azimuth position of scatterers in the scene. Finally, we covered how the Nyquist sampling theorem dictates the PRF, which directly impacts the appearance of a SAR image. A too-low PRF will introduce azimuth ambiguities, while a too-high PRF will introduce range ambiguities.

## 6.2) Range Resolution, Pulse Chirping, and Pulse Bandwidth

### 6.2.1 Range Resolution

In our initial discussions about aperture synthesis in Section [<span class="underline">1.4</span>](01_introduction.md#14-the-invention-of-aperture-synthesis), we discussed azimuth resolution, but did not say anything about the other component of SAR data: range resolution. This is because the “synthetic aperture” technique itself deals only with azimuth. In radar systems, <span class="underline">range resolution</span>—the ability to distinguish two objects that are close together in range—depends on the duration of the transmitted pulse. Shorter pulses provide finer resolution, because they allow the radar to more precisely separate the echoes coming from distinct targets. For a real aperture radar, range resolution is one-half of the pulse length, which is the speed of light (c) times the pulse duration, T:

\[\delta_{\text{ra}} = \frac{cT}{2}\]

Where \(\delta_{\text{ra}}\) is the slant range resolution.

However, there’s a catch: the total energy in each pulse determines how strong the received signal is, and this energy depends on both the pulse duration and the peak power of the transmitter. Since radar transmitters typically operate near their maximum peak power, shortening the pulse means reducing its total energy. This leads to a weaker return signal, lowering the signal-to-noise ratio (SNR) and making it harder to detect targets—especially at long ranges. This creates a fundamental trade-off: we want short pulses for better resolution, but we also need long, energetic pulses to see far into the distance. In spaceborne SAR systems, where power is already limited and the distances are enormous, this becomes a real design challenge.

### 6.2.2 Pulse Chirping

So far, we’ve described radar pulses as if they had a constant frequency—for example, an X-band pulse at 10 GHz with a 3 cm wavelength. However, most modern radars actually transmit <span class="underline">chirped</span> pulses, in which the frequency changes smoothly over the duration of the pulse. This technique is the foundation of a method called <span class="underline">pulse compression</span>, which helps solve the above conundrum: we want long pulses to gather enough energy to detect distant targets, but short pulses to achieve fine range resolution.

Pulse compression allows us to do both. In a chirped pulse, the frequency changes gradually over time. One common example is the <span class="underline">Linear Frequency Modulated (LFM)</span> signal or chirp, where the frequency increases or decreases at a constant rate. Because the pulse lasts longer, it carries more energy—so we can see farther. And because the frequency varies throughout the pulse, delayed echoes from different targets correspond to different frequencies at any given instant. This means that even if the echoes overlap in time, we can separate them later based on their frequency content. In this way, chirped pulses let us have the energy of a long pulse and the resolution of a short one.

<figure id="figure-6.2-pulse-modulation">
<img src="https://github.com/sjjsy/product-documentation/releases/download/additional-assets-test/image25.png">
<figcaption><strong>Figure 6.2: Pulse Modulation.</strong> The upper waveform is an unmodulated single frequency pulse, while the lower is a chirp produced with linear frequency modulation. Modulation facilitates the distinction of overlapping pulses from backscatter.</figcaption>
</figure>

When we state the frequency or wavelength of a SAR sensor, those values typically describe the frequency at the center of the pulse. This is known as the <span class="underline">radar center (or carrier) frequency</span> or wavelength. The actual transmitted wavelengths are varied quite a bit on either side to form chirped pulses (Figure [<span class="underline">6.3</span>](#figure-6.3-center-frequency)).

<figure id="figure-6.3-center-frequency">
<img src="https://github.com/sjjsy/product-documentation/releases/download/additional-assets-test/image26.png">
<figcaption><strong>Figure 6.3: Center Frequency.</strong> In frequency modulation, the instantaneous frequency of the pulse deviates relative to the center frequency of the original unmodulated pulse.</figcaption>
</figure>

There are many different pulse modulation techniques, but the chirp with a constant varying frequency drawn in black in Figure [<span class="underline">6.2</span>](#figure-6.2-pulse-modulation) is most common. A long chirped pulse is easy to produce, and since the total transmitted energy is a product of amplitude and duration, the pulse can contain a substantial amount of energy without requiring large peak power.

### 6.2.3 Pulse Bandwidth

<span class="underline">Pulse bandwidth</span> refers to how wide the range of frequencies is in a radar pulse. Instead of transmitting a single, steady frequency, a chirped pulse sweeps through a range of frequencies during its duration. The bandwidth is simply the difference between the starting and ending frequencies of that sweep.

For example, imagine a chirped pulse that lasts 10 microseconds, has a center frequency of 9.65 GHz, and a bandwidth of 600 MHz. This means the pulse starts at 9.35 GHz, and the frequency increases steadily—like turning a dial—until it reaches 9.95 GHz by the end of the 10 microseconds. Over the course of the pulse, the radar generates a spectrum of frequencies, and that 600 MHz interval is what we call the bandwidth. It tells us how much frequency content the signal has, and it directly influences how well we can resolve targets in range.

Chirped radar pulses are often generated in 1-100 microseconds. Because waves travel at the speed of light, even short pulses result in pulses with approximate lengths of 300 m-30 km (as measured in distance, obtained by multiplying the pulse length with the speed of light), consisting of roughly 10 thousand to a million individual wave cycles, assuming X-band waves are employed.

### 6.2.4 Pulse Compression

Although a chirped pulse contains the information needed for high range resolution, the raw signal received by the radar doesn’t yet look like a sharp, well-separated set of echoes. Instead, it’s a blend of many overlapping reflections from different targets, each one being a delayed and weakened version of the original chirp. Because these echoes arrive at slightly different times, they overlap in the received signal and are hard to separate just by looking at the raw data.

However, there’s a clever way to sort them out—by using a technique called a <span class="underline">matched filter</span>. The idea is that although the echoes are weak and overlapping, each one still has the same structure as the transmitted chirp, just delayed and reduced in amplitude. Because the chirp’s frequency changes steadily over time, each delayed echo has a different frequency pattern at any given moment. This means we can tell them apart based on their unique timing.

To do this, we take a copy of the transmitted chirp and compare it to the received signal, testing different time delays to see where they match. This process, called cross-correlation, works by sliding the transmitted chirp across the received signal and calculating how similar they are at each step. When the alignment is wrong, the result is near zero. But when the alignment is just right—matching the delay of a real echo—the correlation produces a strong peak. This effectively compresses the long, stretched-out chirp into a narrow pulse, giving us sharp, high-resolution measurements of target distances. The result of such <span class="underline">pulse compression</span> is illustrated in Figure [<span class="underline">6.4</span>](#figure-6.4-range-compression).

<figure id="figure-6.4-range-compression">
<img src="https://github.com/sjjsy/product-documentation/releases/download/additional-assets-test/image27.png">
<figcaption><strong>Figure 6.4: Range Compression.</strong> The high amplitude main lobe represents the focused return from the target. Sidelobes are inherent to matched filtering of finite-duration chirps, and are not a result of imperfect compression.</figcaption>
</figure>

The sharpness of the compressed pulse, i.e. the ability to resolve two close-together targets, is directly related to the bandwidth of the chirp signal. The more frequencies the chirp sweeps through, the easier it is to distinguish between echoes arriving at slightly different times. This makes the matched filter response more focused in time, creating a narrower, sharper peak. Mathematically, the width of this peak is inversely proportional to the bandwidth: a wider bandwidth produces a narrower compressed pulse, and thus better range resolution.

For instance, with a bandwidth of 300 MHz we get a compressed pulse width (or duration) of about 3 nanoseconds. Since the measured time delay can easily be converted to range by multiplying by the speed of light and diving by two, we can express the slant range resolution as

\[\delta_{\text{slant}\text{range}\text{chirp}\text{compressed}} = \frac{c}{2B}{}_{{}_{}}\]

This equation is elegant in its simplicity and power—it shows that slant range resolution depends solely on the bandwidth of the chirped pulses.

How much can we vary pulse frequency? Pulse bandwidths can be made quite large. Consider an X-band system capable of a bandwidth of 1200 MHz, which is currently the limit allocated to remote sensing satellites in X-band by the ITU. We can calculate resolution in the slant range using the above equation as follows:

\[\delta_{\text{sr}} = \frac{c}{2B} \approx \frac{3 \cdot 10^{8}\frac{m}{s}}{2 \cdot 1200 \cdot 10^{6}\text{Hz}} = 0.125m\]

Isn’t it almost unbelievable that despite the immense speed of electromagnetic radiation (the speed of light), modern SAR systems can produce and receive radio wave pulses with widely varying frequencies and still (or actually because of it) successfully decipher all the received signal data to produce images with range resolutions of about 10 cm, all the way from outer space\!?

## 6.3) Ground Range Resolution and Incidence Angle

The slant range is the distance between the antenna and the target, and is the dimension where range resolution is measured. To produce images along the ground surface (which is what we tend to be interested in), the pixels have to be projected to the “ground range” from their original slant range orientation (Figure [<span class="underline">6.5</span>](#figure-6.5-ground-range-resolution)). This has the effect of elongating the pixels in range.

<figure id="figure-6.5-ground-range-resolution">
<img src="https://github.com/sjjsy/product-documentation/releases/download/additional-assets-test/image28.png">
<figcaption><strong>Figure 6.5: Ground Range Resolution.</strong></figcaption>
</figure>

Figure [<span class="underline">6.5</span>](#figure-6.5-ground-range-resolution) shows the relationship between slant range resolution, and the length of the equivalent resolution distance along the ground, shown in green. When the illumination is steep, as in this example where the incidence angle is only 30°, the projection to the ground surface results in a much longer ground range cell, illustrated by the solid green horizontal line. Now imagine what would happen as the angle continued to approach nadir (incidence angle of 0°): The extent of the cell represented in Figure [<span class="underline">6.5</span>](#figure-6.5-ground-range-resolution) in green would extend left infinitely and the resulting ground range resolution would be infinitely poor. This is exactly opposite to the situation with optical imaging resolution, which is best at nadir.

The following equation expresses ground range resolution, showing how it depends not only on the signal bandwidth but also on the incidence angle, which affects how slant range resolution projects onto the ground:

\[\delta_{\text{gr}} = \frac{\delta_{\text{sr}}}{\sin\theta}\]

The equation shows mathematically what is shown visually in Figure [<span class="underline">6.5</span>](#figure-6.5-ground-range-resolution). Table [<span class="underline">6.2</span>](#table-6.2-effect-of-incidence-angle-on-ground-range-resolution) provides tangible examples, highlighting the ground range resolutions \(\delta_{\text{gr}}\) at two different incidence angles \(\theta\) given a slant range resolution \(\delta_{\text{sr}}\) of 50 cm. Notice the dramatic increase in ground range resolution for the higher incidence angle and thus more horizontal illumination (remember that incidence angle is the angle between the local vertical or surface normal at the target and the line of sight toward the imaging sensor).

<figure id="table-6.2-effect-of-incidence-angle-on-ground-range-resolution">
<figcaption><strong>Table 6.2: Effect of Incidence Angle on Ground Range Resolution.</strong></figcaption>
<table>
<thead>
<tr>
<th align="left"><strong>Resolution</strong></th>
<th align="left"><strong>30° Incidence Angle</strong></th>
<th align="left"><strong>60° Incidence Angle</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Slant Range</td>
<td align="left">0.50 m</td>
<td align="left">0.50 m</td>
</tr>
<tr>
<td align="left">Ground Range</td>
<td align="left">1.00 m</td>
<td align="left">0.58 m</td>
</tr>
</tbody>
</table>
</figure>

While slant range resolution seems “better” than ground range resolution, keep in mind that it refers to the sensor’s ability to discriminate features along the oblique path of the emitted energy. Most of the features we care about lie along the ground surface, and thus ground range resolution is more useful in describing image resolution.

Note that while slant range resolution is the same in both the near and the far range, ground range resolution is highest in the far range and degrades toward the near range. This is because incidence angle is smallest (the line of sight is most vertical) in the near range, and largest (the line of sight is most horizontal) in the far range.

The practical difference between near and far range depends on the incidence angle range of the imaged scene. For example, if the imaged swath spans from 20° to 45° incidence, the ground range resolution may vary by a factor of around 2.

Finally, topography in the scene also impacts incidence angles. Ground range resolution is better for the areas of slopes that descend away from the satellite, and worse for the slopes facing the satellite.

## 6.4) Spatial Resolution and Impulse Response

At this point, we have introduced three measures of resolution: azimuth, slant range, and ground range resolution. In this section, we discuss spatial resolution in more detail to clarify the concept.

### 6.4.1 Spatial Resolution

<span class="underline">Spatial resolution</span> refers to the ability to distinguish individual features or objects on the ground as separate and distinct. It combines the effects of both azimuth and ground range resolution, since these two dimensions together define the radar's resolving power across an image, and ultimately define the level of detail in a SAR image.

Armed with our new understanding of phase history data, PRF, chirped pulses, and bandwidth, let us return to the concepts of azimuth and slant range resolution. Although they are independent of each other, the calculations for the azimuth and range dimensions have a fundamental similarity:

  - Azimuth resolution is based on phase variations across the collection interval. These are compared to known phase variations across that area to produce a long “synthetic” aperture and a resolution cell narrow in azimuth.

  - Range resolution is based on frequency variations across the returned pulse. These are compared to known frequency variations in the reference pulse to produce a short “synthetic” pulse and a resolution cell narrow in range.

The resulting equations are two of the most simple and powerful in all of remote sensing:

\[\delta{}_{\text{az}} = \frac{\lambda}{2\Delta\theta}\]

\[\delta{}_{\text{sr}} = \frac{c}{2B}\]

With 𝛿<sub>az</sub> and 𝛿<sub>sr</sub> being the azimuth resolution and the slant range resolution, respectively.

Now, as explained in Section [<span class="underline">6.3</span>](#63-ground-range-resolution-and-incidence-angle), the latter equations must be updated to account for incidence angle to derive spatial resolution at the ground plane. Thus we need the equation for the ground range resolution:

\[\delta{}_{\text{gr}} = \frac{\delta{}_{\text{sr}}}{\sin\theta}\]

Now, spatial resolution is the product of 𝛿<sub>az</sub> and 𝛿<sub>gr</sub>.

### 6.4.2 Impulse Response

Let us return to the concept of beamwidth and antenna propagation patterns discussed in Section [<span class="underline">4.2</span>](04_antennas_and_sar_geometry.md#42-beamwidth-and-illumination-power) to deepen our technical understanding of spatial resolution. Typically, the spatial resolution of a SAR system is defined by the half-power beamwidth of the system’s impulse response. The <span class="underline">impulse response (IPR)</span> describes how an ideal point-like target would appear in a SAR image. It reflects the actual resolution capability of the system and for operational systems it is commonly measured using small, highly reflective objects like metal spheres or trihedral corner reflectors. The IPR is typically represented as an <span class="underline">impulse response function (IRF)</span> – a two-dimensional impulse response (backscatter) energy profile, in the slant range and azimuth dimensions. The profile has a main lobe – this is the sharp peak at the center, which represents the concentrated energy of the backscatter signal, and smaller sidelobes, which represent energy spread outside the main response. When plotted on a two dimensional graph it looks quite similar to the antenna propagation patterns shown in Figure [<span class="underline">4.2</span>](04_antennas_and_sar_geometry.md#figure-4.2-antenna-propagation-patterns), but a more detailed illustration is provided in Figure [<span class="underline">6.6</span>](#figure-6.6-impulse-response-function-quality-parameters) below.

The widths of the main lobe in the two dimensions ultimately determine the system’s practical azimuth, range and spatial resolutions, because these widths represent the smallest separation of point targets that results in non-overlapping response profiles, thus setting the lower boundaries for the corresponding resolutions. A narrow pillar-like peak in the IRF indicates high resolution, as it means the radar system can sharply localize the return from a target.

<figure id="figure-6.6-impulse-response-function-quality-parameters">
<img src="https://github.com/sjjsy/product-documentation/releases/download/additional-assets-test/image30.png">
<figcaption><strong>Figure 6.6: Impulse Response Function (IRF) Quality Parameters.</strong></figcaption>
</figure>

Note that the IRF is often asymmetric: Typically, the main lobe is wider in the range dimension than in the azimuth dimension, reflecting the fact that range resolution is limited by transmitted bandwidth while azimuth resolution depends on the synthesized aperture length and processing. In some SAR modes, such as Spotlight, the azimuth IRF can become narrower than the range IRF due to extended dwell time and greater synthetic aperture, whereas in wide-swath or ScanSAR modes the opposite is often true.

The <span class="underline">Peak Sidelobe Ratio (PSLR)</span> and the <span class="underline">Integrated Sidelobe Ratio (ISLR)</span> are two commonly used metrics for quantifying the shape of the impulse response and, consequently, the system’s image sharpness and focus quality. The PSLR measures the ratio between the peak amplitudes of the strongest sidelobe at the left and right relative to the mainlobe, while the ISLR compares the total energy contained in all sidelobes to that within the mainlobe.

For more information on this topic, refer to Article [<span class="underline">5</span>](../techdocs/05_resolution_and_impulse_response_function_quality_parameters.md) in the Technical Documentation, which provides more explanation on the derivation of PSLR, ISLR and other spatial resolution related quality parameters.

Lower PSLR and ISLR values indicate better sidelobe suppression, meaning that strong targets are less likely to contaminate nearby weaker signals. Typical operational SAR systems achieve PSLR values of around -20 dB (which is equal to 0.1) and ISLR values near -10 dB (also 0.1, since this is a power ratio while the former was an amplitude ratio; See the note in Section [<span class="underline">7.3</span>](07_separating_signals_from_noise.md#73-the-challenge-of-noise-and-the-power-of-processing-gains) for a recap on the decibel scale).

### 6.2.3 Pixel Spacing

The shape of the impulse response — defined by its mainlobe width and sidelobe levels, as characterized by the PSLR and ISLR — ultimately determines the system’s true spatial resolution. It describes how distinctly the radar system can separate the returns from closely spaced point targets. When the radar image is processed, this continuous response must be represented as a discrete grid of pixels on the ground.

Here, it is important to understand that resolution and pixel spacing are not the same thing. Resolution is governed by the impulse response and reflects the radar’s physical ability to distinguish separate scatterers, whereas <span class="underline">pixel spacing</span>—the physical distance between the centers of adjacent pixels on the ground—is simply a sampling choice made during image formation. According to the Nyquist criterion, the pixel spacing must be smaller than the resolution to ensure that the full detail of the impulse response is captured without loss of information. Choosing a finer pixel spacing can improve the smoothness and visual quality of the image, but it does not increase the true resolving power of the radar — the impulse response width remains the same, only sampled more finely.

Because radar resolution is often asymmetric (typically finer in azimuth than in range) the data are usually resampled onto a grid with <span class="underline">uniform pixel spacing</span> in ground range and azimuth coordinates. This produces a visually balanced image and simplifies further analysis, even though the underlying physical resolution remains directionally dependent. The resampling process interpolates between the original radar samples without creating new detail, preserving the inherent system resolution while harmonizing the image geometry.

### 6.2.4 Nominal Resolution

Finally, let’s discuss <span class="underline">nominal resolution</span> which is an important metric for consumers of remote sensing data to understand. Because achieved ground resolution varies across images based on factors such as terrain and incidence angle, most SAR imagery providers specify an average or best-case resolution within a theoretical swath that is supposed to represent the most typical or intended imaging scenario.

## 6.5) Geolocation, Geospatial Accuracy and Orthorectification

In Earth observation, having adequate resolution is important—but it's only part of the picture. To truly unlock the value of a SAR image, typically we also need to know exactly where on Earth that image is located. In other words, it's not enough to see fine detail, we must also know where each pixel belongs on the globe.

### 6.5.1 Geolocation

Accuracy is especially important when SAR images are used in combination with other geographic data—such as maps, satellite imagery, or geospatial layers in a <span class="underline">Geographic Information System (GIS)</span>. For example, a SAR image might be just one piece of a larger mosaic of overlapping images, or it might be used to monitor changes at a specific location over time. In all these cases, we must accurately align the SAR image to a geographic model of the Earth. This process is called <span class="underline">geolocation</span>, and the precision with which we can assign real-world coordinates to each image pixel is known as <span class="underline">geospatial accuracy</span>. Without good geolocation, even the sharpest image may be of limited use.

Geolocation, geolocation accuracy and geospatial accuracy are central concepts in GIS that are also related to spatial resolution. <span class="underline">Geolocation</span> is the process of determining the geographic coordinates (latitude, longitude, and altitude) of a point or object on the Earth’s surface in relation to a specific geographic coordinate system. In SAR, <span class="underline">geolocation accuracy</span> refers to the precision with which such coordinates of an object or point on the Earth can be determined based on where it appeared in a SAR image. The precise geolocation of points in a SAR image requires precise knowledge of the radar’s flight path, orientation, and timing information from the imaging, as well as the use of an accurate digital elevation model (DEM) of adequate resolution, which is very important for improving accuracy in uneven terrain. Naturally, high resolution data is also a prerequisite for high geolocation accuracy.

While an Earth ellipsoid model (EEM, introduced in Section [<span class="underline">10.5</span>](10_data_products.md#105-projection-surfaces)) models the general elliptic shape of the Earth, a topographic surface or <span class="underline">Digital Elevation Model (DEM)</span> is a numerical representation of the Earth’s surface that contains actual height points (altitude or elevation above sea level) representing the topography.

### 6.5.2 Geospatial Accuracy

<span class="underline">Geospatial accuracy</span> includes both absolute location accuracy (how close a mapped pixel is to its true ground location) and relative accuracy (how consistently distances and spatial relationships are preserved within and across images). In practice, geospatial accuracy in SAR depends on a chain of factors: precise orbit and timing knowledge, accurate range and azimuth measurement modeling, high-quality elevation data for terrain projection, and consistent geometric calibration of the sensor and processing chain.

For practical interpretation, five contributors are especially important. First, <span class="underline">orbital information accuracy</span>: satellite position and velocity must be known with high precision. Second, <span class="underline">range and azimuth measurement accuracy</span>: residual timing offsets, instrument delays, and Doppler modeling errors directly propagate to pixel position errors. Third, <span class="underline">digital elevation model (DEM) quality</span>: because SAR is side-looking, vertical elevation uncertainty can produce significant horizontal displacement after projection. Fourth, <span class="underline">ground control and calibration</span>: robust accuracy quantification requires comparison against precisely surveyed reference targets (for example corner reflectors). Fifth, <span class="underline">map-based validation limitations</span>: when surveyed ground truth is unavailable, comparisons against reference maps can be useful, but the estimate then also includes errors from the reference data and feature-matching subjectivity.

These concepts are summarized here at a high level; detailed definitions, equations, and validation methodology (including ALE, RMSE, CE90, and the measurement procedure) are provided in Technical Documentation Article [<span class="underline">1</span>](../techdocs/01_geospatial_considerations.md), with campaign-level result examples in Article [<span class="underline">2</span>](../techdocs/02_geolocation_accuracy_validation_campaigns.md).

It is key to point out that geospatial accuracy cannot be measured in a single SAR image—we will discuss why in Section [<span class="underline">6.5.5</span>](#655-accuracy-limitations). Still, users may want to assess the position of a SAR image relative to its true location. The five contributors listed above are the primary factors to consider when estimating geospatial accuracy.

### 6.5.3 Geospatial Rational Polynomial Coefficients

SAR image products include <span class="underline">Rational Polynomial Coefficients (RPCs)</span> in their metadata. These are compact mathematical models that provide a fast and efficient way to convert between geographic coordinates (latitude, longitude, and elevation) and image coordinates (pixel and line). With RPCs, it's possible to accurately map ground locations onto the radar image—or vice versa—without needing to perform complex geometric transformations or image warping. This makes RPCs especially useful for quick geolocation tasks, image alignment, or integrating SAR data into GIS environments.

### 6.5.4 Orthorectification

<span class="underline">Orthorectification</span> is the process of geometrically warping a SAR image so that every pixel corresponds to a precise geographic location—a specific latitude, longitude, and elevation—on the Earth’s surface. This is achieved by warping the image to align with a Digital Elevation Model (DEM) and geographic map coordinates, correcting for terrain-induced distortions. The result is an orthorectified image that displays correct spatial relationships and can be easily overlaid with other map layers or used in geographic information systems (GIS). Figure [<span class="underline">6.7</span>](#figure-6.7-process-of-orthorectification) illustrates steps in the orthorectification process.

<figure id="figure-6.7-process-of-orthorectification">
<img src="https://github.com/sjjsy/product-documentation/releases/download/additional-assets-test/image29.png">
<figcaption><strong>Figure 6.7: Process of Orthorectification.</strong></figcaption>
</figure>

This correction can be performed using Rational Polynomial Coefficients (RPCs) and a DEM, which together allow us to map the radar geometry of the image onto a real-world coordinate system. However, the geospatial accuracy of the orthorectified image depends heavily on the accuracy of the DEM, especially its vertical precision. Even small height errors can lead to significant horizontal shifts in areas with steep terrain. See Figure [<span class="underline">6.8</span>](#figure-6.8-an-animated-illustration-of-orthorectification) for an animation of the gradual orthorectification of an example image and the various shifts that are required to make the image and orthoimage.

<figure id="figure-6.8-an-animated-illustration-of-orthorectification">
<img src="https://github.com/sjjsy/product-documentation/releases/download/additional-assets-test/image31.png">
<figcaption><strong>Figure 6.8: An Animated Illustration of Orthorectification.</strong> This animation shows an optical image captured by the first commercial high-resolution optical Earth imaging satellite IKONOS being orthorectified gradually in several steps. The orthorectification of optical and SAR images is essentially the same, except that with SAR images there is no need to check for possible distortions due to suboptimal lighting or weather conditions during image acquisition.</figcaption>
</figure>

It's also important to note that while orthorectification can make SAR imagery easier to interpret in a geographic context, it also alters some of the inherent geometric features of radar images. For example, effects like layover and foreshortening (discussed in later sections) may be distorted or suppressed, which may remove useful information about the structure of the scene. So while an orthorectified image is useful for visualization and mapping, it does not preserve all radar-specific characteristics and should be used with care depending on the application. Keep in mind that geometric distortions from shadow and layover cannot be removed with orthorectification.

### 6.5.5 Accuracy Limitations

Geolocation and geospatial accuracy are often reported using a statistical measure called <span class="underline">Root Mean Square (RMS) error</span>. This value represents the average deviation between the known true locations of targets on the ground and the locations estimated from the SAR image, accounting for both systematic and random errors.

To measure geospatial accuracy in practice, SAR images are acquired over specific calibration sites—areas where well-characterized targets, such as corner reflectors, have been installed at precisely known locations, typically determined using high-precision GPS. By detecting these reflectors in the SAR image and calculating their estimated geographic coordinates, we can then compare those results to the true ground positions. The differences between the measured and actual positions give us a direct assessment of geospatial accuracy.

Because a single image may be affected by various random factors—such as orbital position errors, atmospheric conditions etc.—one measurement is not enough. This is why a user cannot measure RMS error for a single SAR image. To obtain a reliable and stable estimate, this process is repeated over many images and passes. The RMS error is then calculated as the square root of the average of the squared position errors across all measurements. This single number provides a meaningful summary of the system’s overall geospatial accuracy. This is why you cannot measure, only estimate, geospatial accuracy in a SAR image.

Chapters [<span class="underline">1</span>](../techdocs/01_geospatial_considerations.md) (Geospatial Considerations) and [<span class="underline">2</span>](../techdocs/02_geolocation_accuracy_validation_campaigns.md) (Geolocation Accuracy Validation Campaigns) in the Technical Documentation discuss these concepts, and how their values are calculated, in more detail. The latter section also provides a geospatial accuracy report by ICEYE.

### 6.5.6 Co-Registration

Finally, to reduce risk of confusion, let’s quickly tackle the term co-registration which is sometimes mistaken for georegistration (georeferencing). <span class="underline">Co-registration</span> is the process of aligning two or more images to each other such that each pixel across all images corresponds to the same physical location on the scene. <span class="underline">Georegistration</span> is the process of assigning real-world geographic coordinates (latitude, longitude, elevation) to pixels in an image, usually using external data.

Coregistration is usually performed to prepare images for comparative analysis (see ACD, InSAR or CCD in Section [<span class="underline">9.8</span>](09_data_processing_and_analysis.md#98-other-phase-based-techniques)) where sub-pixel matching accuracy might be required. For best results, the images need to have very similar collection geometries and imaging parameters. Although information like image features, satellite orbit data, and terrain models can help improve the accuracy of alignment, it’s still possible to co-register multiple SAR images without knowing their exact location, provided the images look similar enough that the alignment algorithm can match the same patterns in each one.

Co-registration is fundamentally different from georegistration, but perfectly georegistered images with the same resolution over the same area should also essentially be co-registered.

Accurate and precise co-registration is required for advanced SAR use cases such as Amplitude Change Detection and Coherent Change Detection.

!!! history

    To conclude this chapter, it must be acknowledged that developing and implementing a SAR system that can produce high resolution imagery that can be accurately orthorectified has been possible only during the last decades due to the advanced sensors and other hardware, algorithms and computational processing power and numerous system design insights that are required but which have been made possible by the incessant hard work of numerous scientists and engineers. Arguably the most seminal of those is Carl A. Wiley, a mathematician and engineer who, while working as the engineer-in-charge at Goodyear Aerophysics, invented synthetic aperture radar in 1951 and later patented it under the title “Pulsed Doppler Radar Methods and Means”.
