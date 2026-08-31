
# Open spike-data sources used in NSCI 395

The course uses two public teaching datasets. Students work from a course cache or the original repository. They do not need to search for a dataset during the project period.

## Optogenetic intensity spike events

**Course file:** `data/open/ten_intensities.csv`

**Original public repository:** https://github.com/neural-data-science/Single-Unit-Data

**Original file:** `data/ten_intensities.csv`

The table contains one row per recorded spike. The columns are stimulus intensity, trial number, and spike time in milliseconds. The teaching notebook describes ten intensity levels, ten trials per level, 20 ms trials, and optical stimulation from 4 to 14 ms. The dataset is adapted from Nylen and Wallisch, *Neural Data Science* (2017).

The repository is released under the MIT License. Keep this source note with any copied or modified course file.

## Macaque V4 multielectrode spike events

**Original public repository:** https://github.com/neural-data-science/Single-Unit-Data

**Original file:** `data/multielectrode_data.csv`

**Source study:** Snyder, Morais, Willis, and Smith (2015), "Global network influences on local functional connectivity," *Nature Neuroscience*, 18, 736-743. https://doi.org/10.1038/nn.3979

The public teaching file contains sorted spike events from a subset of channels recorded with a Utah array in macaque area V4. Trials include a 150 ms prestimulus interval and drifting gratings at 0 or 90 degrees. The full teaching file is about 22 MB, so the instructor should cache it once on JupyterHub before projects begin.

Run:

```bash
python scripts/prepare_open_spike_data.py
```

The script downloads the event table to a user or shared cache and creates a trial-by-channel response-count table for decoding and PCA projects.

## Optional advanced repositories

Teams may use an instructor-approved prepared subset from the International Brain Laboratory, DANDI Archive, or Allen Institute. Direct use of a large API or NWB archive is optional because data access and preprocessing can otherwise become the project instead of the neuroscience question.

## Provenance requirement

Every data project README and report must state:

1. the original repository and file or dataset identifier;
2. the source study or teaching source;
3. what one row and each major column represent;
4. units and analysis windows;
5. any filtering, aggregation, or derived variables;
6. the license or reuse statement supplied by the source;
7. whether the team used the complete teaching file or a course-prepared subset.
