"""Small, transparent utilities for NSCI 395 notebooks.

The course keeps the central scientific computations visible in notebooks.
These helpers remove only repetitive setup and plotting code.
"""
from __future__ import annotations

from pathlib import Path
from typing import Iterable

import numpy as np
import matplotlib.pyplot as plt


def set_course_seed(seed: int = 395) -> np.random.Generator:
    """Return a reproducible NumPy random-number generator."""
    return np.random.default_rng(seed)


def clean_axes(ax: plt.Axes | None = None) -> plt.Axes:
    """Apply a restrained, readable axes layout.

    Call it with no argument straight after a ``plt.plot`` style figure, or
    pass an explicit axes object.
    """
    ax = plt.gca() if ax is None else ax
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    return ax


def passive_membrane(
    current_nA: np.ndarray,
    dt_ms: float = 0.1,
    resistance_MOhm: float = 100.0,
    capacitance_nF: float = 0.1,
    e_leak_mV: float = -70.0,
    initial_voltage_mV: float | None = None,
) -> np.ndarray:
    """Simulate a passive RC membrane with forward Euler integration.

    Units are chosen so that nA * MOhm = mV and MOhm * nF = ms.
    """
    current_nA = np.asarray(current_nA, dtype=float)
    if current_nA.ndim != 1:
        raise ValueError('current_nA must be one-dimensional')
    if dt_ms <= 0 or resistance_MOhm <= 0 or capacitance_nF <= 0:
        raise ValueError('dt, resistance, and capacitance must be positive')

    voltage = np.empty_like(current_nA, dtype=float)
    voltage[0] = e_leak_mV if initial_voltage_mV is None else initial_voltage_mV
    for i in range(len(voltage) - 1):
        dVdt = (
            -(voltage[i] - e_leak_mV) / resistance_MOhm + current_nA[i]
        ) / capacitance_nF
        voltage[i + 1] = voltage[i] + dt_ms * dVdt
    return voltage


def lif_neuron(
    current_nA: np.ndarray,
    dt_ms: float = 0.1,
    resistance_MOhm: float = 100.0,
    capacitance_nF: float = 0.1,
    e_leak_mV: float = -70.0,
    threshold_mV: float = -50.0,
    reset_mV: float = -65.0,
    refractory_ms: float = 2.0,
    initial_voltage_mV: float | None = None,
) -> tuple[np.ndarray, np.ndarray]:
    """Simulate a leaky integrate-and-fire neuron.

    Returns
    -------
    voltage_mV : ndarray
        Recorded membrane voltage, including reset and refractory samples.
    spike_indices : ndarray
        Integer sample indices at which threshold was crossed.
    """
    current_nA = np.asarray(current_nA, dtype=float)
    if current_nA.ndim != 1:
        raise ValueError('current_nA must be one-dimensional')
    if dt_ms <= 0:
        raise ValueError('dt_ms must be positive')

    voltage = np.empty_like(current_nA, dtype=float)
    voltage[0] = e_leak_mV if initial_voltage_mV is None else initial_voltage_mV
    refractory_steps = int(round(refractory_ms / dt_ms))
    remaining_refractory = 0
    spikes: list[int] = []

    for i in range(len(voltage) - 1):
        if remaining_refractory > 0:
            voltage[i + 1] = reset_mV
            remaining_refractory -= 1
            continue

        dVdt = (
            -(voltage[i] - e_leak_mV) / resistance_MOhm + current_nA[i]
        ) / capacitance_nF
        candidate = voltage[i] + dt_ms * dVdt
        if candidate >= threshold_mV:
            spikes.append(i + 1)
            voltage[i + 1] = reset_mV
            remaining_refractory = refractory_steps
        else:
            voltage[i + 1] = candidate

    return voltage, np.asarray(spikes, dtype=int)


def spike_times_to_counts(
    spike_times_ms: Iterable[np.ndarray],
    bin_edges_ms: np.ndarray,
) -> np.ndarray:
    """Bin each trial's spike times into a trial-by-bin count matrix."""
    return np.vstack([
        np.histogram(np.asarray(times), bins=bin_edges_ms)[0]
        for times in spike_times_ms
    ])


def psth_hz(counts: np.ndarray, bin_width_ms: float) -> np.ndarray:
    """Convert per-trial spike counts into a trial-averaged rate in Hz.

    ``counts`` is a trials-by-bins matrix. Every trial in the experimental
    design must be present, including trials with no spikes, or the average
    is taken over the wrong denominator.
    """
    counts = np.asarray(counts)
    return counts.mean(axis=0) / (bin_width_ms / 1000.0)


def simulate_ei_network(
    external_e: np.ndarray,
    external_i: np.ndarray | None = None,
    dt: float = 0.1,
    tau_e: float = 10.0,
    tau_i: float = 15.0,
    w_ee: float = 1.2,
    w_ei: float = 1.0,
    w_ie: float = 1.1,
    w_ii: float = 0.4,
    initial: tuple[float, float] = (0.05, 0.05),
) -> tuple[np.ndarray, np.ndarray]:
    """Simulate a bounded two-population E-I rate model."""
    external_e = np.asarray(external_e, dtype=float)
    if external_i is None:
        external_i = np.zeros_like(external_e)
    external_i = np.asarray(external_i, dtype=float)
    if external_e.shape != external_i.shape:
        raise ValueError('external_e and external_i must have the same shape')

    e = np.zeros_like(external_e)
    i = np.zeros_like(external_i)
    e[0], i[0] = initial

    def activation(x: float | np.ndarray) -> float | np.ndarray:
        return np.maximum(0.0, np.tanh(x))

    for t in range(len(e) - 1):
        drive_e = w_ee * e[t] - w_ei * i[t] + external_e[t]
        drive_i = w_ie * e[t] - w_ii * i[t] + external_i[t]
        e[t + 1] = e[t] + dt * (-e[t] + activation(drive_e)) / tau_e
        i[t + 1] = i[t] + dt * (-i[t] + activation(drive_i)) / tau_i
    return e, i


def find_course_root(start: Path | None = None) -> Path:
    """Find the course root from a notebook nested within the repository.

    Notebook setup cells cannot use this, because the course root has to be
    on ``sys.path`` before this module can be imported. It is here for
    scripts and for project repositories that already import course_utils.
    """
    current = Path.cwd() if start is None else Path(start)
    for candidate in [current, *current.parents]:
        if (candidate / 'course_utils.py').exists():
            return candidate
    raise FileNotFoundError('Could not locate course_utils.py in this directory tree')
