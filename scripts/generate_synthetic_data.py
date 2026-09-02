#!/usr/bin/env python3
"""Regenerate small synthetic tables bundled with the course.

The tables produced here are teaching constructions, not recorded data and not
the outputs of validated biophysical models. Keeping their generation explicit
makes provenance and expected values inspectable.
"""
from __future__ import annotations

import csv
import math
from pathlib import Path
import random


COURSE_ROOT = Path(__file__).resolve().parents[1]
DATA = COURSE_ROOT / "data"


def interpolate(time_ms: float, anchors: tuple[tuple[float, float], ...]) -> float:
    """Linearly interpolate a value between ordered anchor points."""

    for (left_t, left_v), (right_t, right_v) in zip(anchors, anchors[1:]):
        if left_t <= time_ms <= right_t:
            fraction = (time_ms - left_t) / (right_t - left_t)
            return left_v + fraction * (right_v - left_v)
    raise ValueError(f"time {time_ms} ms lies outside the anchor range")


def write_membrane_signal() -> Path:
    """Write a recognizable, illustrative action-potential-shaped trace."""

    anchors = (
        (0.0, -70.0),
        (6.5, -70.0),
        (7.0, -65.0),
        (7.5, -50.0),
        (8.0, -20.0),
        (8.5, 15.0),
        (9.0, 35.0),
        (9.5, 20.0),
        (10.0, -10.0),
        (11.0, -55.0),
        (12.0, -78.0),
        (14.0, -75.0),
        (18.0, -72.0),
        (25.0, -70.0),
        (49.5, -70.0),
    )
    output = DATA / "membrane_signal.csv"
    with output.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.writer(stream, lineterminator="\n")
        writer.writerow(("time_ms", "current_nA", "voltage_mV"))
        for index in range(100):
            time_ms = index * 0.5
            current_nA = 0.6 if 5.0 <= time_ms < 7.0 else 0.0
            voltage_mV = interpolate(time_ms, anchors)
            writer.writerow(
                (
                    f"{time_ms:.1f}",
                    f"{current_nA:.1f}",
                    f"{voltage_mV:.6f}".rstrip("0").rstrip("."),
                )
            )
    return output


def fi_rows() -> list[tuple[float, float]]:
    """Construct repeated illustrative f-I observations with a fixed seed.

    The deterministic mean rule is zero below 0.10 nA and increases by 250 Hz
    per nA above that point. Gaussian teaching noise (5 Hz standard deviation)
    is added and negative rates are clipped to zero. This is not a fitted model
    and the rows are not measurements.
    """

    generator = random.Random(395)
    rows: list[tuple[float, float]] = []
    for current_nA in (0.08, 0.12, 0.16, 0.20, 0.24):
        mean_rate_hz = max(0.0, (current_nA - 0.10) * 250.0)
        for _ in range(12):
            rate_hz = max(0.0, mean_rate_hz + generator.gauss(0.0, 5.0))
            rows.append((current_nA, rate_hz))
    return rows


def write_synthetic_fi_observations() -> list[Path]:
    """Write the same explicit teaching table to its two bundled locations."""

    destinations = [DATA / "synthetic_fi_observations.csv"]
    project_data = COURSE_ROOT.parent / "project" / "starters" / "data"
    if project_data.is_dir():
        destinations.append(project_data / "synthetic_fi_observations.csv")

    rows = fi_rows()
    for output in destinations:
        with output.open("w", encoding="utf-8", newline="") as stream:
            writer = csv.writer(stream, lineterminator="\n")
            writer.writerow(("input_current_nA", "synthetic_rate_hz"))
            for current_nA, rate_hz in rows:
                writer.writerow((f"{current_nA:.2f}", f"{rate_hz:.6f}"))
    return destinations


def write_first_spike_counts() -> Path:
    """Write a tiny fixed table for first table-reading demonstrations."""

    observations = (
        (1, 3, "quiet"),
        (2, 5, "quiet"),
        (3, 4, "quiet"),
        (4, 8, "quiet"),
        (5, 7, "quiet"),
        (6, 10, "quiet"),
        (7, 6, "loud"),
        (8, 9, "loud"),
        (9, 12, "loud"),
        (10, 8, "loud"),
        (11, 11, "loud"),
        (12, 7, "loud"),
    )
    output = DATA / "first_spike_counts.csv"
    with output.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.writer(stream, lineterminator="\n")
        writer.writerow(
            ("trial", "spike_count", "window_ms", "stimulus", "firing_rate_hz")
        )
        for trial, count, stimulus in observations:
            writer.writerow((trial, count, 500, stimulus, f"{count / 0.5:.1f}"))
    return output


def write_auditory_trials() -> Path:
    """Write a synthetic, peaked frequency-response teaching table."""

    generator = random.Random(39501)
    settings = (
        (500, 4.0, 2.2, 0),
        (1000, 10.0, 4.0, 0),
        (2000, 20.0, 5.0, 0),
        (4000, 10.0, 4.0, 1),
        (8000, 4.0, 2.2, 1),
    )
    output = DATA / "auditory_trials.csv"
    with output.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.writer(stream, lineterminator="\n")
        writer.writerow(
            (
                "trial",
                "frequency_hz",
                "spike_count",
                "window_s",
                "firing_rate_hz",
                "choice",
            )
        )
        trial = 1
        for frequency_hz, mean_count, sd_count, choice in settings:
            for _ in range(24):
                count = max(0, round(generator.gauss(mean_count, sd_count)))
                writer.writerow((trial, frequency_hz, count, "0.5", f"{count / 0.5:.1f}", choice))
                trial += 1
    return output


def write_two_neuron_geometry() -> Path:
    """Write two synthetic correlated response clouds for geometry practice."""

    generator = random.Random(39502)
    output = DATA / "two_neuron_geometry.csv"
    with output.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.writer(stream, lineterminator="\n")
        writer.writerow(("condition", "neuron_1_hz", "neuron_2_hz"))
        for condition, mean_1, mean_2 in (("A", 4.0, 3.2), ("B", 7.1, 6.7)):
            for _ in range(60):
                shared = generator.gauss(0.0, 1.0)
                response_1 = max(0.0, mean_1 + shared + generator.gauss(0.0, 0.55))
                response_2 = max(0.0, mean_2 + 0.8 * shared + generator.gauss(0.0, 0.70))
                writer.writerow((condition, f"{response_1:.6f}", f"{response_2:.6f}"))
    return output


def write_population_trials() -> Path:
    """Write synthetic population rates with one shared stimulus dimension."""

    generator = random.Random(39503)
    weights = (-1.8, -1.5, -1.2, -0.8, -0.4, -0.1, 0.1, 0.4, 0.8, 1.2, 1.5, 1.8)
    output = DATA / "population_trials.csv"
    neuron_columns = tuple(f"neuron_{index:02d}_hz" for index in range(1, 13))
    with output.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.writer(stream, lineterminator="\n")
        writer.writerow(("trial", "choice", "stimulus_value", *neuron_columns))
        for trial in range(1, 181):
            stimulus = generator.gauss(0.0, 1.0)
            choice = int(stimulus + generator.gauss(0.0, 0.75) >= 0.0)
            shared_noise = generator.gauss(0.0, 0.7)
            responses = [
                max(
                    0.0,
                    9.0
                    + weight * stimulus
                    + shared_noise
                    + generator.gauss(0.0, 1.1),
                )
                for weight in weights
            ]
            writer.writerow(
                (
                    trial,
                    choice,
                    f"{stimulus:.6f}",
                    *(f"{response:.6f}" for response in responses),
                )
            )
    return output


def poisson_sample(mean: float, generator: random.Random) -> int:
    """Draw one Poisson count using Knuth's algorithm."""

    threshold = math.exp(-mean)
    product = 1.0
    count = 0
    while product > threshold:
        count += 1
        product *= generator.random()
    return count - 1


def write_spike_times() -> Path:
    """Write synthetic event times with a larger post-tone event rate."""

    generator = random.Random(39504)
    output = DATA / "spike_times.csv"
    with output.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.writer(stream, lineterminator="\n")
        writer.writerow(("trial", "condition", "spike_time_s"))
        for condition, response_mean in (("silence", 3.5), ("tone", 12.0)):
            for trial in range(1, 21):
                times = [
                    generator.uniform(-0.3, 0.0)
                    for _ in range(poisson_sample(2.0, generator))
                ]
                times.extend(
                    generator.uniform(0.0, 0.4)
                    for _ in range(poisson_sample(response_mean, generator))
                )
                for spike_time_s in sorted(times):
                    writer.writerow((trial, condition, f"{spike_time_s:.6f}"))
    return output


def main() -> int:
    paths = [
        write_membrane_signal(),
        *write_synthetic_fi_observations(),
        write_first_spike_counts(),
        write_auditory_trials(),
        write_two_neuron_geometry(),
        write_population_trials(),
        write_spike_times(),
    ]
    for path in paths:
        try:
            label = path.relative_to(COURSE_ROOT)
        except ValueError:
            label = path.relative_to(COURSE_ROOT.parent)
        print(f"wrote {label}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
