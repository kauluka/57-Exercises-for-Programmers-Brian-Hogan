# 9. Paint Calculator

p_length = input("What is the length of the ceiling? ")
p_width = input("What is the width of the ceiling? ")

p_area = int(p_length)*int(p_width)

# 1 gallon covers 350 square feet
p1_gallon = 350 

def paint_calculator(x):
    """
    input: one number
    output: the amount of gallons of paint needed to paint the ceiling of a room 
    """
    answer = p_area // p1_gallon 
    return answer

print("you will need to purchase ", paint_calculator(int(p_area)), "gallons of paint to cover", p_area, " square feet.")
