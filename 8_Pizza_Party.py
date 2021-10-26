# 8. Pizza Party 

people_amt = input("What is the number of people? ")
pizza_amt = input("What is the number of pizzas? ")
slices_amt = input("How many slices are in a pizza? ")

people_amt = int(people_amt)
pizza_amt = int(pizza_amt)
slices_amt = int(slices_amt)

total_slices = pizza_amt*slices_amt
pieces_to_eat = people_amt*2

leftover_amt = total_slices - pieces_to_eat

print(people_amt, "people with ", pizza_amt, " pizzas.")
print("Each person gets  2 pieces of pizza.")
print("There are ", leftover_amt, " leftover pieces.")