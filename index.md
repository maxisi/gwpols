{% include lib/mathjax.html %}

# Gravitational-wave polarizations

Like electromagnetic waves, gravitational waves (GWs) come in two distinct polarization states. These can be parametrized in a number of ways---we illustrate a few examples below.

## The linear basis

GW polarizations are usually represented in the **linear polarization basis** of plus ($$+$$) and cross ($$\times$$) states, which are typically illustrated by their instantaneous effect on a freely-falling ring of particles, as shown below.

<figure>
<img src="./assets/images/pol_ring_plus.png" alt="Plus polarization" width="200"/>
<img src="./assets/images/pol_ring_cross.png" alt="Cross polarization" width="200"/>
<figcaption>Gravitational-wave polarizations: plus (left) and cross (right).</figcaption>
</figure>

In these diagrams, the GW propagates in the _z_ direction, in or out of the screen, deforming the original ring (dotted circle) into ellipsoidal patterns shown at half-period intervals (solid and dashed).

Any GW can be expressed as a superposition of these two polarization states, and can be specified through time-dependent strain functions $$h_+$$ and $$h_\times$$. These functions determine the signal observed at any given detector; for any specific source, they are prescribed by Einstein's equations and relevant initial conditions.

We can visualize how any GW can be decomposed into $$+$$ and $$\times$$ contributions by explicitly splitting the two polarizations and illustrating their physical effects separately, as in the first figrue above.
More abstractly, we can also represent the GW polarization state at any instant through a vector in a Cartesian space defined by the $$\left(h_+, h_\times\right)$$ amplitudes: the magnitude of this _phasor_ encodes the overall strength of the signal, and its orientation the ratio between $$+$$ and $$\times$$.

If the wave is monochromatic (i.e., it has a definite frequency $$\omega$$), we can further represent the individual phases of each polarization component through so-called _linear quadratures_, $$x_{+/\times}(t) \equiv A_{+/\times} \cos \phi_{+/\times} \cos \omega t$$ and $$y_{+/\times}(t) \equiv A_{+/\times} \sin \phi_{+/\times} \sin \omega t$$ (these are just a convenient way of representing an arbitrary sinusoid).
The figure below shows an example of all these representations for the simple case of a fully $$+$$-polarized wave.

<figure>
<img src="./assets/images/pol_lin_p.gif" alt="Plus polarization"/>
<figcaption>Monochromatic <i>plus</i> polarized wave as a function of time.</figcaption>
</figure>

_Left:_ overall effect on a freely-falling ring of particles. _Center left:_ decomposition of the effect into $$+$$ (top) and $$\times$$ states; in this case, there is no $$\times$$ contribution. _Center right:_ polarization state represented in the $$h_+$$ vs $$h_\times$$ phasor space, where the arrow represents the amplitude of plus vs cross waves at any given instant. _Left_: decomposition into the cosine and sine quadratures for $$+$$ (top) and $$\times$$ (bottom). 

<figure>
<img src="./assets/images/pol_lin_c.gif" alt="Cross polarization"/>
<figcaption>Monochromatic <i>cross</i> polarized wave as a function of time.</figcaption>
</figure>

This last animation is analogous to the previous one, except for a fully $$\times$$-polarized GW (i.e., $$h_+ = 0$$ at all times).

## The circular basis

For monochromatic GWs, just as in the case of electromagnetic waves, we can also define a **circular polarization basis**, composed of right and left handed modes.
These are defined such that they result in a polarization phasor that rotates around a circle in the $$\left(h_+, h_\times\right)$$ plane: if the rotation is _counterclockwise_ (_clockwise_), we say the state is _right_-handed (_left_-handed).

In terms of the linear polarization amplitudes, the corresponding right (R) and left (L) handed polarization amplitudes, $$h_{R/L}$$, are given by

$$
h_{R/L} = \frac{1}{\sqrt{2}} \left( h_+ \mp i h_\times \right)
$$

with the minus (plus) sign for R (L).
Like we did for the linear polarizations above, the effect of a circular R-polarized GW is illustrated in the animation below.

<figure>
<img src="./assets/images/pol_circ_r.gif" alt="Right-handed circular polarization"/>
<figcaption>Monochromatic <i>right-handed</i> wave as a function of time.</figcaption>
</figure>

We see that contributions from both $$+$$ and $$\times$$ components are required to produced a circularly polarized state, and the two linear components must be exactly $$\pi/2$$ radians in phase apart in order to add up to a circle.

Just as the circular polarization states define a circle in the $$\left(h_+, h_\times\right)$$ plane, they also cause test particles to oscillate in a circle around their equilibrium positions (see small circle shown on the left-most panel of the above figure).

A left-handed wave looks the same as above, but with the sense of rotation reversed.

<figure>
<img src="./assets/images/pol_circ_l.gif" alt="Left-handed circular polarization"/>
<figcaption>Monochromatic <i>left-handed</i> wave as a function of time.</figcaption>
</figure>

Any monochromatic GW can be decomposed into right and left handed modes.

## The elliptical basis

Most generally, any fully-polarized GW can be written as a superposition of circularly-polarized modes, which add up to an elliptically polarized state.

<figure>
<img src="./assets/images/pol_ellip.gif" alt="Elliptical polarization"/>
<figcaption>Monochromatic <i>elliptical</i> (i.e., fully polarized) wave as a function of time.</figcaption>
</figure>

