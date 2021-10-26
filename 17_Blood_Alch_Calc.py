# 17. Blood Alcohol Calculator

weight = float(input("What is your weight in pounds? "))
gender = (input("Are you a man or a woman? "))
number_drinks = float(input("How many drinks did you have? "))
amount_drinkv = float(input("How many ounces was a drink? "))
hours_since_ldrink = float(input("How many hours have passed since your last drink? "))

if gender == "man":
    BAC = ( (amount_drinkv * 5.14 ) / (weight * 0.73) ) - (0.15 * hours_since_ldrink)
    if BAC <= 0.08:
        print("Your BAC is ", BAC)
        print(" It is not legal for you to drive.")
    else:
        print("Your BAC is ", BAC)
        print(" It is legal for you to drive.")
else: # women
    BAC = ( (amount_drinkv * 5.14 ) / (weight * 0.66) ) - (0.15 * hours_since_ldrink)
    if BAC <= 0.08:
        print("Your BAC is ", BAC)
        print(" It is not legal for you to drive.")
    else:
        print("Your BAC is ", BAC)
        print(" It is legal for you to drive.")
