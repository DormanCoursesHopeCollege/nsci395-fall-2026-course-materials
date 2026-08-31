# Optional readings for NSCI 395

The course notebooks are the required learning sequence. Nothing on this page is
required unless the instructor says so in class or on Moodle. Use it when you
want a second explanation, more practice, or a fuller treatment than a 50-minute
notebook can give.

Each entry names what the source adds that the notebook does not. Reading a
source that says the same thing in the same way is rarely worth your time; these
were chosen because they differ usefully.

## The four sources

| Short name | Full reference | Level | Licence |
| --- | --- | --- | --- |
| **NDS** | Newman, A. J. *Neural Data Science in Python*. <https://neuraldatascience.io/> | Beginner to intermediate; Python-first | CC BY-NC-SA 4.0 |
| **Bates** | Greene, M. and Bates NS/PY 357 students. *Computational Neuroscience Textbook*. <https://mrgreene09.github.io/computational-neuroscience-textbook/> | Undergraduate; written by undergraduates | CC BY-NC-SA 4.0 |
| **Gerstner** | Gerstner, W., Kistler, W. M., Naud, R., and Paninski, L. (2014). *Neuronal Dynamics*. Cambridge University Press. <https://neuronaldynamics.epfl.ch/online/index.html> | Advanced; graduate reference | © Cambridge University Press. Free to read online. **Do not copy figures or text.** |
| **Think Python** | Downey, A. B. *Think Python*, 3rd edition. <https://allendowney.github.io/ThinkPython/> | Beginner; general programming | CC BY-NC-SA 4.0 |

Gerstner is the deep end. It is included because a few sections are genuinely
readable at our level, and because it is the standard reference if you continue
in this field. Where it is listed below, read the named section only, skip the
mathematics that has not been introduced in class, and treat the figures as
things to look at rather than reproduce.

## Notation crosswalk

Sources write the same model differently. This is the single most common source
of confusion when reading beyond the notebooks.

| Idea | This course | Bates | Gerstner |
| --- | --- | --- | --- |
| Passive membrane | `dV/dt = (-(V - E_leak)/R + I) / C` | `C_m dV_m/dt = I_e - g_L(V_m - E_L)` | `τ_m dV/dt = -(V - u_rest) + R I(t)` |
| Leak term | resistance `R` (MΩ) | conductance `g_L` | resistance `R` |
| Time constant | `τ = R · C` | `τ_m = R_m C_m` | `τ_m` |
| Resting/leak potential | `E_leak` | `E_L` | `u_rest` |
| Membrane voltage | `voltage_mV`, `V` | `V_m` | `u` |

All three are the same model. Conductance is the reciprocal of resistance,
`g_L = 1 / R`, so a large leak conductance and a small membrane resistance mean
the same thing: a leaky cell. Our variable names carry units (`voltage_mV`,
`resistance_MOhm`) because unit confusion is the most common wrong-answer bug in
this course.

Gerstner's form is our form divided through by `C` and rearranged. Multiply our
equation by `R·C` and it becomes his.

## Unit 1: Python foundations (P00-P09, weeks 1-4)

| Notebook | Read for a second explanation | Why |
| --- | --- | --- |
| P00-P01 | NDS, [Introducing Python](https://neuraldatascience.io/python/introduction) and [Data types](https://neuraldatascience.io/python/data-types) | Same Jupyter-first framing as our notebooks, more worked examples |
| P03-P04 | Think Python, "Functions" and "Testing" chapters | Downey is the best short treatment of why functions and tests exist |
| P05 | NDS, [Conditionals](https://neuraldatascience.io/python/conditionals) | Extra practice on boundary cases |
| P06 | NDS, [Lists](https://neuraldatascience.io/python/lists) and [Dictionaries](https://neuraldatascience.io/python/dictionaries) | Our dictionary section is deliberately short; this is the fuller version |
| P07 | NDS, [For loops](https://neuraldatascience.io/python/for-loops) | More loop-tracing practice |
| P08-P09 | NDS, [Visualizing data](https://neuraldatascience.io/viz/introduction) and [Plotting](https://neuraldatascience.io/viz/plotting) | Figure construction in more depth than we have class time for |
| Any week | Bates, [Ch. 2 Introduction to Python](https://mrgreene09.github.io/computational-neuroscience-textbook/Ch1.html) | A neuroscience-flavoured Python primer written by undergraduates |

**Note on style.** NDS teaches Matplotlib with `fig, ax = plt.subplots()`. Our
notebooks use the shorter `plt.plot(...)` form. Both are correct and produce the
same figures; see `PYTHON_QUICK_REFERENCE.md`, which shows the two side by side.

## Unit 2: Modelling single neurons (M01-M06, weeks 5-7)

| Notebook | Read | Why |
| --- | --- | --- |
| M01 | Bates, [Ch. 3 What is Computational Neuroscience?](https://mrgreene09.github.io/computational-neuroscience-textbook/Ch2.html) | Sets up the "what does a model keep" question at our level |
| M02-M03 | Bates, [Ch. 4 Passive Membrane Models](https://mrgreene09.github.io/computational-neuroscience-textbook/Ch3.html) | Derives the Nernst and GHK background we skip, and gives the exact solution we test against in M04 |
| M03 | Gerstner, [1.2 Elements of Neuronal Dynamics](https://neuronaldynamics.epfl.ch/online/Ch1.S2.html) | The same equation with a physicist's framing |
| M05 | Gerstner, [1.3 Integrate-And-Fire Models](https://neuronaldynamics.epfl.ch/online/Ch1.S3.html) | The canonical statement of threshold-and-reset |
| M05 | Gerstner, [1.4 Limitations of the Leaky Integrate-and-Fire Model](https://neuronaldynamics.epfl.ch/online/Ch1.S4.html) | **Recommended.** Short, non-mathematical, and directly answers "what is this model not telling me?" |
| M06 | Bates, [Ch. 6 Firing Rates](https://mrgreene09.github.io/computational-neuroscience-textbook/Ch5.html) | Rate definitions and their tradeoffs |
| M06 | Gerstner, [7.2 Mean Firing Rate](https://neuronaldynamics.epfl.ch/online/Ch7.S2.html) | Three different things the phrase "firing rate" can mean |
| M06 | Gerstner, [7.3 Interval distribution and coefficient of variation](https://neuronaldynamics.epfl.ch/online/Ch7.S3.html) | Why a mean rate hides the variability our model does not have |

## Unit 3: Real spike data (D00-D05, P11, weeks 8-10)

| Notebook | Read | Why |
| --- | --- | --- |
| D00-D01 | NDS, [Effects of light intensity on spike rate](https://neuraldatascience.io/single-unit/ten-intensities) | **This is our dataset.** Newman works through the same ten-intensity file with rasters and PSTHs |
| D00 | NDS, [Single unit data](https://neuraldatascience.io/single-unit/introduction) and [learning objectives](https://neuraldatascience.io/single-unit/learning-objectives) | Frames what single-unit recording is and is not |
| P11 | NDS, [Exploratory data analysis](https://neuraldatascience.io/eda/introduction) | More pandas reshaping practice |
| D02 | Gerstner, [7.1 Spike train variability](https://neuronaldynamics.epfl.ch/online/Ch7.S1.html) | Where trial-to-trial variability comes from |
| D03 | Bates, [Ch. 8 Decoding](https://mrgreene09.github.io/computational-neuroscience-textbook/Ch7.html) | The encoding/decoding distinction at our level |
| D04-D05 | NDS, [Machine learning](https://neuraldatascience.io/machine-learning/introduction) | Train/test logic and evaluation, in the same scikit-learn idiom we use |
| D05 | Gerstner, [Ch. 11 Encoding and Decoding with Stochastic Neuron Models](https://neuronaldynamics.epfl.ch/online/Ch11.html) | Skim only. Shows how far this idea is taken in research |

**Read this one before G04 and I02.** The NDS ten-intensities page contains
complete worked code for rasters and PSTHs on our dataset. That makes it a good
second explanation and a poor place to copy from: your submitted analysis uses
different windows and a different question, and you must be able to explain
every line you submit. Cite it in your assistance disclosure if you used it.

## Unit 4: Circuits and populations (C01-C03, POP01-POP02, weeks 11-12)

| Notebook | Read | Why |
| --- | --- | --- |
| C01 | Gerstner, [Ch. 3 Dendrites and Synapses](https://neuronaldynamics.epfl.ch/online/Ch3.html) | Sections 3.1-3.2 only, for what a synaptic input physically is |
| C02 | Gerstner, [Ch. 15 Fast Transients and Rate Models](https://neuronaldynamics.epfl.ch/online/Ch15.html) | The rate-model framing our E-I simulation uses |
| C02-C03 | Bates, [Ch. 9 Neural Networks](https://mrgreene09.github.io/computational-neuroscience-textbook/Ch8.html) | A gentler on-ramp to network behaviour |
| C03 | Gerstner, [Ch. 17 Memory and Attractor Dynamics](https://neuronaldynamics.epfl.ch/online/Ch17.html) | Skim 17.1 for what "persistent activity" means |
| POP01-POP02 | Gerstner, [Ch. 12 Neuronal Populations](https://neuronaldynamics.epfl.ch/online/Ch12.html) | Read 12.1 for what a population variable is |

## Unit 5: Model choice and claims (S01-S02, week 13-14)

| Notebook | Read | Why |
| --- | --- | --- |
| S01 | Bates, [Ch. 5 Hodgkin and Huxley Model](https://mrgreene09.github.io/computational-neuroscience-textbook/Ch4.html) | Our level, with the gating variables explained |
| S01 | Gerstner, [2.2 Hodgkin-Huxley Model](https://neuronaldynamics.epfl.ch/online/Ch2.S2.html) | The reference statement of the model, including the rate functions our demonstration uses |
| S01 | Gerstner, [2.3 The Zoo of Ion Channels](https://neuronaldynamics.epfl.ch/online/Ch2.S3.html) | Why "add more detail" has no natural stopping point |
| S02 | NDS, "AI-Assisted Coding" chapter (find it in the sidebar at <https://neuraldatascience.io/>) | Newman's take on disclosure and verification, which is close to ours |

## Project support

| Project option | Read |
| --- | --- |
| PM1, PM2 (LIF) | Gerstner [1.3](https://neuronaldynamics.epfl.ch/online/Ch1.S3.html), [1.4](https://neuronaldynamics.epfl.ch/online/Ch1.S4.html); Bates [Ch. 6](https://mrgreene09.github.io/computational-neuroscience-textbook/Ch5.html) |
| PM3 (E-I circuit) | Gerstner [Ch. 15](https://neuronaldynamics.epfl.ch/online/Ch15.html) |
| PM4 (competing accumulators) | Gerstner [Ch. 16 Competing Populations and Decision Making](https://neuronaldynamics.epfl.ch/online/Ch16.html) |
| PD1 (optogenetic reliability) | NDS [ten intensities](https://neuraldatascience.io/single-unit/ten-intensities) |
| PD2, PD3, PD4 (macaque V4) | NDS [multielectrode data](https://neuraldatascience.io/single-unit/intro-multielec-data); Snyder et al. (2015), *Nature Neuroscience* 18, 736-743, <https://doi.org/10.1038/nn.3979> |

## What each source will not give you

- **NDS** is the closest match to our Python and data work, and has almost no
  simulation. It will not help with M01-M06 or C01-C03.
- **Bates** covers the modelling arc at the right level but assumes a slightly
  different Python style and uses conductance notation.
- **Gerstner** is authoritative and mostly above this course. Sections 1.3, 1.4,
  2.2, 2.3, 7.1, and 7.2 are the reliably readable ones.
- **Think Python** is about programming, not neuroscience. Use it when the
  obstacle is Python itself rather than the science.

## How to cite a source in your work

If a reading changed what you submitted, say so in the assistance disclosure:
the source, what you took from it, and what you checked yourself. Copying code
from any of these books into graded work without disclosure is the same problem
as copying it from anywhere else.
