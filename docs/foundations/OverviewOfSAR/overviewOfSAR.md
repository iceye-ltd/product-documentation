# An Overview of SAR Imaging

!!! Note
    This overview is excerpted with permission from [The Essentials of SAR](https://www.amazon.com/dp/B09CGKTLZV/ref=cm_sw_em_r_mt_dp_H9NDBJSVREXRK5PA4Z58), by Thomas P. Ager[@ageressentials]This comprehensive text was written for SAR users, not electrical engineers. It reviews the many interesting aspects of SAR and its uses that we cannot cover in this short overview.

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
| BAND | WAVELENGTH [CM] | FREQUENCY [GHZ] | ORIGIN |
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

## References
\bibliography
