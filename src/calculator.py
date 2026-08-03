from input_handler import get_rate_of_return_collection,get_length_of_time_collection,get_initial_investment_collection,get_contribute_monthly

def investment_growth_calculation(initial_invest: float, 
                      rate_of_ret: float, 
                      length_of_time:int, 
                      monthly_contributions:int) -> float:
    
    monthly__annual_rate = rate_of_ret / 12
    number_months = length_of_time * 12

    future_initial = initial_invest * (1 + monthly__annual_rate) ** number_months
    future_contribution = monthly_contributions * (((1 + monthly__annual_rate) ** number_months - 1) / monthly__annual_rate)

    future_value = round(future_initial + future_contribution, 2)

    return print(future_value)


def main():
    investment_growth_calculation(get_initial_investment_collection(), get_rate_of_return_collection(), get_length_of_time_collection(),get_contribute_monthly())

if __name__ == "__main__":
    main()