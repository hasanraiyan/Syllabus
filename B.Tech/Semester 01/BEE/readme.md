# Basic Electrical Engineering

**Module 1: DC Circuits (8 Lectures)**
- [ ] Electrical Circuit Elements (R, L, and C)
- [ ] Voltage and Current Sources
- [ ] Kirchhoff Current and Voltage Laws
- [ ] Analysis of Simple Circuits with DC Excitation
- [ ] Star-Delta Conversion
- [ ] Network Theorems (Superposition, Thevenin, Norton, and Maximum Power Transfer Theorems)
- [ ] Time-Domain Analysis of First-Order RL and RC Circuits

**Module 2: AC Circuits (8 Lectures)**
- [ ] Representation of Sinusoidal Waveforms
- [ ] Peak, RMS, and Average Values (Form Factor and Peak Factor)
- [ ] Impedance of Series and Parallel Circuits
- [ ] Phasor Representation
- [ ] Real Power, Reactive Power, Apparent Power, Power Factor, Power Triangle
- [ ] Analysis of Single-Phase AC Circuits consisting of R, L, C, RL, RC, RLC Combinations (Series and Parallel), Resonance
- [ ] Three-Phase Balanced Circuits, Voltage and Current Relations in Star and Delta Connections

**Module 3: Magnetic Circuits (4 Lectures)**
- [ ] Series and Parallel Magnetic Circuits
- [ ] Analysis of Series and Parallel Magnetic Circuits

**Module 4: Transformers (6 Lectures)**
- [ ] Magnetic Materials
- [ ] BH Characteristics
- [ ] Ideal and Practical Transformer
- [ ] EMF Equation
- [ ] Equivalent Circuit
- [ ] Losses in Transformers, Regulation, and Efficiency
- [ ] Auto-Transformer and Three-Phase Transformer Connections

**Module 5: Electrical Machines (10 Lectures)**
- [ ] Construction, Working, Torque-Speed Characteristic, and Speed Control of Separately Excited DC Motor
- [ ] Generation of Rotating Magnetic Fields
- [ ] Construction and Working of a Three-Phase Induction Motor
- [ ] Significance of Torque-Slip Characteristic
- [ ] Loss Components and Efficiency, Starting and Speed Control of Induction Motor
- [ ] Construction and Working of Synchronous Generators

**Module 6: Electrical Installations (6 Lectures)**
- [ ] Components of LT Switchgear: Switch Fuse Unit (SFU), MCB, ELCB, MCCB, Types of Wires and Cables, Earthing
- [ ] Types of Batteries, Important Characteristics for Batteries
- [ ] Elementary Calculations for Energy Consumption, Power Factor Improvement, and Battery Backup

Great! Let's start with the first topic and work our way down the list.

### 1. Representation of Sinusoidal Waveforms
A sinusoidal waveform (or sine wave) is a mathematical curve that describes a smooth periodic oscillation. It's essential in AC circuits.

**Key Points:**
- **Mathematical Representation:**
  - Voltage: \( V(t) = V_m \sin(\omega t + \phi) \)
  - Current: \( I(t) = I_m \sin(\omega t + \phi) \)
  - Where:
    - \( V_m \) and \( I_m \) are the peak values (maximum amplitude).
    - \( \omega \) is the angular frequency (\( \omega = 2\pi f \), where \( f \) is the frequency).
    - \( \phi \) is the phase angle.
    - \( t \) is the time.

- **Graphical Representation:**
  - The waveform is plotted with time on the x-axis and amplitude (voltage or current) on the y-axis.
  - The sine wave oscillates between +V_m and -V_m (or +I_m and -I_m for current).

### 2. Peak, RMS, and Average Values (Form Factor and Peak Factor)

**Peak Value:**
- The maximum value (amplitude) of the waveform.
- For voltage: \( V_{peak} = V_m \)
- For current: \( I_{peak} = I_m \)

**RMS (Root Mean Square) Value:**
- Represents the equivalent DC value that delivers the same power to a load.
- For a sinusoidal voltage: \( V_{rms} = \frac{V_m}{\sqrt{2}} \)
- For a sinusoidal current: \( I_{rms} = \frac{I_m}{\sqrt{2}} \)

**Average Value:**
- The average value over one complete cycle of a sine wave is zero. However, the average of the absolute value (or the average over half a cycle) is:
  - \( V_{avg} = \frac{2V_m}{\pi} \)
  - \( I_{avg} = \frac{2I_m}{\pi} \)

**Form Factor:**
- Ratio of RMS value to the average value.
- \( \text{Form Factor} = \frac{V_{rms}}{V_{avg}} = \frac{\sqrt{2}}{2/\pi} \approx 1.11 \)

**Peak Factor:**
- Ratio of peak value to the RMS value.
- \( \text{Peak Factor} = \frac{V_{peak}}{V_{rms}} = \sqrt{2} \approx 1.414 \)

### 3. Impedance of Series and Parallel Circuits

**Impedance (Z):**
- The total opposition a circuit offers to the flow of alternating current.
- For a resistor (\( R \)): \( Z_R = R \)
- For an inductor (\( L \)): \( Z_L = j\omega L \)
- For a capacitor (\( C \)): \( Z_C = \frac{1}{j\omega C} \)
  - Where \( j \) is the imaginary unit (\( j^2 = -1 \)).

**Series Circuit:**
- Impedances add up.
- \( Z_{total} = Z_1 + Z_2 + \ldots + Z_n \)

**Parallel Circuit:**
- Reciprocals of impedances add up.
- \( \frac{1}{Z_{total}} = \frac{1}{Z_1} + \frac{1}{Z_2} + \ldots + \frac{1}{Z_n} \)

### 4. Phasor Representation

**Phasors:**
- A phasor is a complex number representing the magnitude and phase angle of a sinusoidal function.
- Voltage phasor: \( \tilde{V} = V_m e^{j\phi} \)
- Current phasor: \( \tilde{I} = I_m e^{j\phi} \)
- Phasors simplify AC circuit analysis by converting differential equations to algebraic equations.

**Phasor Diagrams:**
- Graphical representation of phasors, showing the phase relationships between different sinusoidal quantities.

### 5. Real Power, Reactive Power, Apparent Power, Power Factor, Power Triangle

**Real Power (P):**
- The actual power consumed by the circuit.
- \( P = V_{rms} I_{rms} \cos(\phi) \)
- Measured in watts (W).

**Reactive Power (Q):**
- Power stored and released by the reactive components (inductors and capacitors).
- \( Q = V_{rms} I_{rms} \sin(\phi) \)
- Measured in volt-amperes reactive (VAR).

**Apparent Power (S):**
- The product of the RMS values of voltage and current.
- \( S = V_{rms} I_{rms} \)
- Measured in volt-amperes (VA).

**Power Factor (PF):**
- The ratio of real power to apparent power.
- \( \text{PF} = \cos(\phi) \)

**Power Triangle:**
- A right triangle representing the relationship between P, Q, and S.
- Real Power (P) on the adjacent side, Reactive Power (Q) on the opposite side, and Apparent Power (S) as the hypotenuse.

### 6. Analysis of Single-Phase AC Circuits consisting of R, L, C, RL, RC, RLC Combinations (Series and Parallel), Resonance

**Series Circuits:**
- Calculate total impedance: \( Z = R + j\omega L + \frac{1}{j\omega C} \)
- Determine voltage and current using Ohm's law and phasor analysis.

**Parallel Circuits:**
- Calculate total admittance (reciprocal of impedance): \( Y = \frac{1}{R} + j\omega C + \frac{1}{j\omega L} \)
- Convert admittance back to impedance.

**Resonance:**
- Occurs when the inductive reactance (\( \omega L \)) equals the capacitive reactance (\( \frac{1}{\omega C} \)).
- Resonant frequency: \( \omega_0 = \frac{1}{\sqrt{LC}} \)
- At resonance, impedance is purely resistive, and the circuit behaves like a pure resistor.

### 7. Three-Phase Balanced Circuits, Voltage and Current Relations in Star and Delta Connections

**Three-Phase Systems:**
- Consist of three sinusoidal voltages or currents that are 120 degrees out of phase with each other.

**Star (Y) Connection:**
- Line voltage (\( V_L \)) is \(\sqrt{3}\) times the phase voltage (\( V_{ph} \)).
- Line current (\( I_L \)) equals phase current (\( I_{ph} \)).

**Delta (Δ) Connection:**
- Line voltage (\( V_L \)) equals phase voltage (\( V_{ph} \)).
- Line current (\( I_L \)) is \(\sqrt{3}\) times the phase current (\( I_{ph} \)).

**Voltage and Current Relations:**
- For Star: \( V_L = \sqrt{3} V_{ph} \), \( I_L = I_{ph} \)
- For Delta: \( V_L = V_{ph} \), \( I_L = \sqrt{3} I_{ph} \)

Would you like a deeper dive into any specific topic or more practice problems for these concepts?
