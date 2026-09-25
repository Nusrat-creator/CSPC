# CSPC - Computer Science for Physics and Chemistry

My coursework repository. Each practical is under PW<n>/Lab <X>/.

## Setup
Create the environment for a given lab:
conda env create -f PW<n>/Lab\ <X>/environment.yml
conda activate cspc

---

## PW1 - Lab A: Reproducible Foundations

**What I built:**
- Directory hierarchy, Conda environment, pytest test suite, and speed benchmark for radioactive decay simulation.

**Speed comparison (loop vs NumPy):**
- loop : 0.45 s
- numpy : 0.02 s
- speed-up: 22.5x faster

**Tests:** all passing? yes

**Conclusion:**
- Using NumPy vectorization significantly improves simulation performance compared to standard Python loops. All three pytest functions pass without error, verifying numerical accuracy by nusrat seyidzde 14 september 2026.

## PW1 - Lab B: Visualization and Automation

**What the data showed:**
- The observed radioactive decay data (`decay_observed.csv`) follows an exponential decrease in particle counts over time

**Match with analytical law:**
- The observed data points closely match the theoretical analytical curve ($N_0 e^{-\lambda t}$) shown on the right side of the generated figure

**Snakemake pipeline role:**
- The Snakemake pipeline automates the generation of `figure.png` from `decay_observed.csv` using `plot.py`, tracking file timestamps to prevent redundant re-computations[cite: 15, 17].BY NUSRAT SEYIDZADE

## PW2 - Lab A: Derivatives and Noise

**The Noise Problem:**
- The calculated acceleration is highly noisy because it requires taking the derivative twice, a process that compares nearby measurements and heavily magnifies small measurement errors present in the original position data.BY NUSRAT SEYIDZADE LAST UPDATE 25.09.2026

**Integration and Noise Recovery:**
- Because integration behaves as a sum, it suppresses noise (the opposite of differentiation). Integrating the highly noisy acceleration data twice recovered the original position data with a maximum error of roughly 1 metre.BY NUSRAT SEYIDZADE

## PW2 --- Lab A Report

* **Mean Acceleration:** The measured mean acceleration of the falling object was roughly -9.81 m/s^2, confirming free fall.
* **Noise Observation:** The computed acceleration was highly noisy because calculating derivatives magnifies the small, random measurement errors present in the original position data.
* **Integration Recovery:** Integrating the noisy acceleration back up to position suppressed the noise, recovering the original position track within roughly 1 metre.BY NUSRAT SEYIDZADE
