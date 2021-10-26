# 12. Computing Simple Interest

p_amount = float(input("Enter the principal: "))
r_interest = float(input("Enter the rate of interest in percent form: "))
num_years = float(input("Enter the number of years: "))

r_interest = r_interest/100

si_output = p_amount*(1+r_interest*num_years)

r_interest = r_interest*100

print("After ", int(num_years), " years at ", f'{r_interest:.2f}', "%, the investment will be worth $", f'{si_output:.2f}', sep='')
