# Methodology

## Regression Discontinuity Design

We employ a sharp regression discontinuity (RD) design to identify the causal effect of early autism diagnosis on long-term outcomes. The running variable is the age at which a child enters the diagnostic assessment queue, with a discontinuity at 36 months when service responsibility transitions between organizations.

### Identification Strategy

Our identification exploits the following institutional feature: at age 3, responsibility for autism assessment and services transitions from Agency A (serving ages 0-3) to Agency B (serving ages 3+). This transition creates several sources of exogenous variation:

1. **Processing Delays**: Agency B has longer wait times (average 6 months vs 3 months for Agency A)
2. **Diagnostic Criteria**: Agency B applies slightly stricter diagnostic thresholds
3. **Service Intensity**: Agency A provides more intensive early intervention services

Children who enter the assessment queue just before their 3rd birthday are likely to be diagnosed and begin services before age 4. Those entering just after age 3 face delays that push diagnosis past age 4. This creates a discontinuity in diagnosis age around the cutoff.

### Estimating Equation

We estimate the following local linear regression:

$$Y_i = \alpha + \tau D_i + \beta_1 (A_i - c) + \beta_2 D_i \times (A_i - c) + \varepsilon_i$$

Where:
- $Y_i$ is the outcome for individual $i$
- $D_i = \mathbb{1}(A_i < c)$ indicates diagnosis before age 3
- $A_i$ is age at assessment queue entry
- $c = 36$ months is the cutoff
- $\tau$ is the treatment effect of early diagnosis

## Data

### Synthetic Data Generation

Given privacy constraints on actual autism registry data, we generate synthetic data that preserves key statistical properties observed in the literature:

- **Sample Size**: N = 5,000 individuals
- **Age at Diagnosis**: Mean = 48 months, SD = 12 months {cite}`maenner2023prevalence`
- **Gender Distribution**: 80% male, 20% female {cite}`loomes2017male`
- **Baseline IQ**: Mean = 85, SD = 20 {cite}`charman2011iq`
- **Treatment Effects**: Based on meta-analyses of early intervention studies {cite}`sandbank2020intervention`

### Outcome Variables

We examine four primary outcomes:

1. **IQ at Age 10**: Standardized cognitive assessment scores
2. **Adaptive Behavior at Age 10**: Vineland Adaptive Behavior Scales composite
3. **Employment at Age 25**: Binary indicator of paid employment
4. **Independent Living at Age 25**: Binary indicator of living independently

### Covariates

While RD designs do not require covariate adjustment for identification, we collect:
- Gender
- Race/ethnicity  
- Parental education
- Household income
- Geographic region

These variables allow us to test covariate balance and explore heterogeneous treatment effects.

## Estimation Procedures

### Bandwidth Selection

We implement multiple approaches to bandwidth selection:

1. **Optimal Bandwidth**: Using the {cite}`imbens2012optimal` procedure
2. **Fixed Bandwidths**: 6, 9, 12, 15, 18, and 24 months
3. **Cross-validation**: Leave-one-out CV to minimize mean squared error

Our main specification uses a 12-month bandwidth, including children assessed between 24-48 months.

### Local Linear Regression

We estimate separate linear regressions on each side of the cutoff:

**Left of cutoff (treated)**:
$$Y_i = \alpha_L + \beta_L (A_i - c) + \varepsilon_i \text{ for } A_i \in [c-h, c)$$

**Right of cutoff (control)**:
$$Y_i = \alpha_R + \beta_R (A_i - c) + \varepsilon_i \text{ for } A_i \in [c, c+h]$$

The treatment effect is: $\tau = \alpha_L - \alpha_R$

### Standard Errors

We calculate robust standard errors using the {cite}`calonico2014robust` procedure, which accounts for the bias-variance tradeoff in RD estimation.

## Validity Tests

### Manipulation Testing

We test for manipulation of the running variable using:
1. **McCrary Density Test**: {cite}`mccrary2008manipulation`
2. **Visual Inspection**: Histogram of assessment queue entry ages
3. **Bunching Analysis**: Test for excess mass just before cutoff

### Covariate Balance

We verify that predetermined covariates are balanced at the threshold:
$$X_i = \gamma + \delta D_i + \zeta (A_i - c) + \eta D_i \times (A_i - c) + \nu_i$$

A significant $\delta$ would suggest selection into treatment.

### Placebo Tests

We implement placebo tests at false cutoffs (30 and 42 months) where no discontinuity should exist.

## Robustness Checks

1. **Alternative Polynomials**: Quadratic and cubic specifications
2. **Donut RD**: Excluding observations immediately around cutoff
3. **Fuzzy RD**: Accounting for imperfect compliance
4. **Permutation Tests**: Randomization inference for finite-sample inference

## Software and Code

All analyses are conducted using Python 3.12 with the following packages:
- `pandas` for data manipulation
- `numpy` for numerical computation
- `matplotlib` for visualization
- `scikit-learn` for regression models
- `statsmodels` for statistical tests

Code is available at: https://github.com/maxghenis/autism-diagnosis