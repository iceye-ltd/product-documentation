# The Beautiful Equations
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