def calculate_premium(age, smoker):
    """
    Calculate annual health insurance premium based on age and smoker status.
    Args:
        age (int): Policyholder's age
        smoker (bool): True if smoker, False otherwise
    Returns:
        float: Annual premium in INR
    """
#all the calculations are done in INR 
    base_rate = 10000  
    profit_margin = 0.1 * base_rate  # 10% profit margin
    update_base_rate = base_rate + profit_margin  # Updated base rate with profit margin
    age_load = max(0, (age - 30) * 50)  # 50 INR loaded for each year over 30 
    prob_smok,prob_nonsmok =0.547,0.434 #probability of smoker and non smoker (from data)
    severity_smok,severity_nonsmok = 32050.231, 8434.268 # severity of claims for smoker and non smoker (from data)
    expected_claim = (prob_smok*severity_smok if smoker else prob_nonsmok*severity_nonsmok) # expected claim amount based on smoker status
    return update_base_rate + age_load + expected_claim

if __name__ == "__main__":
    # Example usage
    print(f"Premium for 35-year-old smoker: ${calculate_premium(35, True)}")
    print(f"Premium for 25-year-old non-smoker: ${calculate_premium(25, False)}")
    print(f"Premium for 19-year-old smoker: ${calculate_premium(19, True)}")