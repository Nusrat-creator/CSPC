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

## PW2 - Lab B: Optimization Algorithms

**Three routes to a minimum:**
- On the easy convex function $f(x)$, Gradient Descent, Newton's Method, and SLSQP all easily agree on the global minimum at $x=3$.
- On the harder landscape $g(x)$, starting from $x_0=0$ causes the methods to disagree: Gradient Descent and SLSQP find a local minimum, but Newton's method zeroes in on the nearest stationary point, which happens to be a local maximum ($g'' < 0$).
- When changing the starting point to $x_0=2$, all three methods successfully find and agree on the same local minimum. 
- **Key Lesson:** On complicated landscapes, the choice of algorithm and the initial starting point drastically change the final result.BY NUSRAT SEYIDZADE DATE IS 5 OCTOBER 2026 CS2 2025 L1

## PW2 --- Lab B Report

* **Optimization Methods Comparison:** Gradient Descent, Newton's method, and SLSQP easily agreed on a simple convex function. However, on a harder landscape with multiple stationary points, their success and agreement depended entirely on the starting point.
* **Fitted Rate Constant:** Using curve-fitting (minimizing squared error), the rate constant $k$ for the first-order reaction was found to be approximately 0.26.
* **Equilibrium Composition:** Both root-finding (Newton) and minimization (SLSQP) found the extent of reaction to be $x \approx 0.66$. This yields an equilibrium composition of roughly 0.33 mol H2, 0.33 mol I2, and 1.33 mol HI.
* **Titration Equivalence Point (Bonus):** By calculating the derivative of the pH curve and finding its maximum slope, the equivalence point was numerically located at approximately 50 mL.

## PW2 --- Lab B Report

* **Optimization Methods Comparison:** Gradient Descent, Newton's method, and SLSQP easily agreed on a simple convex function. However, on a harder landscape with multiple stationary points, their success and agreement depended entirely on the starting point.
* **Fitted Rate Constant:** Using curve-fitting (minimizing squared error), the rate constant $k$ for the first-order reaction was found to be approximately 0.26.
* **Equilibrium Composition:** Both root-finding (Newton) and minimization (SLSQP) found the extent of reaction to be $x \approx 0.66$. This yields an equilibrium composition of roughly 0.33 mol H2, 0.33 mol I2, and 1.33 mol HI.
* **Titration Equivalence Point (Bonus):** By calculating the derivative of the pH curve and finding its maximum slope, the equivalence point was numerically located at approximately 50 mL.

## PW3 - Session 2: Draw Conclusions

**Is the effect real? (Heart Disease vs Thalach):**
- A Mann-Whitney U test confirmed that heart disease patients reach a significantly lower maximum heart rate (`thalach`) compared to healthy patients ($p < 0.001$).
- Displaying group means with Standard Error of the Mean (SEM) error bars clearly separates the two populations beyond visual uncertainty.

**Do two things move together? (Age vs Thalach):**
- Age and `thalach` display a moderate negative correlation ($r \approx -0.40, p < 0.001$), demonstrating that maximum achievable heart rate decreases systematically as age increases.

**Chemical-Exposure Mystery (Confounding Variables):**
- **Naive Analysis:** At face value, one chemical appeared far more strongly associated with tumor malignancy score.
- **Controlling for Pollution Index:** Restricting the cohort to patients with similar area pollution indices ($40 < \text{pollution\_index} < 60$) caused the naive association to collapse. The third variable (`pollution_index`) was the true underlying driver influencing both chemical exposure and malignancy score.

**Bonus (Category Unpredictability):**
- Calculated Shannon entropy on the target class proportions yields a value close to $1.0\text{ bit}$, indicating a nearly balanced distribution that represents maximum unpredictability for binary classification.

## PW3 --- Data Characterisation and Chemical Mystery Report

### Session 1: Data Characterisation & Normality Verdicts
* **age:** Approximately normal (bell-shaped distribution, low skewness).
* **chol:** Not normal (right-skewed with extreme high-value outliers above 400 mg/dL, Shapiro-Wilk test $p < 0.05$).
* **trestbps:** Not normal (right-skewed due to clinical measurement clustering, Shapiro-Wilk test $p < 0.05$).
* **thalach:** Not normal (left-skewed toward higher max heart rates, Shapiro-Wilk test $p < 0.05$).

### Session 2: Heart Rate & Age Analysis
* **Heart Rate Comparison (`thalach`):** Non-parametric Mann-Whitney U test confirmed that heart disease patients reach a significantly lower maximum heart rate ($\approx 139$ bpm) compared to healthy patients ($\approx 158$ bpm, $p < 0.001$).
* **Age vs. Heart Rate Relationship:** Spearman correlation ($r \approx -0.40, p < 0.001$) demonstrated a significant negative trend: maximum heart rate decreases systematically as age increases.

### Chemical Exposure Mystery: Correlation vs. Causation
* **Naive Conclusion:** At face value, `benzene` showed a strong positive correlation with tumor malignancy, making it look guilty, while `cadmium` appeared weak.
* **Controlling for Confounding Variable (`pollution_index`):** When restricting the cohort to patients in the same pollution band ($40 < \text{pollution\_index} < 60$), the correlation between `benzene` and malignancy completely vanished ($r \approx 0$). Meanwhile, `cadmium` showed a strong positive association with malignancy across all pollution tiers.
* **Final Verdict:** `cadmium` is the actual chemical that drives malignancy. `benzene` only appeared guilty because high benzene concentrations co-occurred with high area pollution levels, which acted as a confounding variable.
