def calculate_premium(age, smoker):
    """
    Calculate annual health insurance premium based on age and smoker status.
    Args:
        age (int): Policyholder's age
        smoker (bool): True if smoker, False otherwise
    Returns:
        float: Annual premium in dollars
    """
#all the calculations are done in INR 
    base_rate = 1000  # 500 for exepenses + 500 for base claim 
    profit_margin = 0.1 * base_rate  # 20% profit margin
    update_base_rate = base_rate + profit_margin  # Updated base rate with profit margin
    age_load = max(0, (age - 30) * 50)  # 50 INR loaded for each year over 30 
    smoker_load = 1000 if smoker else 0   # extra loading of 1000 inr for smokers
    return update_base_rate + age_load + smoker_load

if __name__ == "__main__":
    # Example usage
    print(f"Premium for 35-year-old smoker: ${calculate_premium(35, True)}")
    print(f"Premium for 25-year-old non-smoker: ${calculate_premium(25, False)}")