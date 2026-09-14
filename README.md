# CSPC Repository

## PW1 --- Lab A Report

### Speed Comparison Results
* **Pure-Python `simulate_loop` time**: Measured using `time.perf_counter()` on 200,000 atoms.
* **NumPy `simulate` time**: Measured using `time.perf_counter()` on 200,000 atoms.
* **Speed-up Factor**: NumPy implementation runs significantly faster than standard Python loops.

### Test Status
* All 3 pytest tests in `test_decay.py` passed successfully.

### Conclusion
Vectorized NumPy operations drastically reduce execution time compared to explicit Python loops when simulating large particle decay populations.
