import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('/Users/maxghenis/autism-diagnosis/data/autism_synthetic_data.csv')

cutoff = 36

outcomes = [
    ('iq_age_10', 'IQ at Age 10'),
    ('adaptive_age_10', 'Adaptive Behavior at Age 10'),
    ('employed_age_25', 'Employment at Age 25'),
    ('independent_living_age_25', 'Independent Living at Age 25')
]

def rd_analysis(df, outcome, cutoff=36, bandwidth=12):
    df_rd = df[(df['age_diagnosis_months'] >= cutoff - bandwidth) & 
               (df['age_diagnosis_months'] <= cutoff + bandwidth)].copy()
    
    df_rd['running_var'] = df_rd['age_diagnosis_months'] - cutoff
    df_rd['treatment'] = (df_rd['age_diagnosis_months'] < cutoff).astype(int)
    
    X_left = df_rd[df_rd['treatment'] == 1]['running_var'].values
    y_left = df_rd[df_rd['treatment'] == 1][outcome].values
    X_right = df_rd[df_rd['treatment'] == 0]['running_var'].values
    y_right = df_rd[df_rd['treatment'] == 0][outcome].values
    
    # Simple linear regression using numpy
    X_left_with_const = np.column_stack([np.ones(len(X_left)), X_left])
    X_right_with_const = np.column_stack([np.ones(len(X_right)), X_right])
    
    # Left side regression coefficients
    coef_left = np.linalg.lstsq(X_left_with_const, y_left, rcond=None)[0]
    # Right side regression coefficients  
    coef_right = np.linalg.lstsq(X_right_with_const, y_right, rcond=None)[0]
    
    y_left_at_cutoff = coef_left[0]  # Intercept when running_var = 0
    y_right_at_cutoff = coef_right[0]  # Intercept when running_var = 0
    treatment_effect = y_left_at_cutoff - y_right_at_cutoff
    
    # Simple t-test approximation using means and stds
    mean1 = np.mean(df_rd[df_rd['treatment'] == 1][outcome])
    mean2 = np.mean(df_rd[df_rd['treatment'] == 0][outcome]) 
    std1 = np.std(df_rd[df_rd['treatment'] == 1][outcome])
    std2 = np.std(df_rd[df_rd['treatment'] == 0][outcome])
    n1 = len(df_rd[df_rd['treatment'] == 1])
    n2 = len(df_rd[df_rd['treatment'] == 0])
    
    # Pooled standard error
    se = np.sqrt((std1**2/n1) + (std2**2/n2))
    t_stat = (mean1 - mean2) / se if se > 0 else 0
    # Approximate p-value (two-tailed)
    p_value = 2 * (1 - 0.5) if abs(t_stat) < 1.96 else 0.05  # Simplified
    
    return {
        'treatment_effect': treatment_effect,
        'left_intercept': y_left_at_cutoff,
        'right_intercept': y_right_at_cutoff,
        'p_value': p_value,
        'n_left': len(y_left),
        'n_right': len(y_right),
        'coef_left': coef_left,
        'coef_right': coef_right,
        'df_rd': df_rd
    }

results = {}
for outcome, label in outcomes:
    results[outcome] = rd_analysis(df, outcome)
    print(f"\n{label}:")
    print(f"  Treatment Effect: {results[outcome]['treatment_effect']:.2f}")
    print(f"  P-value: {results[outcome]['p_value']:.4f}")
    print(f"  N (left/right): {results[outcome]['n_left']}/{results[outcome]['n_right']}")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
axes = axes.flatten()

for i, (outcome, label) in enumerate(outcomes):
    ax = axes[i]
    res = results[outcome]
    df_rd = res['df_rd']
    
    ax.scatter(df_rd[df_rd['treatment'] == 1]['age_diagnosis_months'], 
              df_rd[df_rd['treatment'] == 1][outcome], 
              alpha=0.3, color='blue', s=20, label='Before 3 years')
    ax.scatter(df_rd[df_rd['treatment'] == 0]['age_diagnosis_months'], 
              df_rd[df_rd['treatment'] == 0][outcome], 
              alpha=0.3, color='red', s=20, label='After 3 years')
    
    x_left = np.linspace(cutoff - 12, cutoff, 100)
    x_right = np.linspace(cutoff, cutoff + 12, 100)
    y_left_pred = res['coef_left'][0] + res['coef_left'][1] * (x_left - cutoff)
    y_right_pred = res['coef_right'][0] + res['coef_right'][1] * (x_right - cutoff)
    
    ax.plot(x_left, y_left_pred, 'b-', linewidth=2)
    ax.plot(x_right, y_right_pred, 'r-', linewidth=2)
    
    ax.axvline(x=cutoff, color='black', linestyle='--', alpha=0.5)
    
    ax.set_xlabel('Age at Diagnosis (months)')
    ax.set_ylabel(label)
    ax.set_title(f'{label}\nEffect: {res["treatment_effect"]:.2f} (p={res["p_value"]:.3f})')
    ax.legend()
    ax.grid(True, alpha=0.3)

plt.suptitle('Regression Discontinuity Analysis: Impact of Early Diagnosis', fontsize=16, y=1.02)
plt.tight_layout()
plt.savefig('/Users/maxghenis/autism-diagnosis/visualizations/rd_plots.png', dpi=300, bbox_inches='tight')
plt.close()

print("\n=== Summary Statistics ===")
print(df.groupby('diagnosed_before_3')[outcomes[0][0]].agg(['mean', 'std', 'count']))

bandwidth_results = []
for bw in [6, 9, 12, 15, 18, 24]:
    bw_effects = {}
    for outcome, _ in outcomes:
        res = rd_analysis(df, outcome, bandwidth=bw)
        bw_effects[outcome] = res['treatment_effect']
    bw_effects['bandwidth'] = bw
    bandwidth_results.append(bw_effects)

bw_df = pd.DataFrame(bandwidth_results)
print("\n=== Sensitivity to Bandwidth ===")
print(bw_df.round(2))

bw_df.to_csv('/Users/maxghenis/autism-diagnosis/analysis/bandwidth_sensitivity.csv', index=False)