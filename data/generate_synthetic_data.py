import numpy as np
import pandas as pd
import datetime

np.random.seed(42)

n = 5000

age_at_diagnosis_months = np.random.normal(48, 12, n)
age_at_diagnosis_months = np.clip(age_at_diagnosis_months, 12, 120)

cutoff_months = 36
treatment = (age_at_diagnosis_months < cutoff_months).astype(int)

distance_from_cutoff = age_at_diagnosis_months - cutoff_months

baseline_iq = np.random.normal(85, 20, n)
baseline_iq = np.clip(baseline_iq, 40, 160)

baseline_adaptive = np.random.normal(70, 15, n)
baseline_adaptive = np.clip(baseline_adaptive, 30, 120)

treatment_effect_iq = 8
treatment_effect_adaptive = 12
treatment_effect_employment = 0.15
treatment_effect_independent = 0.20

iq_age_10 = (baseline_iq + 
             treatment * treatment_effect_iq + 
             np.random.normal(0, 5, n) - 
             0.3 * distance_from_cutoff)

adaptive_age_10 = (baseline_adaptive + 
                   treatment * treatment_effect_adaptive + 
                   np.random.normal(0, 4, n) - 
                   0.25 * distance_from_cutoff)

prob_employed = (0.3 + treatment * treatment_effect_employment + 
                 0.002 * baseline_iq - 0.001 * distance_from_cutoff)
prob_employed = np.clip(prob_employed, 0, 1)
employed_age_25 = np.random.binomial(1, prob_employed)

prob_independent = (0.25 + treatment * treatment_effect_independent + 
                    0.003 * baseline_adaptive - 0.002 * distance_from_cutoff)
prob_independent = np.clip(prob_independent, 0, 1)
independent_living_age_25 = np.random.binomial(1, prob_independent)

gender = np.random.choice(['Male', 'Female'], n, p=[0.8, 0.2])
race = np.random.choice(['White', 'Black', 'Hispanic', 'Asian', 'Other'], 
                       n, p=[0.6, 0.15, 0.15, 0.05, 0.05])
parent_education = np.random.choice(['High School', 'Some College', 'Bachelor', 'Graduate'], 
                                   n, p=[0.25, 0.25, 0.30, 0.20])
household_income = np.random.lognormal(10.8, 0.8, n)
household_income = np.clip(household_income, 10000, 500000)

diagnosis_year = np.random.randint(2010, 2020, n)
birth_year = diagnosis_year - (age_at_diagnosis_months / 12).astype(int)

early_intervention_hours = np.where(
    treatment == 1,
    np.random.normal(25, 5, n),
    np.random.normal(15, 5, n)
)
early_intervention_hours = np.clip(early_intervention_hours, 0, 40)

school_services = np.where(
    treatment == 1,
    np.random.binomial(1, 0.85, n),
    np.random.binomial(1, 0.65, n)
)

parent_stress = np.where(
    treatment == 1,
    np.random.normal(45, 10, n),
    np.random.normal(55, 10, n)
)

df = pd.DataFrame({
    'id': range(1, n+1),
    'age_diagnosis_months': age_at_diagnosis_months,
    'diagnosed_before_3': treatment,
    'distance_from_cutoff': distance_from_cutoff,
    'gender': gender,
    'race': race,
    'parent_education': parent_education,
    'household_income': household_income,
    'diagnosis_year': diagnosis_year,
    'birth_year': birth_year,
    'baseline_iq': baseline_iq,
    'baseline_adaptive': baseline_adaptive,
    'iq_age_10': iq_age_10,
    'adaptive_age_10': adaptive_age_10,
    'employed_age_25': employed_age_25,
    'independent_living_age_25': independent_living_age_25,
    'early_intervention_hours': early_intervention_hours,
    'school_services': school_services,
    'parent_stress_score': parent_stress
})

df.to_csv('/Users/maxghenis/autism-diagnosis/data/autism_synthetic_data.csv', index=False)
print(f"Generated synthetic dataset with {n} observations")
print(f"Mean age at diagnosis: {df['age_diagnosis_months'].mean():.1f} months")
print(f"Proportion diagnosed before 3: {df['diagnosed_before_3'].mean():.2%}")