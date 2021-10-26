# 10. Self-Checkout 
selfc_p = []
selfc_q = []
for i in range(3):
    item_price = input("Enter the price of the item: ")
    selfc_p.append(float(item_price))
    
    item_quantity = input("Enter the quantity for that item: ")
    selfc_q.append(float(item_quantity))
    print("{: ^50s}".format("The next item, please")) 

tax_rate = 0.055 

total_sc = []
for i in range(3):
    total = selfc_p[i]*selfc_q[i]
    total_sc.append(total)

#calculating the subtotal, tax and total values
total_sc=float((sum(total_sc)))

subtotal = total_sc
tax = tax_rate*subtotal
total = subtotal + tax

print("Subtotal: $", f'{subtotal:.2f}', sep='')
print("Tax: $", f'{tax:.2f}', sep='')
print("Total: $", f'{total:.2f}', sep='')