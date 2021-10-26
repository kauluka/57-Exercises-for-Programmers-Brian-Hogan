#18 Temperature Converter

print("Press C to convert to Fahrenheit to Celsius.")
print("Press F to convert from Celsius to Fahrenheit.")
temp_choice = input("Your choice: ") # C or F 

the_temp = 0

def cels_2_f(q):
    """
    input: temperature in Celsius 
    output: the temperature in Fahrenheit 
    """
    temp_answer = (the_temp * (9/5) ) + 32
    return temp_answer

def fahr_2_c(q):
    """
    input: temperature in Fahrenheit 
    output: the temperature in Celsius 
    """
    temp_answer = (the_temp - 32) * 5 / 9 
    return temp_answer 

if temp_choice == "C" or "c":
    the_temp = float(input("Please enter the temperature in Fahrenheit: "))
    print("The temperature in Celsius is ", fahr_2_c(the_temp))
elif temp_choice == "F" or "f":
    the_temp = float(input("Please enter the temperature in Celsius: "))
    print("The temperature in Fahrenheit is ", cels_2_f(the_temp))