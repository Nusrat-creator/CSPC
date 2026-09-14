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
