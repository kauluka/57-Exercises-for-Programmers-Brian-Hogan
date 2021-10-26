# 11. Currency Conversion

euro_amt = input("How many euros are you exchanging? ")
exc_rate = input("What is the current exchange rate? ")

euro_amt = float(euro_amt)
exc_rate = float(exc_rate)

dollar_amt = (euro_amt*exc_rate/100)

print(euro_amt, "euros at an exchange rate of", f'{exc_rate:.2f}', "is", f'{dollar_amt:.2f}', " U.S. dollars.")
