
#Genetic Variants and Risk Assessment 

""" Performance Metrics Overview
1. Prevalence of High-Risk Genetic Variants

    Current: Identification of 2-3 key variants
    Target: Identify > 5 key variants associated with myocardial infarction (MI) risk
    Data Source: Population Genomic Studies, Literature Review

2. Risk Stratification Accuracy

    Current: 75-80%
    Target: 90% accuracy in predicting high-risk individuals
    Data Source: Risk Assessment Models, Clinical Validation

3. Genetic Risk Score (GRS) Calculation

    Current: Identification of 70-80% of high-risk individuals
    Target: 100% identification
    Data Source: Genotype-Phenotype Association Studies

4. Response to Treatment Variability

    Current: 60-70% correlation with treatment outcomes
    Target: ≥ 80% correlation
    Data Source: Clinical Trials, Pharmacogenomics Studies#
"""




import numpy as np

# Define targets and benchmarks
benchmarks = {
    "Prevalence of High-Risk Variants": {"current": 3, "target": 5, "unit": "variants"},
    "Risk Stratification Accuracy": {"current": 0.775, "target": 0.90, "unit": ""},
    "Genetic Risk Score Identification": {"current": 0.75, "target": 1.00, "unit": ""},
    "Response to Treatment Correlation": {"current": 0.65, "target": 0.80, "unit": ""},
}

# Simulate metrics calculation
def simulate_genetic_risk(num_samples=1000, high_risk_genes=5):
    """
    Simulates metrics for genetic risk and treatment variability.
    Args:
        num_samples (int): Total number of individuals in the study.
        high_risk_genes (int): Total number of high-risk genes being tracked.
    Returns:
        dict: Performance metrics.
    """
    np.random.seed(42)

    # Simulate prevalence of high-risk variants
    detected_variants = np.random.randint(2, 4)  # Simulate 2-3 detected variants

    # Simulate risk stratification accuracy
    risk_accuracy = np.random.uniform(0.75, 0.80)  # Current accuracy 75-80%

    # Simulate GRS identification rate
    grs_identification = np.random.uniform(0.70, 0.80)  # Current 70-80%

    # Simulate treatment variability correlation
    treatment_correlation = np.random.uniform(0.60, 0.70)  # Current 60-70%

    return {
        "Prevalence of High-Risk Variants": detected_variants,
        "Risk Stratification Accuracy": round(risk_accuracy, 3),
        "Genetic Risk Score Identification": round(grs_identification, 3),
        "Response to Treatment Correlation": round(treatment_correlation, 3),
    }

# Run simulation
metrics = simulate_genetic_risk()

# Display metrics
def display_metrics(metrics, benchmarks):
    print(f"{'Metric':<35} {'Current':<15} {'Target':<15} {'Status':<10}")
    print("-" * 80)
    for metric, value in metrics.items():
        target = benchmarks[metric]["target"]
        unit = benchmarks[metric]["unit"]
        status = "Meets" if (
            value >= target if metric != "Response to Treatment Correlation" else value >= target
        ) else "Below"
        print(f"{metric:<35} {value:<15}{target} {unit:<10} {status:<10}")

print("Genetic Variants and Risk Assessment Metrics\n")
display_metrics(metrics, benchmarks)
