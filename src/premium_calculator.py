def calculate_premium(age, smoker,region=None, bmi_category=None):
    """
    Calculate annual health insurance premium based on age and smoker status.
    Args:
        age (int): Policyholder's age
        smoker (bool): True if smoker, False otherwise
        region (str): Region of policyholder (e.g., 'southwest', 'southeast')
    bmi_category (str): BMI category ('underweight', 'normal', 'overweight', 'obese')
    Returns:
        float: Annual premium in INR
    """

    # Input validation
    if not isinstance(age, (int, float)):
        raise TypeError("Age must be a number (integer or float)")
    if age < 0 or age > 120:
        raise ValueError("Age must be between 0 and 120")
    if not isinstance(smoker, bool):
        raise TypeError("Smoker must be a boolean (True/False)")
    valid_regions = ['southwest', 'southeast', 'northwest', 'northeast']
    if region and region not in valid_regions:
        raise ValueError(f"Region must be one of {valid_regions}")
    valid_bmi_categories = ['underweight', 'normal', 'overweight', 'obese']
    if bmi_category and bmi_category not in valid_bmi_categories:
        raise ValueError(f"BMI category must be one of {valid_bmi_categories}")


#all the calculations are done in INR 
    base_rate = 10000  
    profit_margin = 0.1 * base_rate  # 10% profit margin
    update_base_rate = base_rate + profit_margin  # Updated base rate with profit margin
    age_load = max(0, (age - 30) * 50)  # 50 INR loaded for each year over 30 
    prob_smok,prob_nonsmok =0.9964,0.1382 #probability of smoker and non smoker (from data)
    severity_smok,severity_nonsmok = 32050.231, 8434.268 # severity of claims for smoker and non smoker (from data)
    expected_claim = (prob_smok*severity_smok if smoker else prob_nonsmok*severity_nonsmok) # expected claim amount based on smoker status
    region_adjustments = {
            'southwest': 0,
            'southeast': 100,
            'northwest': -50,
            'northeast': 50
        }
    region_load = region_adjustments.get(region, 0)

        
    bmi_adjustments = {
            'underweight': 50,
            'normal': 0,
            'overweight': 100,
            'obese': 200
        }
    bmi_load = bmi_adjustments.get(bmi_category, 0)

    
    risk_margin = 0.1 * expected_claim
    total_premium = update_base_rate + age_load + region_load + bmi_load + risk_margin + expected_claim
    return total_premium

    


if __name__ == "__main__":
    # Example usage
    print(f"Premium for 35-year-old smoker: ${calculate_premium(35, True)}")
    print(f"Premium for 25-year-old non-smoker: ${calculate_premium(25, False)}")
    print(f"Premium for 19-year-old smoker: ${calculate_premium(19, True)}")