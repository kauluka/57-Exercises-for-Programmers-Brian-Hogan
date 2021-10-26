# 13. Determining Compound Interest 

p_amt = float(input("What is the principal amount? "))
r_amt = float(input("What is the rate? "))/100
num_oyears = float(input("What is the number of years? "))
c_time = float(input("What is the number of times the interest is compounded per year? "))

ci_output = p_amt * (1 + (r_amt/c_time))**(c_time*num_oyears)

print("$",f'{p_amt:.2f}', " invested at ", r_amt*100, "% for ", int(num_oyears), " years", sep='')
print("compounded ", int(c_time), " times per year is $", f'{ci_output:.2f}', ".", sep='')