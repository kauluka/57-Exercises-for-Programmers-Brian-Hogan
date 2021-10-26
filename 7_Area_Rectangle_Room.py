# 7. Area of a Rectangular Room
length = input("What is the length of the room in feet? ")
width = input("What is the width of the room in feet? ")

length = int(length)
width = int(width)

area = length * width
sqft_sqmt = 0.092903

def square_meters(a):
    """
    input: one number
    output: the area of the arguments in square meters 
    """
    sq_answer = area*sqft_sqmt
    return sq_answer

print("You entered dimensions of ",length, "by", width, " feet.")
print("The area is")
print(area, " square feet", sep='')
print(square_meters(area), " square meters", sep='')
