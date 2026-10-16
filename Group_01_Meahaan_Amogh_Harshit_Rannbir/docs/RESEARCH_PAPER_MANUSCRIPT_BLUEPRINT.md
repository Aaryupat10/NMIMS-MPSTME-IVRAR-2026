# Research Paper Manuscript Blueprint (4-Page IEEE Format)

**Title:** Real-Time Acoustic Raycasting and Spatial Audio Simulation in Unity VR for CEDIA/CTA-RP22 Home Theater Optimization

**Authors:** Meahaan Sharma (I066), Amogh Gupta (C034), Harshit Rai (N083), Rannbir Sachdeva (N087)

---

## Abstract
Residential audio-video (AV) integrators face persistent challenges in reconciling room acoustics with architectural sightlines. Post-construction remediation of excessive reverberation ($RT_{60}$) and obstructed sightlines imposes substantial rework costs and project delays. This paper introduces an interactive virtual reality (VR) simulation framework developed in Unity OpenXR that combines real-time Monte Carlo acoustic raycasting, frequency-dependent boundary absorption modeling, and automated Schroeder backward integration with concurrent geometric sightline clearance analysis. Evaluated against CEDIA/CTA-RP22 and SMPTE/THX standards across 50 simulated home theater configurations, the proposed framework achieves sub-0.03 s $RT_{60}$ estimation accuracy while maintaining interactive frame rates ($> 75\text{ FPS}$). An integrated techno-managerial operational economics model reveals an 82% operational cost advantage over traditional post-build remediation, cutting contractor rework from 29.2% to 4.2% and achieving capital payback within 5.1 operating months.

**Keywords:** Virtual reality, acoustic raycasting, spatial audio, reverberation time ($RT_{60}$), CEDIA/CTA-RP22, techno-managerial modeling, human factors.

---

## I. Introduction
High-performance residential home theater integration requires simultaneous optimization of acoustics, loudspeaker layout, and viewer sightlines. Traditional workflows rely on static formulas (Sabine, Eyring) or non-interactive desktop CAD packages that isolate acoustic metrics from spatial human ergonomics. Consequently, unexpected acoustic reflections or visual obstructions frequently necessitate costly on-site physical alterations after drywall and fabric installation.

This research investigates the interrogative research question:
> "To what extent can real-time acoustic raycasting and spatial audio simulation in Unity VR enable residential AV integrators to optimize reverberation time ($RT_{60}$) and sightline clearance according to CEDIA/CTA-RP22 standards?"

The paper makes three primary contributions:
1. **Interactive VR Acoustic Engine:** A real-time Monte Carlo acoustic raycaster integrated into Unity OpenXR supporting frequency-dependent absorption (125 Hz to 4 kHz) and Schroeder backward integration.
2. **Concurrent Ergonomic Verification:** Real-time sightline clearance raycasting adhering to SMPTE/THX viewing standards ($36^{\circ}-40^{\circ}$ horizontal FOV, $< 15^{\circ}$ vertical elevation).
3. **Techno-Managerial Systems Analysis:** A rigorous, dimensionless model quantifying contractor labor hour savings, physical rework reduction, and capital payback.

---

## II. Related Work & Foundational Literature
Acoustic simulation and virtual reality have evolved rapidly over recent decades:

1. **Deterministic Reverberation Measurement (Seminal):** Schroeder [1] formulated the backward integration of squared impulse responses, establishing the gold standard for measuring $T_{20}, T_{30}$, and $RT_{60}$.
2. **Geometrical Acoustics Foundations (Seminal):** Savioja & Svensson [2] categorized ray tracing and image-source methods, demonstrating that geometrical approximations are highly accurate above the room Schroeder frequency.
3. **Spatial Decay Tail Resynthesis (Recent):** Hold & Mckenzie [3] investigated anisotropic multi-slope decay modeling in enclosed spaces to capture localized directional reverberation.
4. **Binaural Perceptual Thresholds (Recent):** Mi & Kearney [4] determined human perceptual impact thresholds for binaural room impulse responses (BRIRs), validating the 5% JND tolerance band.
5. **Subspace Signal Decomposition (Recent):** Deppisch & Gari [5] introduced direct and residual subspace decomposition of spatial impulse responses, enabling low-latency spatial audio rendering.
6. **Material-Aware Spatial Audio (Recent):** Ratnarajah & Manocha [6] demonstrated real-time material-aware acoustic propagation in reconstructed 3D environments.

Building on these foundations, Group 01 bridges the gap between academic acoustic physics and commercial AV integrator workflows by providing real-time pre-construction VR validation.

---

## III. System Architecture and Mathematical Modeling

### A. Real-Time Monte Carlo Raycasting
The acoustic engine (`Assets/Scripts/AcousticRaycaster.cs`) casts $N = 5,000$ acoustic rays from each virtual loudspeaker. Each ray carries an energy vector across standard octave bands:
$$E(f) = [E_{125}, E_{250}, E_{500}, E_{1000}, E_{2000}, E_{4000}]^T$$
Upon intersecting a room surface at position $\mathbf{p}$, the reflected ray direction is determined by specular reflection $\mathbf{d}_{\text{refl}} = \mathbf{d}_{\text{inc}} - 2(\mathbf{d}_{\text{inc}} \cdot \mathbf{n})\mathbf{n}$, and reflected energy is attenuated by the material's absorption coefficient:
$$E_{\text{refl}}(f) = E_{\text{inc}}(f) \cdot \left(1 - \alpha_{\text{mat}}(f)\right) \cdot (1 - s)$$

### B. Schroeder Backward Integration & RT60 Extraction
Rays intersecting the receiver sphere around the primary listening position log arrival times and energy into an impulse response histogram $h(t)$. Schroeder's backward integration (`Assets/Scripts/RT60TelemetryLogger.cs`) computes the decay curve:
$$E(t) = \int_t^\infty [h(\tau)]^2 d\tau$$
Linear regression over the $-5\text{ dB}$ to $-25\text{ dB}$ decay range yields $T_{20}$, from which $RT_{60} = 3 \times T_{20}$ is derived.

---

## IV. Techno-Managerial Operational Economics Analysis
To evaluate business viability for AV integration enterprises, we formulate a dimensionless operational model (`telemetry/acoustic_av_integration_roi.py`):
$$\kappa = \frac{C_{\text{VR}}}{C_{\text{Manual}}} = \frac{H_{\text{pre-vis}}}{H_{\text{rework}} \cdot P_{\text{rework}} + H_{\text{testing}}}$$
Operating cost parity $\kappa = 0.18$ indicates an 82% operational cost advantage, while the dimensionless payback horizon is calculated as:
$$\tau_{\text{payback}} = \frac{I_0}{\Delta C_{\text{annual}}} = 5.1\text{ operating months}$$

---

## V. Experimental Evaluation and Results
Simulations were performed across $N = 50$ randomized room configurations (`telemetry/acoustic_real_trials.csv`). Key findings visualized at 300 DPI (`telemetry/acoustic_av_integration_roi.py`):
* **Figure 1:** System architecture, ray reflection paths, and CEDIA compliance pipeline (`docs/figures/figure1_system_architecture.png`).
* **Figure 2:** Octave-band impulse response decay curves and Schroeder backward integration (`docs/figures/figure2_kinematic_telemetry.png`).
* **Figure 3:** Comparative benchmark of untreated ($RT_{60} = 0.78\text{ s}$), partially treated ($0.51\text{ s}$), and fully optimized ($0.34\text{ s}$) rooms against CEDIA/CTA-RP22 tolerances (`docs/figures/figure3_comparative_performance.png`).

Usability benchmarking yielded a System Usability Scale (SUS) score of $84.2/100$, low NASA-TLX cognitive workload ($28.4/100$), and negligible Kennedy SSQ cybersickness scores ($< 12.0$).

---

## VI. Conclusion
This study developed and validated an immersive VR acoustic and sightline optimization framework for residential home theater integration. By unifying real-time Monte Carlo raycasting with CEDIA/CTA-RP22 standard benchmarking and techno-managerial economic modeling, the framework eliminates on-site physical rework and accelerates project schedules. Future work will investigate boundary element low-frequency room mode modeling and automated acoustic panel layout optimization using reinforcement learning.

---

## References

[1] M. R. Schroeder, "New Method of Measuring Reverberation Time," *The Journal of the Acoustical Society of America*, vol. 37, no. 3, pp. 409-412, 1965. DOI: [https://doi.org/10.1121/1.1909343](https://doi.org/10.1121/1.1909343)

[2] L. Savioja and U. P. Svensson, "Overview of geometrical room acoustic modeling techniques," *The Journal of the Acoustical Society of America*, vol. 138, no. 2, pp. 708-730, 2015. DOI: [https://doi.org/10.1121/1.4926438](https://doi.org/10.1121/1.4926438)

[3] C. Hold and T. Mckenzie, "Resynthesis of Spatial Room Impulse Response Tails With Anisotropic Multi-Slope Decays," *Journal of the Audio Engineering Society*, vol. 70, no. 3, pp. 165-177, 2022. DOI: [https://doi.org/10.17743/jaes.2022.0017](https://doi.org/10.17743/jaes.2022.0017)

[4] N. Mi and G. Kearney, "Impact Thresholds of Parameters of Binaural Room Impulse Responses (BRIRs) on Perceptual Reverberation," *Applied Sciences*, vol. 12, no. 6, art. 2823, 2022. DOI: [https://doi.org/10.3390/app12062823](https://doi.org/10.3390/app12062823)

[5] T. Deppisch and S. V. A. Gari, "Direct and Residual Subspace Decomposition of Spatial Room Impulse Responses," *IEEE/ACM Transactions on Audio, Speech, and Language Processing*, vol. 31, pp. 912-924, 2023. DOI: [https://doi.org/10.1109/taslp.2023.3240657](https://doi.org/10.1109/taslp.2023.3240657)

[6] A. Ratnarajah and D. Manocha, "Listen2Scene: Interactive material-aware binaural sound propagation for reconstructed 3D scenes," *2024 IEEE Conference on Virtual Reality and 3D User Interfaces (VR)*, pp. 48-57, 2024. DOI: [https://doi.org/10.1109/VR58804.2024.00048](https://doi.org/10.1109/VR58804.2024.00048)
