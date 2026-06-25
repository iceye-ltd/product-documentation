# 7\) Separating Signals from Noise

!!! summary inline end

    - Radar signals weaken dramatically with distance, decreasing with the square of range—once on transmission, and again on reception—resulting in extremely faint returns that must be separated from system noise.

    - Noise arises primarily from random thermal emissions within the receiver and antenna system but also from external sources, creating a noise floor that competes with weak echoes; thermal noise power is proportional to bandwidth, so increasing bandwidth improves range resolution but also raises the noise baseline.

    - Radar Cross Section (RCS) quantifies a target’s effective reflectivity or detectability, and Normalized RCS (NRCS) is essentially RCS divided by illuminated target size, so high-NRCS targets appear brighter in SAR images.

    - Noise Equivalent Sigma Zero (NESZ) expresses the minimum detectable backscatter level above system noise, with lower NESZ values indicating better sensitivity; high NESZ systems clearly show only the brightest targets.

    - Radiometric resolution describes the system's ability to distinguish different backscatter intensities, with quantization and dynamic range trade-offs affecting how continuous analog measurements are converted to discrete digital values.

    - The Radar Range Equation (RRE) and the Signal-to-Noise Ratio (SNR) integrate key radar parameters to quantify received signal power and clarity as functions of transmitted power, antenna gains, wavelength, target radar cross section, distance, as well as system losses and noise.

    - Modern SAR systems overcome weak-signal challenges through both hardware and processing innovations, including pulse compression (concentrating chirped pulses into sharp peaks) and coherent integration (summing successive echoes constructively so coherent signals rise above incoherent noise).

In order for a signal to be recognized and utilized, it must be distinguishable from background and system noise. Indeed, as defined already in Section [<span class="underline">4.2</span>](04_antennas_and_sar_geometry.md#42-beamwidth-and-illumination-power), an essential measure is the <span class="underline">Signal-to-Noise Ratio (SNR)</span> which describes the strength and clarity of the desired signal in the backscatter, relative to noise. Radar imaging is the advanced science of sending out electromagnetic signals and then separating their faint reflections from noise to build an image of the scene.

We start this chapter by presenting the Radar Range Equation and its Signal-to-Noise Ratio form as they provide a physics-based framework for understanding radar performance, and a structure for this chapter. Albeit heavy, the equations powerfully integrate essential factors and learnings from previous chapters with the ones that are yet to be tackled in this one. The subsequent sections dive deeper into the impact of range, and system losses and noise, and how these are countered. Finally, we define a central measure of sensitivity and noise performance, the Noise Equivalent Sigma Zero and related terms, and finish by exploring radiometric resolution and related digital implementation challenges.

## 7.1) The Radar Range Equation and the Signal-to-Noise Ratio

Let us examine the standard <span class="underline">Radar Range Equation (RRE)</span> which is presented below in three forms:

\[P_{r} = \frac{P_{t}G_{t}A_{r}\sigma}{(4\pi)^{2} R_{t}^{2} R_{r}^{2} L}\]

\[P_{r} = \frac{P_{t}G_{t}G_{r}\lambda^{2}\sigma}{(4\pi)^{3} R_{t}^{2} R_{r}^{2} L}\]

\[P_{r} = \frac{P_{t}G^{2}\lambda^{2}\sigma}{(4\pi)^{3} R^{4} L}\]

The equation may seem daunting, but most terms have already been discussed in previous chapters. Let’s dive into understanding the rest: The first expression describes the expected received signal power \(P_{r}\) as a function of \(P_{t}\) or the power of the transmitted pulse (both in Watts), \(G_{t}\) or the gain of the transmitting antenna (see Section [<span class="underline">4.1</span>](04_antennas_and_sar_geometry.md#41-active-phased-array-antennas-boresight-and-gain)), \(A_{r}\) or the effective aperture of the receiving antenna (see Section [<span class="underline">1.1</span>](01_introduction.md#11-radar-imaging-antenna-aperture-and-beamwidth)), \(\sigma\) or the radar cross section or scattering coefficient of the target (this will be discussed in Section [<span class="underline">7.4</span>](#74-noise-equivalent-sigma-zero-and-the-radar-cross-section)), \(R_{t}\) and \(R_{r}\) which are the distances travelled by the signal from the transmitter to the target, and then from the target to the receiver, respectively, and \(L\) or the system loss coefficient (to be discussed in Section [<span class="underline">7.2</span>](#72-fading-pulse-power-and-system-losses)).

The second expression substitutes the (instantaneous) effective aperture with a term that includes \(G_{r}\) or the gain of the receiving antenna and \(\lambda\) or the wavelength of the transmitted signal, effectively translating the equation from the geometric view (effective aperture area) to the electric view (effective antenna gain).

Finally, the third form is a simplified approximation for monostatic radar applications where it is assumed that both the antenna gain and the distance travelled by the signal are either identical or so similar for both transmission and receipt that they can be represented with single variables \(G\) and \(R\).

While these standard RRE forms give us the received signal power (in absolute Watts), what is often more interesting is the <span class="underline">Signal-to-Noise Ratio (SNR)</span>. The SNR is the ratio of backscatter signal power to receiver noise power or so-called noise floor and it must be higher than 1:1 in order for scatterers and other targets in the scene to be distinguishable in the image.

The SNR can be solved from the above monostatic RRE equation by dividing both sides of the equation with \(P_{n}\), the average noise power:

\[\text{SNR} = \frac{P_{s}}{P_{n}} = \frac{P_{t}G^{2}\lambda^{2}\sigma}{(4\pi)^{3} R^{4} L k T B F_{n}}\]

In the equation, the term \(P_{r}\) is also renamed as \(P_{s}\) to emphasize the word signal over mere receipt, and on the right side the average noise power term is further substituted according to the following equation:

\[P_{n} = \text{kTB}F_{n}\]

Here, \(k\) is Boltzmann's constant, a fundamental physical constant related to thermal energy, \(T\) is the system noise temperature, \(B\) is the receiver pulse bandwidth (see Section [<span class="underline">6.2</span>](06_spatial_resolution_and_geospatial_accuracy.md#62-range-resolution-pulse-chirping-and-pulse-bandwidth)), and \(F_{n}\) is the receiver noise factor. The \(\text{kTB}\) represents the thermal noise baseline that is inherent to all radar systems while \(F_{n}\) is the so-called noise factor which represents the further noise generated within the receiver hardware.

Now, by looking at the SNR equation, we can conclude the following: To maximize signal clarity, we should work to maximize the factors in the numerator while minimizing those in the denominator.

Signal transmit power and antenna gain were already discussed in Section [<span class="underline">4.2</span>](04_antennas_and_sar_geometry.md#42-beamwidth-and-illumination-power). In Chapter [<span class="underline">6</span>](06_spatial_resolution_and_geospatial_accuracy.md), we learned that increasing wavelength would have the often undesirable effect of reducing resolution. And of course, in Earth Observation, we cannot generally influence the reflectivity and radar visibility (\(\sigma\)) of our targets.

Thus, the next two sections will focus on dissecting the terms in the denominator: Section [<span class="underline">7.2</span>](#72-fading-pulse-power-and-system-losses), will elaborate on the terms that were also in the RRE, and which reduce signal power: the relentless impact of range, and the further impact of various system losses. Thereafter, in Section [<span class="underline">7.3</span>](#73-the-challenge-of-noise-and-the-power-of-processing-gains), we will focus on the factors that increase noise, but also how clever SAR engineers counter the balance in our favor.

## 7.2) Fading Pulse Power and System Losses

Notice that in both the monostatic RRE and the corresponding SNR equation presented in Section [<span class="underline">7.1</span>](#71-the-radar-range-equation-and-the-signal-to-noise-ratio), the distance between the radar and the target diminishes the energy intensity of the received backscatter signal in the fourth power\! This means that doubling the distance reduces the received signal strength by a factor of 16\!

Indeed, as a radar pulse travels from the antenna to the ground surface its total energy remains constant. However, as the pulse moves away from the antenna, it spreads out into space and its power density weakens, as introduced in Section [<span class="underline">4.2</span>](04_antennas_and_sar_geometry.md#42-beamwidth-and-illumination-power). As shown in Figure [<span class="underline">7.1</span>](#figure-7.1-expanding-surface-area-of-a-pulse), it is as if the “skin” of the pulse becomes thinner with distance- like blowing up a balloon. This weakening is dramatic; it decreases with the square of the distance from the antenna.

<figure id="figure-7.1-expanding-surface-area-of-a-pulse">
<img src="https://github.com/sjjsy/product-documentation/releases/download/additional-assets-test/image31.png">
<figcaption><strong>Figure 7.1: Expanding Surface Area of a Pulse.</strong></figcaption>
</figure>

Given that the ground might be 750 km from the antenna, the pulse is very weak by the time it finally reflects from surface objects. The returning, already weakened pulse is weakened yet again with the square of the distance. By the time the backscatter microwaves return to the antenna, they are microscopically faint.

However, as shown by the RRE and SNR equations, the signal power is not only weakened simply by its geometric spreading over distance: Along with the term \(R⁴\) in the denominator, there is also the term \(L\), which is the <span class="underline">system loss coefficient</span>. It represents all other mechanisms that reduce the effective received signal power. These include propagation and hardware related losses, such as antenna feed inefficiencies and atmospheric absorption that weaken the transmitted signal before it reaches the receive signal detector. In some contexts, the term is also considered to include post-detection losses due to factors like imperfect signal processing. Such losses, along with the relentless effect of long ranges, drastically reduce the effective signal pulse power and thus lower the SNR.

## 7.3) The Challenge of Noise and the Power of Processing Gains

Backscattered microwaves are so weak when they arrive at the antenna that they are easily perturbed by various sources of noise. This brings us to the third and last non-constant term in the denominator, the average noise power term \(P_{n}\). In Section [<span class="underline">7.1</span>](#71-the-radar-range-equation-and-the-signal-to-noise-ratio), \(P_{n}\) was broken down into two parts:

The first part of \(P_{n}\) is \(\text{kTB}\), which represents the <span class="underline">thermal noise baseline</span> that limits all radar receivers. In radar engineering, the term “temperature” does not refer only to the physical warmth of the electronics, but to the <span class="underline">system noise temperature</span> — the combined effect of all random electromagnetic energy affecting the receiver. It consists of the <span class="underline">receiver noise temperature</span>, which represents the thermal noise generated by internal electronics, and the <span class="underline">antenna noise temperature</span>, which represents random microwave emissions and background radiation received by the antenna.

One of the tenets of remote sensing is that all objects emit electromagnetic energy based on their temperature, due to the random motion of electrons and molecules. This random emission is the physical origin of <span class="underline">thermal noise</span>, and it spans all frequencies, including the microwave bands used in SAR, and forms the <span class="underline">noise floor</span> that competes with the faint radar echoes reflected from the Earth’s surface. As indicated by the equation, this noise baseline is unfortunately proportional to temperature and receiver bandwidth, as a broader bandwidth receiver also unavoidably receives a broader span of noise.

The second part of \(P_{n}\) is the receiver’s <span class="underline">noise factor</span> \(F_{n}\), which accounts for the additional noise generated internally by the receiver that exceeds the unavoidable thermal baseline.

Together, thermal noise and these additional contributions generated within the receiver constitute <span class="underline">internal noise</span>. By contrast, the term <span class="underline">external noise</span> refers to noise that originates outside the receiver, and corresponds largely with the other half of the previously defined system noise temperature, the antenna noise. Cosmic background radiation, solar bursts, atmospheric discharges, as well as radio-frequency interference (RFI) from human transmitters can all enter the radar through the antenna and are sometimes indistinguishable from genuine echoes. However, in SAR-based Earth observation, external noise is usually a lesser problem when compared with internal noise. For modern high-quality spaceborne SAR receivers, the noise factor is typically in the range 1.5-2.0, and is often expressed as a <span class="underline">noise figure</span>, in decibels, with which the corresponding range becomes 1.8 - 3 dB.

For comparison, the thermal noise power of a spaceborne SAR system viewing the Earth can be between -70 and -90 dBm (decibel-milliwatts), depending on bandwidth and other design parameters. Assuming a thermal noise power of -83 dBm and a noise figure of 3 dB we get a total noise of -80 dBm which equals 10 pW (picowatts) or \(10^{- 11}\) W. While the additional receiver noise may double the total noise power, in the big picture its effect is quite minor, as it is the thermal baseline that sets the stage in the logarithmic scale.

!!! note inline end

    The <span class="underline">decibel (dB)</span> is a logarithmic unit that expresses the ratio between two values, commonly used for power and amplitude measurements in radar and signal processing. By definition, two signals whose levels differ by one decibel have a power ratio of \(10^{\frac{1}{10}} \approx 1.26\) or root-power ratio of \(10^{\frac{1}{20}} \approx 1.12\). It follows that, for power ratios, a 10 dB change corresponds to a tenfold increase or decrease, but for amplitude (root-power) ratios, such an increase or decrease requires a 20 dB change, since power is proportional to the square of amplitude. Similarly, a 3 dB change translates to a doubling or halving of a power quantity as \(10^{\frac{3}{10}} \approx 2.00\), or an increase or decrease by a factor of \(\sqrt{2}\) of an amplitude quantity. This logarithmic scaling simplifies the comparison of SAR parameters where values can span many orders of magnitude, like noise levels (as discussed here), and NESZ, backscatter intensity and dynamic range (which will be discussed later in this chapter).

The challenge of noise in SAR is mitigated through a combination of clever system design, antenna performance, and signal processing engineering. System design trade-offs—such as higher power transmitters and larger antennas (see Chapter [<span class="underline">4</span>](04_antennas_and_sar_geometry.md)), lower orbital altitudes (see Section [<span class="underline">5.5</span>](05_collection_strategies.md#55-altitude-independence)), steeper incidence angles (see Section [<span class="underline">6.3</span>](06_spatial_resolution_and_geospatial_accuracy.md#63-ground-range-resolution-and-incidence-angle)), and cooler, more efficient and noise-free receivers—help strengthen the received echoes relative to noise and thus improve SNR and image quality.

Beyond these physical measures, SAR systems achieve substantial <span class="underline">processing gains</span> that are not explicit in the standard forms of the radar range and SNR equations but which have already been discussed in previous chapters, and which increase SNR by orders of magnitude. Indeed, two multipliers are sometimes added to them to make the impact of these innovations explicit:

The first multiplier, \(G_{p} = \tau B\), represents the effect of <span class="underline">pulse compression</span>: Longer, frequency-modulated and compressed pulses can carry many times the energy of shorter, unmodulated pulses of the same peak power, as was explained in Section [<span class="underline">6.2</span>](06_spatial_resolution_and_geospatial_accuracy.md#62-range-resolution-pulse-chirping-and-pulse-bandwidth). This positive effect can be approximated by the time–bandwidth product as shown in the equation above. The magnitude of this effect may be 30-50 dB, depending on pulse bandwidth, PRF and other parameters. Such multiplication is impactful\!

The second multiplier, \(G_{i} = N\), represents the effect of <span class="underline">coherent integration</span>: Each additional aperture position from which another coherent pulse is successfully integrated contributes constructively to increase the signal-to-noise ratio with an integration gain roughly proportional to the number of combined samples, represented simply with the letter \(N\) in the equation. This founding principle of SAR was discussed especially in Chapter [<span class="underline">1</span>](01_introduction.md) and Section [<span class="underline">6.1</span>](06_spatial_resolution_and_geospatial_accuracy.md#61-azimuth-resolution-phase-history-data-and-prf). Its impact to SNR might be in the 20-40 dB range, with the highest multiplier values being possible with long dwell duration Spotlight collections.

Together, these innovative mechanisms act as powerful multiplicative gain factors that allow SAR to reveal targets far, far below the instantaneous noise floor: A scatterer that reflects signals that would otherwise be a whopping -30 dB of the noise floor, that is, with only one thousandth of the baseline noise power, can be separated and made “loud and clear” thanks to powerful data processing\!

This is why research in improving SAR performance is not only about hardware, but also about clever algorithmic and processing innovation. Improving phase coherence across long synthetic apertures, for instance, is still a topic of research, as such innovations have and can still lead to significant improvements in SNR and thus SAR image quality\!

With this understanding, the next two sections will introduce further concepts which complement this topic of separating signals from noise, and which often appear in related materials.

## 7.4) Noise Equivalent Sigma Zero and the Radar Cross Section

One of the ways that noise and backscatter signal sensitivity is quantified for SAR sensors is with a parameter called <span class="underline">Noise Equivalent Sigma Zero (NESZ)</span>. It describes the backscatter level that produces the same power level at the receiver as the system noise. All received signals have to be stronger than the NESZ value to rise above the noise level to become distinguishable. Therefore, it is best for NESZ to be as low as possible. Images with very high NESZ values look noisy and have worse visual quality, because even the strongest signals have barely surpassed the system noise floor.

NESZ can be derived from the radar equation (presented in Section [<span class="underline">7.1</span>](#71-the-radar-range-equation-and-the-signal-to-noise-ratio)), where sigma or \(\sigma\) symbolizes the radar cross section. NESZ is specifically defined to represent the minimum detectable normalized radar cross section, \(\sigma^{0}\), that scatterers must exceed in order to surpass the system noise baseline and become discernible. <span class="underline">Radar Cross Section (RCS)</span> or <span class="underline">radar signature</span> or <span class="underline">sigma</span> (\(\sigma\)) is a measure of the radar detectability or reflectivity of a target. The RCS is quantified as the hypothetical *effective area*, denoted in square meters (m²) or dBsm (decibel relative to a square meter), that would be required as the cross-sectional area of an isotropic (or uniform) reflector, such as a smooth solid metal sphere, in order for it to produce equal backscatter power with the actual target. The RCS depends on target size, shape and orientation relative to the radar, as well as the properties of both the target’s surface material and the radar signal. For example, the RCS of a pine tree might be 0.1-1.0 m² (-10 to 0 dBsm) while that of a large cargo ship could be 100 000 m² (50 dBsm).

<span class="underline">Sigma nought</span> (\(\sigma^{0}\)) or <span class="underline">Normalized Radar Cross-Section (NRCS)</span> is also a measure of the reflectivity of a target, but it is referred to as a <span class="underline">radar backscatter coefficient</span>, because it is the ratio of the received power to the incident power, normalized to the target's physical area, and is thus typically given in square meters per square meter (m²/m²). Because it is the RCS per unit area, it does not depend on target size or shape, but it does depend on the target’s surface properties and their interaction with the used radar signal, and also incidence angle, which can greatly affect scattering. NRCS is useful when analyzing different scatterers in a scene to predict how they will appear in a radar image. For example, the X-band radar NRCS values are very high for passenger airplanes and cars, and very low for grasslands and water bodies. Indeed, the NRCS for a calm pond might be -30 dB, whereas it could be 10 dB for a passenger car, yielding a contrast of about 40 dB, or a 10 000 fold difference in backscatter intensity. Scattering and factors that affect NRCS values are explored further in Section [<span class="underline">8.2</span>](08_sar_imagery_and_interpretation_considerations.md#82-backscatter-polarization-and-scattering-mechanisms).

Now that we understand RCS and NRCS, let us dive back into the radar sensitivity metric: NESZ defines the reference σ⁰ value that corresponds to an SNR of 1 (or 0 dB, as they are equal) for a specific radar system under standard conditions. You can think of NESZ as a system-level, calibration-derived equivalent of 0 dB SNR, standardized to σ⁰ units, determined under realistic operational conditions.

Modern spaceborne SAR systems typically boast NESZ values in the -4 to -24 dB m²/m² range. For example, a NESZ of -24 dB m²/m² means that the system’s baseline noise power is \(10^{\frac{- 24}{10}} \approx 0.40\mathrm{\%}\) of the reference NRCS of an idealized metal sphere. Conversely, -4 dB m²/m² corresponds to roughly 40%. The difference between these two extremes represents a sixteenfold change in effective sensitivity: With the latter, the backscatter from the metal sphere would be only a little over two times stronger than the system noise baseline, which makes it barely distinguishable, but with the former it would exceed the baseline 250-fold\!

NESZ values are influenced by antenna size and other hardware, the collection method including the imaging geometries applied, and data processing. However, the bandwidth of the radar system is also a direct and significant influence. Therefore, there are differences across the different imaging strategies. While Spotlight mode achieves finer spatial resolution, its wider signal bandwidth admits more thermal noise, often yielding NESZ values around -4 to -18 dB. In contrast, Stripmap and ScanSAR modes may achieve better NESZ, values ranging from -20 to -23 dB, due to their use of lower bandwidths and other trade-off choices. Thus, despite offering lower resolution, they might provide “cleaner” images.

Table [<span class="underline">7.1</span>](#table-7.1-detectability-of-different-targets-in-sar) provides examples of several example targets and estimates of their respective RCS and NRCS values and visibility at two different NESZ thresholds. However, note that the visibility estimates in the table assume high enough resolution and other imaging parameters necessary for imaging each target. The estimates qualitatively indicate how far above (or below) the system NESZ each target’s effective NRCS is likely to be, assuming typical incidence angles. Section [<span class="underline">8.2</span>](08_sar_imagery_and_interpretation_considerations.md#82-backscatter-polarization-and-scattering-mechanisms) explains further how and why NRCS values vary between different targets. Please note the values in the table are estimates, and not diagnostic values.

<figure id="table-7.1-detectability-of-different-targets-in-sar">
<figcaption><strong>Table 7.1: Detectability of Different Targets in SAR.</strong></figcaption>
<table>
<thead>
<tr>
<th align="left"><strong>Target</strong></th>
<th align="left"><strong>Typical RCS (m²)</strong></th>
<th align="left"><strong>Approx. NRCS (dB m²/m²)</strong></th>
<th align="left"><strong>Visibility with NESZ -4 dB</strong></th>
<th align="left"><strong>Visibility with NESZ -18 dB</strong></th>
<th align="left"><strong>Remarks</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Large cargo ship</td>
<td align="left">10,000 to 100,000</td>
<td align="left">20 to 30 dB</td>
<td align="left">Very visible</td>
<td align="left">Extremely visible</td>
<td align="left">Very strong double-bounce and metallic reflections; among the brightest man-made targets.</td>
</tr>
<tr>
<td align="left">Passenger car</td>
<td align="left">1 to 10</td>
<td align="left">0 to +10 dB</td>
<td align="left">Visible</td>
<td align="left">Very visible</td>
<td align="left">Strong reflections from metal surfaces and ground interaction.</td>
</tr>
<tr>
<td align="left">Pine tree</td>
<td align="left">0.1 to 1</td>
<td align="left">-10 to 0 dB</td>
<td align="left">May be discernible</td>
<td align="left">Somewhat bright</td>
<td align="left">Volume scattering from branches and needles, variable with polarization and wavelength.</td>
</tr>
<tr>
<td align="left">Stealth fighter</td>
<td align="left">0.001 to 0.1</td>
<td align="left">-30 to -10 dB</td>
<td align="left">Invisible</td>
<td align="left">May be discernible in favorable conditions</td>
<td align="left">Radar-absorbing materials and shaping suppress backscatter by 40–60 dB.</td>
</tr>
<tr>
<td align="left">Pigeon</td>
<td align="left">0.001 to 0.01</td>
<td align="left">-30 to -20 dB</td>
<td align="left">Invisible</td>
<td align="left">Practically invisible</td>
<td align="left">Minimal reflections difficult to reliably detect amid the noise.</td>
</tr>
<tr>
<td align="left">Calm pond (specular)</td>
<td align="left">&lt; 0.001</td>
<td align="left">&lt; -30 dB</td>
<td align="left">Invisible (black)</td>
<td align="left">Invisible (black)</td>
<td align="left">Mirror-like reflection directs energy away from the radar, producing dark image areas.</td>
</tr>
</tbody>
</table>
</figure>

It is important to understand that NESZ does not determine the practical visibility and clarity of targets, and it captures only one measure of image quality. The fundamental trade-off between resolution (via higher bandwidth) and noise was already mentioned, and there are many other factors and trade-offs that must be considered to accurately assess the quality, performance or interpretability of a SAR image, such as those discussed in the following section.

## 7.5) Radiometric Resolution, Quantization and Dynamic Range

In chapter [<span class="underline">6</span>](06_spatial_resolution_and_geospatial_accuracy.md), we explained the concept and genesis of azimuth, range, ground range and spatial resolution. There is an additional, separate form of resolution - radiometric resolution- which we will discuss before continuing on our path to understand SAR image quality.

<span class="underline">Radiometric resolution</span> measures the system's ability to distinguish and record differences in backscatter intensity from different image resolution cells. Each pixel is assigned a greyscale value representing backscatter intensity—pure black for no return, pure white for maximum return. Higher radiometric resolution provides more shades of gray to distinguish energy levels between these extremes, enabling better representation of NRCS differences (the radar reflectivity measure from Section [<span class="underline">7.4</span>](07_separating_signals_from_noise.md#74-noise-equivalent-sigma-zero-and-the-radar-cross-section)) across scatterers in a scene.

As all SAR data is stored digitally, it is important to also understand quantization and dynamic range. Trade-offs between these two factors must be considered when converting analogue radiometric backscatter intensities into digital values suitable for processing.

<span class="underline">Quantization</span> is the process of mapping values from a continuous range into a limited set of discrete levels. Computers use <span class="underline">data types</span> with specific bit lengths that constrain available levels, causing rounding and clipping of true measurements. This introduces <span class="underline">quantization noise</span>—the error from digitization—which decreases as more bits provide finer granularity. Insufficient bit depth also causes <span class="underline">quantization loss</span>: the permanent loss of subtle signal variations. <span class="underline">Dynamic range</span> refers to the ratio between the largest and smallest measurable values, typically expressed as a base-10 logarithmic decibel (dB) value.

SAR pixels are said to be “complex” because each pixel contains both an amplitude data component and a phase data component, which represent the average intensity and phase of the backscatter from that pixel, respectively (see Section [<span class="underline">8.1</span>](08_sar_imagery_and_interpretation_considerations.md#81-complex-and-amplitude-images) for more). These terms—quantization and dynamic range—typically refer to limits in the digital storage representation of these complex pixels.

Amplitude values are typically quantized as <span class="underline">8- or 16-bit unsigned integers</span>, referred to as <span class="underline">u8</span> and <span class="underline">u16</span>, providing 256 or 65536 distinct levels, or shades of gray, respectively. This corresponds to approximate dynamic ranges of 25 dB and 50 dB — sufficient for many applications but below the full dynamic range of SAR echoes, which can span over 100 dB.

To capture this wider range, many SAR systems use the <span class="underline">float</span> data type, which is a <span class="underline">32-bit floating-point representation</span> that encodes both a *significand* and an *exponent* with the latter dedicated to enabling a much larger dynamic range – in excess of 150 dB – and with the former providing nonetheless high precision. The float data type is used to handle raw data and image formation to minimize both quantization noise and loss while maintaining phase fidelity.

At later processing stages, however, floats are often converted to integer formats to reduce storage size and accelerate downstream processing. This conversion inevitably compresses or clips values outside the reduced dynamic range, but the trade-off is often acceptable: u16 images still provide sufficient contrast for most operational and scientific uses while requiring only half the memory. Nonetheless, sticking to the float data type remains essential when fine discrimination is needed—metallic infrastructure amid vegetation, subtle ocean patterns—and in phase-sensitive applications like interferometric SAR (see Section [<span class="underline">9.7</span>](09_data_processing_and_analysis.md#97-phase-based-interferometric-techniques)), where floating-point precision prevents data degradation and preserves radiometric integrity.

High dynamic range and radiometric resolution are important in SAR, as backscatter intensities vary greatly especially during the imaging and image generation process. The echoes are weaker at beam edges, farther ranges, high incidence angles, and surfaces that reflect energy away or poorly overall (see Section [<span class="underline">8.2</span>](08_sar_imagery_and_interpretation_considerations.md#82-backscatter-polarization-and-scattering-mechanisms)). The intensity variation can span even 100 dB, as noted earlier, but simultaneously the detection of subtle intensity differences can also be valuable, which challenges both the sensitivity and the dynamic range capacity of a SAR system. Moreover, the spatial distribution of sidelobes described by the PSLR and ISLR metrics, introduced in Section [<span class="underline">6.4</span>](06_spatial_resolution_and_geospatial_accuracy.md#64-_penquw79sxco), also influences radiometric fidelity by introducing low-level energy into adjacent pixels, effectively reducing the achievable contrast between weak and strong scatterers.

It must be noted that there is a close link between the system’s noise performance — characterized by the NESZ metric introduced in Section [<span class="underline">7.4</span>](07_separating_signals_from_noise.md#74-noise-equivalent-sigma-zero-and-the-radar-cross-section) — and its radiometric resolution. A high (poor) NESZ raises the noise floor, suppressing faint scatterers below detectability and reducing the effective radiometric dynamic range across the scene. The upper part of the range remains available for strong reflectors, but radiometric subtlety in darker regions is lost.

This brings us to <span class="underline">radiometric calibration</span>, which refers to the process of converting the raw pixel values of a SAR image into physically meaningful measures of backscatter, such as sigma nought (σ⁰), by compensating for sensor geometry, antenna pattern, and range-dependent attenuation. While radiometric resolution determines the available precision, radiometric calibration ensures the accuracy across pixels in the scene.

In calibrated SAR images, black pixels correspond to areas at or below the NESZ threshold—where backscatter is indistinguishable from noise. Greyscale values then map logarithmically (according to system radiometric resolution and dynamic range) to calibrated NRCS values up to the brightest reflectors, which appear pure white. Consequently, as noted in Table [<span class="underline">7.1</span>](#table-7.1-detectability-of-different-targets-in-sar), calm water surfaces with near-specular reflections appear completely black (returns below the noise floor), while large cargo ships with metallic surfaces at varying angles often produce pure white pixels.

!!! note inline end

    In this chapter, titled “Separating Signals from Noise”, we have now dissected the Radar Range Equation and its Signal-to-Noise Ratio form. We have emphasized the relentless impact of range and how it makes the many sources of noise a challenge. However, we have also explained the innovations with which radar engineers have greatly tackled that challenge to improve signal clarity. And then, we have discussed NESZ (backscatter signal sensitivity) and NRCS (scatterer reflectivity), and now radiometric resolution and related digital implementation considerations, all of which allow us to better understand how target signals can be separated from all the noise. Next, in Chapter [<span class="underline">8</span>](08_sar_imagery_and_interpretation_considerations.md), we continue to dive deeper into image quality and interpretation.
