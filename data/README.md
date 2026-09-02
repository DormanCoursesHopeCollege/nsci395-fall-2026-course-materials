# Course data

The small tables in this folder support instruction and local notebook checks.
They are not interchangeable with empirical observations. Each notebook must
state whether the table it uses is recorded, simulated from a specified model,
or constructed for teaching.

## `membrane_signal.csv`

- **Status:** illustrative synthetic teaching construction; not recorded data
  and not output from a validated biophysical model.
- **Purpose:** gives P00 a recognizable action-potential-shaped example while
  students learn JupyterLab cells, Markdown, output, and kernel state.
- **Columns:** `time_ms` (0.5 ms samples), `current_nA` (brief 0.6 nA teaching
  pulse), and `voltage_mV` (piecewise-linear action-potential-shaped voltage).
- **Generator:** `../scripts/generate_synthetic_data.py`.
- **Expected landmarks:** 100 rows; resting value -70 mV; maximum +35 mV;
  minimum -78 mV; injected current begins at 5 ms.
- **Limit:** the timing and waveform were chosen for legibility. They must not
  be used to infer real-neuron kinetics, channel mechanisms, or population
  variability.

Regenerate the table from the course repository root with:

```bash
python course_repo/scripts/generate_synthetic_data.py
```

## `synthetic_fi_observations.csv`

- **Status:** illustrative synthetic repeated observations; not recorded data.
- **Purpose:** supports comparison of a deterministic LIF f-I curve with a
  small variable table whose known construction is inspectable.
- **Columns:** `input_current_nA` and `synthetic_rate_hz`; five current levels
  have 12 constructed observations each.
- **Generator:** `../scripts/generate_synthetic_data.py`, using the fixed seed
  395. The teaching mean is zero below 0.10 nA and increases by 250 Hz/nA above
  it; Gaussian teaching noise with 5 Hz standard deviation is added and
  negative values are clipped to zero.
- **Limit:** the rule and noise were chosen for pedagogy and were not estimated
  from a preparation. The table cannot support empirical claims about neuronal
  variability, an actual f-I relationship, or goodness of fit to a recording.

The identical project-starter copy is generated at
`project/starters/data/synthetic_fi_observations.csv` so the starter remains
self-contained.

## Other generated teaching tables

The following files are also produced by
`../scripts/generate_synthetic_data.py`. They are constructed examples, not
measurements. Fixed seeds make every row reproducible.

### `first_spike_counts.csv`

A 12-row fixed example for early table reading. Each row is one synthetic trial
with an integer spike count in a 500 ms window; `firing_rate_hz` is exactly the
count divided by 0.5 s. The `quiet` and `loud` labels are teaching categories,
not experimental conditions from a study.

### `auditory_trials.csv`

A 120-row synthetic frequency-tuning table: 24 constructed trials at each of
500, 1000, 2000, 4000, and 8000 Hz. Counts are drawn from clipped rounded
Gaussian teaching distributions with a peak mean at 2000 Hz; rates are counts
divided by a 0.5 s window. `choice` is a fixed illustrative low/high category.
The table can support grouping, variation, and figure practice, but not claims
about auditory physiology, tuning in a recorded neuron, or behavioral choice.

### `two_neuron_geometry.csv`

Two 60-row synthetic response clouds with correlated variation. The columns
`neuron_1_hz` and `neuron_2_hz` are constructed rates used to make population
geometry visible. Cluster separation and covariance were chosen for teaching;
they are not estimates from recorded neurons.

### `population_trials.csv`

One hundred eighty synthetic trials with a unitless `stimulus_value`, a noisy
constructed binary `choice`, and 12 unit-bearing synthetic rate columns
(`neuron_01_hz` through `neuron_12_hz`). The generator gives the rates one
shared stimulus-related dimension plus shared and independent noise. This lets
students study shape, PCA, and leakage with a known construction. It does not
represent a brain area, participant, animal, or measured population.

### `spike_times.csv`

Synthetic sparse event times for 20 `silence` and 20 `tone` trials. Events are
drawn in a -0.3 to 0.4 s interval from an explicit teaching process with equal
prestimulus rates and a larger post-zero rate for `tone`. It may be used to
practice rasters and histograms, not as recorded auditory evidence.

## Public recorded data

The `open/` subfolder is different: `open/ten_intensities.csv` is an adapted
public recorded spike-event table. Its separate `SOURCE_AND_LICENSE.md` and MIT
license state the source, design, row meaning, and redistribution terms. Do not
describe generated tables above as recorded, and do not describe the public
event file as synthetic.
