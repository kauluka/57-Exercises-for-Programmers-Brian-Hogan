 # 14. Tax Calcuator

WI_subtotal = float(input("What is the order amount? "))
state_WI = input("What is the state? ")

WI_tax_rate = 0.055
WI_tax = WI_subtotal*WI_tax_rate
WI_oos_total = WI_subtotal + WI_tax

if state_WI == "WI":
    print("The total is $", f'{WI_subtotal:.2f}')
else: 
    print("The subtotal is $", int(WI_subtotal))
    print("The tax is $", f'{WI_tax_rate:.2f}')
    print("The total is $", f'{WI_oos_total:.2f}')
