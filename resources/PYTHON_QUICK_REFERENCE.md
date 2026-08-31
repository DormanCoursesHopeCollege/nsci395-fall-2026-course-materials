# Python quick reference for neural data and models

## Names and calculations

```python
spike_count = 12
window_s = 0.5
rate_hz = spike_count / window_s
```

Use names that preserve the scientific meaning and unit.

## Functions

```python
def firing_rate_hz(spike_count, window_s):
    return spike_count / window_s
```

Test a small known answer:

```python
assert firing_rate_hz(10, 0.5) == 20
```

## Conditions

```python
if voltage_mV >= threshold_mV:
    label = 'spike'
else:
    label = 'no spike'
```

Pay attention to boundaries: `>` and `>=` are not the same.

## Lists and loops

```python
counts = [4, 7, 5]
rates = []
for count in counts:
    rates.append(count / 0.5)
```

Trace the loop for one element before running it.

## Building a list in one line

A list comprehension is the loop above, written on one line.

```python
rates = [count / 0.5 for count in counts]
strong = [count for count in counts if count >= 6]
```

## Dictionaries

A list finds a value by position; a dictionary finds it by name.

```python
condition = {'label': 'baseline', 'current_nA': 0.18, 'spike_count': 12}
condition['spike_count'] = 13
print(condition['current_nA'])
```

A list of dictionaries becomes a table with one row per dictionary, which is how
we build results tables in M04 and I01:

```python
rows = []
for current_nA in [0.10, 0.18, 0.30]:
    rows.append({'current_nA': current_nA, 'spike_count': run_model(current_nA)})
results = pd.DataFrame(rows)
```

## NumPy arrays

```python
import numpy as np

voltage_mV = np.array([-70, -66, -61, -58])
above_threshold = voltage_mV >= -60
selected = voltage_mV[above_threshold]
```

Useful checks:

```python
type(voltage_mV)
voltage_mV.shape
voltage_mV[:5]
above_threshold.sum()
```

## Time masks

```python
response = (time_ms >= 100) & (time_ms < 300)
response_values = voltage_mV[response]
```

Parentheses around each comparison are required with `&`.

## pandas tables

```python
import pandas as pd

trials = pd.read_csv('auditory_trials.csv')
trials.head()
trials.shape
trials.columns
trials.groupby('stimulus')['spike_count'].mean()
```

One row should represent one observation whose meaning you can state.

### Reshaping events into a trial table

Real spike files have one row per event. Analysis usually needs one row per
trial, including trials where nothing happened.

```python
trial_index = pd.MultiIndex.from_product(
    [range(10), range(10)], names=['Intensity', 'Trial']
)

# Count events per trial, then put back the trials that had no events.
counts = (
    spikes.groupby(['Intensity', 'Trial'])
    .size()
    .reindex(trial_index, fill_value=0)
    .rename('total_spikes')
    .reset_index()
)
```

`pd.cut` labels each value with the bin it falls in, and `pivot_table` turns
those labels into one column per bin. `right=False` makes each bin include its
left edge and exclude its right edge.

```python
spikes['window'] = pd.cut(
    spikes['SpikeTime'],
    bins=[0, 4, 14, 21],
    right=False,
    labels=['prestimulus', 'response', 'late'],
)

features = spikes.pivot_table(
    index=['Intensity', 'Trial'],
    columns='window',
    values='SpikeTime',
    aggfunc='size',
    fill_value=0,
    observed=False,
).reindex(trial_index, fill_value=0).reset_index()
```

Check the row count after every reshape. If it is not the number of trials the
experiment ran, something was dropped or duplicated.

## Matplotlib

This is the form the course notebooks use.

```python
import matplotlib.pyplot as plt

plt.plot(time_ms, voltage_mV)
plt.xlabel('Time (ms)')
plt.ylabel('Voltage (mV)')
plt.show()
```

You will meet a second form in other books, including *Neural Data Science in
Python*. It does the same thing and is worth recognising, because it names the
axes object explicitly and is the easier form when a figure has several panels.

```python
fig, ax = plt.subplots()
ax.plot(time_ms, voltage_mV)
ax.set(xlabel='Time (ms)', ylabel='Voltage (mV)')
plt.show()
```

`course_utils.clean_axes()` removes the top and right box lines from the current
figure. Call it after plotting, with no argument.

## Restart and run all

Before submission:

1. save;
2. restart the kernel;
3. run all cells from top to bottom;
4. inspect errors, warnings, figures, and final claims;
5. commit and push the checked version.
